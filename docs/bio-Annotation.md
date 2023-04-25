
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

---

## Gene Ontology (GO)

### Retrieve GO terms from UniProt Using SwissProt IDs

The following steps will use the UniProt Python API to create a tab-delimited file of data retrieved from UniProt.

1. Create newline-delimited file of SwissProt IDs. (e.g. `SPIDS.txt`)

    ```bash
    cat SPIDS.txt

    Q86IC9
    P04177
    Q8L840
    Q61043
    A1E2V0
    P34456
    P34457
    O00463
    Q00945
    Q5SWK7
    ```

2. Create Python file (e.g. `uniprot-retrieval.py`) with the following:

    ```python
    import re
    import zlib
    import gzip
    import requests
    from requests.adapters import HTTPAdapter, Retry
    import sys


    re_next_link = re.compile(r'<(.+)>; rel="next"')
    retries = Retry(total=5, backoff_factor=0.25, status_forcelist=[500, 502, 503, 504])
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retries))


    def get_next_link(headers):
        if "Link" in headers:
            match = re_next_link.match(headers["Link"])
            if match:
                return match.group(1)


    def get_batch(batch_url):
        while batch_url:
            response = session.get(batch_url)
            response.raise_for_status()
            total = response.headers["x-total-results"]
            yield response, total
            batch_url = get_next_link(response.headers)


    def main(accession_file):
        with open(accession_file, 'r') as f:
            accessions = f.read().splitlines()

        accession_query = '%29%20OR%20%28accession%3A'.join(accessions)
        url = f"https://rest.uniprot.org/uniprotkb/search?compressed=true&fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Clength%2Cgo_p%2Cgo_c%2Cgo_f%2Cgo%2Cgo_id&format=tsv&query=%28%28accession%3A{accession_query}%29%29&size=500"

        progress = 0
        lines = []
        for batch, total in get_batch(url):
            # Decompress each batch as we want to extract the header
            decompressed = zlib.decompress(batch.content, 16 + zlib.MAX_WBITS)
            batch_lines = [line for line in decompressed.decode("utf-8").split("\n") if line]
            if not progress:
                # First line so print TSV header
                lines = [batch_lines[0]]
            lines += batch_lines[1:]
            progress = len(lines) - 1
            print(f"{progress} / {total}")

        # Save lines to a gzip file
        with gzip.open("uniprot-retrieval.tsv.gz", "wt", encoding="utf-8") as f:
            f.write('\n'.join(lines))

    if __name__ == '__main__':
        main(sys.argv[1])
    ```

3. Run they Python script:

    ```bash
    python uniprot-retrieval.py SPIDS.txt
    ```

    The resulting output file (`uniprot-retrieval.tsv.gz`) will be in your working directory.

4. Gunzip the output file:

    ```bash
    gunzip uniprot-retrieval.tsv.gz
    ```

The resulting file (`uniprot-retrieval.tsv`) will be formatted with the following columns:

| Entry | Reviewed | Entry Name | Protein names | Gene Names | Organism | Length | Gene Ontology (biological process) | Gene Ontology (cellular component) | Gene Ontology (molecular function) | Gene Ontology (GO) | Gene Ontology IDs |
|-------|----------|------------|---------------|------------|----------|--------|------------------------------------|------------------------------------|------------------------------------|--------------------|-------------------|


NOTES:

- This requires Python >= 3 to run. Simplest way to access Python 3 is via a conda environment.

- On the first attempt, you'll likely need to install the packages that are being imported at the very beginning of the script.

- [Create an issue](https://github.com/RobertsLab/resources/issues) if you need help with any of the above.

---

## Genome features
In addition to sequence database alignment, finding spatial relationship within a genome is also an import approach for annotation. Often this is done using software tools such as `bedtools`.

### `bedtools::intersectbed`
see also https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html

---

## Transcriptome (Trinity)

After [transcriptome assembly using Trinity](https://robertslab.github.io/resources/bio_Transcriptome-assembly/), run the numbered steps below, in order.

NOTE: The following info is long and requires the use of many programs. All of the code listed below are solely examples. Making the commands functional requires a fair amount of organization (i.e. listing paths to programs and input/output files, creating subdirectories for organizing outputs, etc.). See the Use Cases at the end of this section for a more complete picture of how to organize/run this pipeline.

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

            - The output file is formatted like this (`<trinity-id>``<tab>``<GO:NNNNNN,GO:NNNNN,...>`):

            ```
            TRINITY_DN0_c0_g1	GO:0003674,GO:0003824,GO:0003964,GO:0006139,GO:0006259,GO:0006310,GO:0006313,GO:0006725,GO:0006807,GO:0008150,GO:0008152,GO:0009987,GO:0016740,GO:0016772,GO:0016779,GO:0032196,GO:0034061,GO:0034641,GO:0043170,GO:0044237,GO:0044238,GO:0044260,GO:0044699,GO:0044710,GO:0044763,GO:0046483,GO:0071704,GO:0090304,GO:1901360
            TRINITY_DN0_c10_g1	GO:0003674,GO:0003824,GO:0004659,GO:0004660,GO:0005488,GO:0005575,GO:0005829,GO:0005875,GO:0005965,GO:0006464,GO:0006807,GO:0008150,GO:0008152,GO:0008270,GO:0008318,GO:0009987,GO:0016740,GO:0016765,GO:0018342,GO:0018343,GO:0019538,GO:0032991,GO:0036211,GO:0043167,GO:0043169,GO:0043170,GO:0043234,GO:0043412,GO:0044237,GO:0044238,GO:0044260,GO:0044267,GO:0044422,GO:0044424,GO:0044430,GO:0044444,GO:0044446,GO:0044464,GO:0046872,GO:0046914,GO:0071704,GO:0097354,GO:1901564,GO:1902494,GO:1990234
            TRINITY_DN0_c2_g4	GO:0000166,GO:0003674,GO:0005488,GO:0005524,GO:0005575,GO:0005737,GO:0005856,GO:0017076,GO:0030554,GO:0032553,GO:0032555,GO:0032559,GO:0035639,GO:0036094,GO:0043167,GO:0043168,GO:0043226,GO:0043228,GO:0043229,GO:0043232,GO:0044424,GO:0044464,GO:0097159,GO:0097367,GO:1901265,GO:1901363
            ```

    - Make transcript features annotation map

            ```
            Trinotate_get_feature_name_encoding_attributes.pl \
            Trinity.fasta.annotation_report.txt \
            > Trinity.fasta.annotation_feature_map.txt
            ```