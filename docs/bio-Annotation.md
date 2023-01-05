
# Annotation

## Intro (Blast)
Blast is a key component of working with lesser studied taxa. Here are some resources to help with this.

**First off, you should be familar with the command line interface and bash**

- [Introducing the Shell](http://swcarpentry.github.io/shell-novice/01-intro/)
- [Introduction to the Command Line for Genomics](https://datacarpentry.org/shell-genomics/)
- <https://explainshell.com/>

---


### Blast Notebooks

- <https://github.com/RobertsLab/code/blob/master/09-blast.ipynb> - An example of how one might take a multi sequence fasta file and using NCBI Blast, compare the sequences with the Swiss-Prot Database on their own computer.

- <https://github.com/RobertsLab/code/blob/master/10-blast-2-slim.ipynb> - A notebook to seamlessly take blast output to GO Slim list

- <https://github.com/RobertsLab/code/blob/master/script-box/complete_go_annotation_notebook.Rmd> -

- https://github.com/sr320/ceabigr/blob/main/code/17-Swiss-Prot-Annotation.Rmd -  Blasting C virginica to Swiss-Prot. Author: Steven Roberts ![GitHub last commit](https://img.shields.io/github/last-commit/sr320/ceabigr)

## Genome features
In addition to sequence database alignment, finding spatial relationship within a genome is also an import approach for annotation. Often this is done using software tools such as `bedtools`.

### `bedtools::intersectbed`
see also https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html

## Transcriptome (Trinity)

After [transcriptome assembly using Trinity](https://robertslab.github.io/resources/bio_Transcriptome-assembly/), in order:

1. Transdecoder

  - Identify longest open reading frames (ORFs).

  - Use transcriptome assembly and gene-trans map from [Trinity assembly](https://robertslab.github.io/resources/bio_Transcriptome-assembly/).

    ```
    TransDecoder.LongOrfs \
    --gene_trans_map Trinity.fasta.gene_trans_map \
    -t Trinity.fasta"
    ```

2. BLASTp

  - Run blastp on long ORFs from Step 1 above.

  - Output format 6 produces a standard BLAST tab-delimited file.

  - Settings are recommended in TransDecoder documentation.

  - Peptide database (`-db uniprot_sprot.pep`) is supplied with Trinotate (e.g. `Trinotate-v3.1.1/admin/uniprot_sprot.pep`), but can be changed to use your own version.

    ```
    blastp \
    -query longest_orfs.pep \
    -db uniprot_sprot.pep \
    -max_target_seqs 1 \
    -outfmt 6 \
    -evalue 1e-5 \
    -num_threads ${threads} \
    > Trinity.fasta.blastp.outfmt6
    ```

3. BLASTx ([`DIAMOND`](https://github.com/bbuchfink/diamond))

  - Run [`DIAMOND`](https://github.com/bbuchfink/diamond) blastx on long ORFs from Step 1 above.

  - Output format 6 produces a standard BLAST tab-delimited file.

  - Settings (`--evalue` and `--max-target-seqs`) are recommended in TransDecoder documentation.

  - `--block-size` and `--index-chunks` are specific to running [`DIAMOND`](https://github.com/bbuchfink/diamond) BLASTx.

  - `--db uniprot_sprot.dmnd` is a [`DIAMOND`](https://github.com/bbuchfink/diamond)-formatted BLAST database. User can generate their own.

        ```
        diamond blastx \
        --db uniprot_sprot.dmnd \
        --query Trinity.fasta \
        --out Trinity.fasta.blastx.outfmt6 \
        --outfmt 6 \
        --evalue 1e-4 \
        --max-target-seqs 1 \
        --block-size 15.0 \
        --index-chunks 4
        ```


4. pFam

  - Run pfam search on long ORFs from Step 1 above.

  - Protein hidden Markov model database (`Pfam-A.hmm`) is supplied with Trinotate (e.g. `Trinotate-v3.1.1/admin/Pfam-A.hmm`), but can be changed to use your own version.

  - Uses 

    ```
    hmmscan \
    --cpu ${threads} \
    --domtblout Trinity.fasta.pfam.domtblout \
    Pfam-A.hmm \
    longest_orfs.pep
    ```



5. Transdecoder

  - Run Transdecoder using transcriptome assembly FastA, `blastp` and `Pfam` results.

   ```
   TransDecoder.Predict \
     -t Trinity.fasta \
    --retain_pfam_hits Trinity.fasta.pfam.domtblout \
    --retain_blastp_hits Trinity.fasta.blastp.outfmt6
   ```

6. Trinotate

  - Trinotate requires a large number of steps and programs!

    - Run `signalp`

        ```
        signalp \
        -f short \
        -n Trinity.fasta.trinotate.signalp.out \
        longest_orfs.pep
        ```

    - Run `tmHMM`

        ```
        tmhmm \
        --short \
        < longest_orfs.pep \
        > Trinity.fasta.trinotate.tmhmm.out
        ```

    - Run `RNAmmer`

      - Uses a special Trinotate implementation of `rnammer` (e.g. `Trinotate/util/rnammer_support/RnammerTranscriptome.pl`)

        ```
        RnammerTranscriptome.pl \
        --transcriptome Trinity.fasta \
        --path_to_rnammer rnammer
        ```
    
    - Load transcripts and coding regions into Trinotate SQLite database

        ```
        Trinotate \
        Trinotate.sqlite \
        init \
        --gene_trans_map Trinity.fasta.gene_trans_map \
        --transcript_fasta Tinity.fasta \
        --transdecoder_pep longest_orfs.pep
        ```

    - Load BLASTp/x homologies into SQLite database

        ```
        Trinotate \
        Trinotate.sqlite \
        LOAD_swissprot_blastp \
        Trinity.fasta.blastp.outfmt6
        ```

        ```   
        Trinotate \
        Trinotate.sqlite \
        LOAD_swissprot_blastx \
        Trinity.fasta.blastx.outfmt6
        ```

    - Load Pfam into SQLite database

        ```
        Trinotate \
        Trinotate.sqlite \
        LOAD_pfam \
        Trinity.fasta.pfam.domtblout
        ```

    - Load transmembrane domains

        ```
        Trinotate \
        Trinotate.sqlite \
        LOAD_tmhmm \
        Trinity.fasta.trinotate.tmhmm.out
        ```

    - Load signal peptides

        ```
        Trinotate \
        Trinotate.sqlite \
        LOAD_signalp \
        Trinity.fasta.trinotate.signalp.out
        ```

    - Load RNAmmer

        ```
        Trinotate \
        Trinotate.sqlite \
        LOAD_rnammer \
        Trinity.fasta.rnammer.gff
        ```

    - Create annotation report

        ```
        Trinotate \
        Trinotate.sqlite \
        report \
        > Trinity.fasta.annotation_report.txt
        ```

    - Extract gene ontology (GO) terms from annotation report

        ```
        extract_GO_assignments_from_Trinotate_xls.pl \
        --Trinotate_xls Trinity.fasta.annotation_report.txt \
        -G \
        --include_ancestral_terms \
        > Trinity.fasta.go_annotations.txt
        ```

- Make transcript features annotation map

        ```
        Trinotate_get_feature_name_encoding_attributes.pl \
        Trinity.fasta.annotation_report.txt \
        > Trinity.fasta.annotation_feature_map.txt
        ```