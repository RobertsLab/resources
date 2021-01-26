Here we try to compile genomic resources such that they are readily available and somewhat described. An effort will be made to keep respective index files alongside so these files can be directly used in IGV _etc_.

##### Related Resources
- Archived Versions of this page - [091319](http://htmlpreview.github.io/?https://github.com/RobertsLab/resources/blob/master/archive/Genomic-Resources.091419.html);  

- [Nightingales (Google Sheet)](https://docs.google.com/spreadsheets/d/1_XqIOPVHSBVGscnjzDSWUeRL7HUHXfaHxVzec-I-8Xk/edit?usp=sharing) : Database of all raw high-throughput sequencing data


# _Chionoecetes bairdi_

## Genomes

* [cbai_genome_v1.01.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_genome_v1.01.fasta) (18MB)

  - MD5 = `5a08d8b0651484e3ff75fcf032804596`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/09/24/Assembly-Assessment-BUSCO-C.bairdi-Genome-v1.01-on-Mox.html):
  `C:0.4%[S:0.3%,D:0.1%],F:0.2%,M:99.4%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_genome_v1.01.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_genome_v1.01.fasta.fai)

  - Assembly from [20200923](https://robertslab.github.io/sams-notebook/2020/09/23/Data-Wrangling-Subsetting-cbai_genome_v1.0-Assembly-with-faidx.html)

    - Q7-filtered NanoPore data. Includes _Hematodinium_-infected sample.

    - Subset of `cbai_genome_v1.0.fasta` with contigs >1000bp

* [cbai_genome_v1.0.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_genome_v1.0.fasta) (19MB)

  - MD5 = `2f3b651bb0b875b0287e71e315cad59a`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/09/18/Assembly-Assessment-BUSCO-C.bairdi-Genome-v1.0-on-Mox.html):
  `C:0.4%[S:0.3%,D:0.1%],F:0.3%,M:99.3%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_genome_v1.0.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_genome_v1.0.fasta.fai)

  - Assembly from [20200917](https://robertslab.github.io/sams-notebook/2020/09/17/Genome-Assembly-C.bairdi-cbai_v1.0-Using-All-NanoPore-Data-With-Flye-on-Mox.html)

    - Q7-filtered NanoPore data. Includes _Hematodinium_-infected sample.

## Transcriptomes

* [RNA-seq sample list](https://docs.google.com/spreadsheets/d/1d17yg5F5gKKC66O8QkTIlPxljJeuX7ZsG46pkBr1lNQ/edit#gid=0)

* [cbai_transcriptome_v3.1.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v3.1.fasta)

  - MD5 = `aeec8ffbf8fa44fb1750caee6abaf68a`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/06/05/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-Transcriptome-v3.1.html): `C:96.5%[S:40.3%,D:56.2%],F:2.2%,M:1.3%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v3.1.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v3.1.fasta.fai)

  - [BLASTx annotation](https://gannet.fish.washington.edu/Atumefaciens/20200608_cbai_diamond_blastx_v2.1_v3.1/cbai_transcriptome_v3.1.blastx.outfmt6) (outfmt6)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200828_cbai_trinotate_transcriptome-v3.1/20200828.cbai_transcriptome_v3.1.fasta.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-UW with _non_Alveolata_. [Derived from `cbai_transcriptome_v3.0.fasta`](https://robertslab.github.io/sams-notebook/2020/06/05/Sequence-Extractions-C.bairdi-Transcriptomes-v2.0-and-v3.0-Excluding-Alveolata-with-MEGAN6-on-Swoose.html)

* [cbai_transcriptome_v3.0.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v3.0.fasta)

  - Assembly from [20200518](https://robertslab.github.io/sams-notebook/2020/05/18/Transcriptome-Assembly-C.bairdi-All-Pooled-RNAseq-Data-Without-Taxonomic-Filters-with-Trinity-on-Mox.html)

  - MD5 = `5516789cbad5fa9009c3566003557875`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/05/19/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-Transcriptome-v3.0.html): `C:97.6%[S:39.1%,D:58.5%],F:1.6%,M:0.8%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v3.0.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v3.0.fasta.fai)

  - [BLASTx annotation](https://gannet.fish.washington.edu/Atumefaciens/20200519_cbai_diamond_blastx_transcriptome_v3.0/20200518.C_bairdi.Trinity.blastx.outfmt6) (outfmt6)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200526_cbai_trinotate_transcriptome-v3.0/20200526.cbai_transcriptome_v3.0.fasta.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-UW with _no taxonomic filter_.

* [cbai_transcriptome_v2.1.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v2.1.fasta)

  - MD5 = `1fb788175f9bb7cd5145370a399ae857`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/06/05/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-Transcriptome-v2.1.html): `C:98.3%[S:25.2%,D:73.1%],F:1.4%,M:0.3%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v2.1.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v2.1.fasta.fai)

  - [BLASTx annotation](https://gannet.fish.washington.edu/Atumefaciens/20200608_cbai_diamond_blastx_v2.1_v3.1/cbai_transcriptome_v2.1.blastx.outfmt6)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200831_cbai_trinotate_transcriptome-v2.1/20200831.cbai_transcriptome_v2.1.fasta.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-GW, 2020-UW with _non_Alveolata_. [Derived from `cbai_transcriptome_v2.0.fasta`](https://robertslab.github.io/sams-notebook/2020/06/05/Sequence-Extractions-C.bairdi-Transcriptomes-v2.0-and-v3.0-Excluding-Alveolata-with-MEGAN6-on-Swoose.html)

* [cbai_transcriptome_v2.0.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v2.0.fasta)

  - Also referred to as [`20200507.C_bairdi.Trinity.fasta`](https://robertslab.github.io/sams-notebook/2020/05/02/Transcriptome-Assembly-C.bairdi-All-RNAseq-Data-Without-Taxonomic-Filters-with-Trinity-on-Mox.html).

  - MD5 = `01adbd54298495c147767b19ee5c0de9`
https://gannet.fish.washington.edu/Atumefaciens/20200526_cbai_trinotate_transcriptome-v3.0/20200526.cbai.trinotate.go_annotations.txt
  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/05/08/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-v2.0-Transcriptome.html): `C:98.8%[S:24.9%,D:73.9%],F:0.9%,M:0.3%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v2.0.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v2.0.fasta.fai)

  - [BLASTx annotation](https://gannet.fish.washington.edu/Atumefaciens/20200508_cbai_diamond_blastx_transcriptome-v2.0/20200507.C_bairdi.Trinity.blastx.outfmt6)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200513_cbai_trinotate_transcriptome-v2.0/20200513.cbai.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-GW, 2020-UW with _no taxonomic filter_.

* [cbai_transcriptome_v1.7.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.7.fasta)

  - MD5 = `032d1f81c7744736ebeefe7f63ed6d95`

  - Assembly from [20200527](https://robertslab.github.io/sams-notebook/2020/05/27/Transcriptome-Assembly-C.bairdi-All-Pooled-Arthropoda-only-RNAseq-Data-with-Trinity-on-Mox.html)

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v1.7.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.7.fasta.fai) :
        `https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.7.fasta.fai`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/05/27/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-Transcriptome-v1.7.html): `C:86.7%[S:66.5%,D:20.2%],F:8.2%,M:5.1%,n:978`

  - [BLASTx Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200527_cbai_diamond_blastx_transcriptome_v1.7/cbai_transcriptome_v1.7.blastx.outfmt6) (outfmt6)

  - [GO Terms Annotation] (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-UW with _Arthropoda_ only reads.


* [cbai_transcriptome_v1.6.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.6.fasta)

  - MD5 = `46d77ce86cdbbcac26bf1a6cb820651e`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v1.6.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.6.fasta.fai) :
      `https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.6.fasta.fai`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/05/19/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-Transcriptome-v1.6.html): `C:91.7%[S:62.6%,D:29.1%],F:6.2%,M:2.1%,n:978`

  - [BLASTx Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200519_cbai_diamond_blastx_transcriptome_v1.6/cbai_transcriptome_v1.6.blastx.outfmt6) (outfmt6)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200520_cbai_trinotate_transcriptome-v1.6/20200520.cbai_transcriptome_v1.6.fasta.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-GW, 2020-UW with _Arthropoda_ only reads.


* [cbai_transcriptome_v1.5.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.5.fasta)

  - MD5 = `e61d68c45728ffbb91e3d34c087d9aa9`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/04/07/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-MEGAN-Transcriptome.html): C:91.8%[S:64.0%,D:27.8%],F:5.9%,M:2.3%,n:978

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v1.5.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.5.fasta.fai) :
    `https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.5.fasta.fai`

  - Updated assembly from [20200330](https://robertslab.github.io/sams-notebook/2020/03/30/Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html). Also referred to as `20200408.C_bairdi.megan.Trinity.fasta`

  - [BLASTx Annotation](https://robertslab.github.io/sams-notebook/2020/04/08/Transcriptome-Annotation-C.bairdi-MEGAN-Trinity-Assembly-Using-DIAMOND-BLASTx-on-Mox.html)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200409_cbai_trinotate_megan/20200409.cbai.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019, 2020-GW with Arthropoda only reads.


* [cbai_transcriptome_v1.0.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.0.fasta)

  - MD5 = `fb28a203154b44b67ec2e2476d96d326`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/02/07/Transcriptome-Assessment-BUSCO-Metazoa-on-C.bairdi-MEGAN-Transcriptome.html): `C:85.5%[S:64.7%,D:20.8%],F:9.3%,M:5.2%,n:978`

  - FastA index (```samtools faidx```)

    - [cbai_transcriptome_v1.0.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.0.fasta.fai) :
    `https://owl.fish.washington.edu/halfshell/genomic-databank/cbai_transcriptome_v1.0.fasta.fasta.fai`

  - Initial Trinity assembly from [20200122](https://robertslab.github.io/sams-notebook/2020/01/22/Transcriptome-Assembly-C.bairdi-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html)

  - [BLASTx Annotation](https://robertslab.github.io/sams-notebook/2020/01/23/Transcriptome-Annotation-C.bairdi-MEGAN-Trinity-Assembly-Using-DIAMOND-BLASTx-on-Mox.html)

  - [GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200126_cbai_trinotate_megan/20200126.cbai.trinotate.go_annotations.txt) (Trinotate)

  - internal short-hand: includes 2018, 2019 with _Arthropoda_ only reads.

---

# _Crassostrea gigas_

##### Related Resources
- [Compilation of DNA Methylation Genome Feature Tracks (_Crassostrea gigas_)](https://figshare.com/articles/Compilation_of_DNA_Methylation_Genome_Feature_Tracks_Crassostrea_gigas_/1456226) _circa 2015_

- [Re-defining Cgigas Canonical features](http://onsnetwork.org/halfshell/2015/02/27/re-defining-cgigas-canonical-features/) _circa 2015_

- [Gigaton](http://gigaton.sigenae.org/ngspipelines/#!/NGSpipelines/Crassostrea%20gigas%20-%20GIGATON)

- [TJGR](https://github.com/RobertsLab/resources/blob/master/html/tjgr.markdown)

## Genome:

* [Crassostrea_gigas.oyster_v9.dna_sm.toplevel.fa](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel.fa) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel.fa`

  - MD5 = 6de9d1239eb10ea0545bed6c4e746d6c

  - FastA index (```samtools faidx```) :
    `http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel.fa.fai`

## Bisulfite Genome:

  - [Crassostrea_gigas.oyster_v9.dna_sm.toplevel_bisulfite.tar.gz](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel_bisulfite.tar.gz) :
  `http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel_bisulfite.tar.gz`

    - Gzipped tarball of bisulfite genome for use with Bismark
    - Creation details [here](https://robertslab.github.io/sams-notebook/2019/02/21/Data-Management-Create-C.gigas-Bisulfite-Genome-with-Bismark-on-Mox.html)


## Genome Feature Tracks

* [Cgigas_v9_gene.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_gene.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_gene.gff`

* [Cgigas_v9_exon.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_exon.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_exon.gff`

* [Cgigas_v9_intron.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_intron.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_intron.gff`

* [Cgigas_v9_TE.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_TE.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_TE.gff`

  - Contains [Tandem Repeats](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_TE-TANDEMREPEAT.gff) and [wublastx](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_TE-WUBLASTX.gff) features.

* [Cgigas_v9_CG.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_CG.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_CG.gff`

  - index: `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_CG.gff.idx`

* [Cgigas_v9_1k5p_gene_promoter.gff](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_1k5p_gene_promoter.gff) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_1k5p_gene_promoter.gff`

* [Cgigas_v9_COMP_gene_prom_TE.bed](https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_COMP_gene_prom_TE.bed) : `https://eagle.fish.washington.edu/trilobite/Crassostrea_gigas_v9_tracks/Cgigas_v9_COMP_gene_prom_TE.bed`

* [Crassostrea_gigas.oyster_v9.40.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.40.gff3) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.40.gff3`

  - MD5 = 90a747fbc94a0a9225c43f75cc40b9db

* [Crassostrea_gigas.oyster_v9.40.abinitio.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.40.abinitio.gff3) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.40.abinitio.gff3`

  - MD5 = c2a8c388f5a8afb22a115d61dee3dda0

* [Crassostrea_gigas.oyster_v9.40_mRNA.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.40_mRNA.gff3)
  - ```grep "mRNA" Crassostrea_gigas.oyster_v9.40.gff3 > Crassostrea_gigas.oyster_v9.40_mRNA.gff3```



---

# _Crassostrea virginica_

[NCBI FTP](ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/022/765/GCF_002022765.2_C_virginica-3.0/)

## Genomes:

* [Cvirginica_v300.fa](http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300.fa) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300.fa`

    - MD5 = f9135e323583dc77fc726e9df2677a32

    - FastA index (```samtools faidx```)

      - [Cvirginica_v300.fa.fai](http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300.fa.fai) :
      `http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300.fa.fai`



* [GCF_002022765.2_C_virginica-3.0_genomic.fna](ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/022/765/GCF_002022765.2_C_virginica-3.0/GCF_002022765.2_C_virginica-3.0_genomic.fna.gz) : `ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/022/765/GCF_002022765.2_C_virginica-3.0/GCF_002022765.2_C_virginica-3.0_genomic.fna.gz`

    - compressed version of `Cvirginica_v300.fa` (same files)

## Bisulfite Genomes:

- [Cvirginica_v300_bisulfite.tar.gz](http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300_bisulfite.tar.gz) :
`http://owl.fish.washington.edu/halfshell/genomic-databank/Cvirginica_v300_bisulfite.tar.gz`
  - Gzipped tarball of bisulfite genome for use with Bismark
  - Creation details [here](https://robertslab.github.io/sams-notebook/2019/02/21/Data-Management-Create-C.virginica-Bisulfite-Genome-wit-Bismark-on-Mox.html)



## Genome Feature Tracks



* [C_virginica-3.0_Gnomon_mRNA.gff3](http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_Gnomon_mRNA.gff3) : `http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_Gnomon_mRNA.gff3`


* [C_virginica-3.0_Gnomon_exon.bed](http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_Gnomon_exon.bed) : `http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_Gnomon_exon.bed`

* [C_virginica-3.0_intron.bed](http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_intron.bed) : `http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_intron.bed`

* [C_virginica-3.0_CG-motif.bed](http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_CG-motif.bed) : `http://eagle.fish.washington.edu/Cvirg_tracks/C_virginica-3.0_CG-motif.bed`

  - MD5 = f88c171bccf45a6f3afcf455b6be810f

  - Dead link in this Jupyter Notebook obscures details on how this was generated (via Galaxy):

    - https://github.com/sr320/nb-2018/blob/master/C_virginica/22-CG-track.ipynb


* [C_virginica-3.0_TE-all.gff](http://owl.fish.washington.edu/halfshell/genomic-databank/C_virginica-3.0_TE-all.gff) : `http://owl.fish.washington.edu/halfshell/genomic-databank/C_virginica-3.0_TE-all.gff`      

  - MD5 = d0d81fc6cf7525bc2c61984bee23521b    

  - [Details](http://onsnetwork.org/kubu4/2018/08/28/transposable-element-mapping-crassostrea-virginica-genome-cvirginica_v300-using-repeatmasker-4-07/)

* [C_virginica-3.0_TE-Cg.gff](http://owl.fish.washington.edu/halfshell/genomic-databank/C_virginica-3.0_TE-Cg.gff) : `http://owl.fish.washington.edu/halfshell/genomic-databank/C_virginica-3.0_TE-Cg.gff`      

  - MD5 = 83cd753c171076464fee1165b7e1c6ba

  - [Details](http://onsnetwork.org/kubu4/2018/08/28/transposable-element-mapping-crassostrea-virginica-genome-cvirginica_v300-using-repeatmasker-4-07/)


---

# _Hematodinium sp._ (Host: _Chionoecetes bairdi_)

## Transcriptomes

* [hemat_transcriptome_v1.5.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.5.fasta)

  - MD5 = `b8d4a3c1bad2e07da8431bf70bdabfdd`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/03/31/Transcriptome-Assessment-BUSCO-Metazoa-on-Hematodinium-MEGAN-Transcriptome.html): `C:25.6%[S:20.7%,D:4.9%],F:11.7%,M:62.7%,n:978`

  - FastA index (```samtools faidx```)

    - [hemat_transcriptome_v1.5.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.5.fasta.fai) :
    `https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.5.fasta.fai`

  - Updated assembly from [20200330](https://robertslab.github.io/sams-notebook/2020/03/30/Transcriptome-Assembly-Hematodinium-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html).

  - [BLASTx Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200331_hemat_diamond_blastx_megan/20200408.hemat.megan.Trinity.fasta.blastx.outfmt6) (txt; 355KB)

  - [Trinotate GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200408_hemat_trinotate_megan/20200408.hemat.trinotate.go_annotations.txt) (txt; 2.3MB)

  - internal short-hand: includes 2018, 2019, 2020-GW with _Alveolata_ only reads.

* [hemat_transcriptome_v1.0.fasta](https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.0.fasta) (3.9MB)

  - MD5 = `fa5eb74767d180af5265d2d1f80b6430`

  - [BUSCOs](https://robertslab.github.io/sams-notebook/2020/02/07/Transcriptome-Assessment-BUSCO-Metazoa-on-Hematodinium-MEGAN-Transcriptome.html): `C:25.1%[S:19.2%,D:5.9%],F:9.5%,M:65.4%,n:978`

  - FastA index (```samtools faidx```)

    - [hemat_transcriptome_v1.0.fasta.fai](https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.0.fasta.fai) :
    `https://owl.fish.washington.edu/halfshell/genomic-databank/hemat_transcriptome_v1.0.fasta.fai`

  - Initial Trinity assembly from [20200122](https://robertslab.github.io/sams-notebook/2020/01/22/Transcriptome-Assembly-Hematodinium-with-MEGAN6-Taxonomy-specific-Reads-with-Trinity-on-Mox.html)

  - [BLASTx Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200123_hemat_diamond_blastx_megan/20200122.hemat.megan.Trinity.blastx.outfmt6) (txt; 308KB)

  - [Trinotate GO Terms Annotation](https://gannet.fish.washington.edu/Atumefaciens/20200126_hemat_trinotate_megan/20200126.hemat.trinotate.go_annotations.txt) (txt; 2.1MB)

  - internal short-hand: includes 2018, 2019 with _Alveolata_ only reads.

---

# _Metacarcinus magister_ (_Cancer magister_)

## Genome:

* `mmag_pilon_scaffolds.fasta`

  - MD5 = 5dfa2ba11edf0ff8191f112e0b1378d1

  - Not shared publicly until permission received from NOAA.

  - Roberts Lab members can access on Owl: `/web/halfshell/genomic-databank/mmag_pilon_scaffolds.fasta`

  - Original filename: `pilon_scaffolds.fasta`

  - FastA index (```samtools faidx```)

    - `mmag_pilon_scaffolds.fasta.fai`

---

# _Ostrea lurida_

## Genome:

* [Olurida_v081.fa](http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081.fa) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081.fa`

  - MD5 = 3ac56372bd62038f264d27eef0883bd3

  - This is `v080` with only contigs > 1000bp. Details of how `v080` was reduced found [here](https://github.com/sr320/nb-2018/blob/master/O_lurida/04-Pbjelly-10k-mapping.ipynb).

  - FastA index (```samtools faidx```)

    - [Olurida_v081.fa.fai](http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081.fa.fai) :
    `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081.fa.fai`


* [Olurida_v080.fa](http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v080.fa) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v080.fa`

  - MD5 = 9258398f554493e08fdc30e9c1409864

  - FastA index (```samtools faidx```)

    - [Olurida_v080.fa.fai](http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v080.fa.fai) :
    `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v080.fa.fai`

  - Also known as `pbjelly_sjw_01`. Details found [here](https://github.com/sr320/LabDocs/blob/master/jupyter_nbs/sam/20171130_emu_pbjelly.ipynb), though confirmation would be good.

  ## Bisulfite Genomes:

    - [Olurida_v080_bisulfite.tar.gz](http://owl.fish.washington.edu/halfshell/genomic-databank/Crassostrea_gigas.oyster_v9.dna_sm.toplevel_bisulfite.tar.gz) :
    `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v080_bisulfite.tar.gz`

      - Gzipped tarball of bisulfite genome for use with Bismark
      - Creation details [here](https://robertslab.github.io/sams-notebook/2018/05/08/bs-seq-mapping-olympia-oyster-bisulfite-sequencing-trimgalore-fastqc-bismark.html)

## Transcriptomes:

* [Olurida_transcriptome_v3.fasta](http://eagle.fish.washington.edu/cnidarian/Olurida_transcriptome_v3.fasta)

  - MD5 = 9da3242af2be0463051ec7e1f39b2593

#### Tissue-specific transcriptomes generated by Katherine Silliman

- [Olurida_CA_adductor_Trinity.fasta.gz](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_CA_adductor_Trinity.fasta.gz)

- [Olurida_CA_ctenidia_Trinity.fasta.gz](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_CA_ctenidia_Trinity.fasta.gz)

- [Olurida_CA_mantle_Trinity.fasta.gz](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_CA_mantle_Trinity.fasta.gz)

- [Olurida_gonad_Trinity.fasta.gz](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_gonad_Trinity.fasta.gz)


## Genome Feature Tracks

* [Olurida_v081_genome_snap02.all.renamed.putative_function.domain_added.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_genome_snap02.all.renamed.putative_function.domain_added.gff) (2.9GB) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_genome_snap02.all.renamed.putative_function.domain_added.gff`

  - MD5 = `f54512bd964f45645c34b1e8e403a2b0`

* [Olurida_v081-20190709.CDS.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.CDS.gff) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.CDS.gff`

* [Olurida_v081-20190709.exon.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.exon.gff) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.exon.gff`

* [Olurida_v081-20190709.gene.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.gene.gff) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.gene.gff`

* [Olurida_v081-20190709.mRNA.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.mRNA.gff) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081-20190709.mRNA.gff`

* [Olurida_v081_TE-Cg.gff](http:/owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_TE-Cg.gff) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_TE-Cg.gff`

  - MD5 = 977fd7cdb460cd0b9df5e875e1e880ea

  - Transposable Element track - more details in [Sam's Notebook](http://onsnetwork.org/kubu4/2018/07/03/transposable-element-mapping-olympia-oyster-genome-assembly-olurida_v081-using-repeatmasker-4-07/), including a [summary table](http://owl.fish.washington.edu/Athaliana/20180702_oly_repeatmasker_Cgigas/Olurida_v081.fa.tbl).

* [Olurida_v081_CG-motif.gff](https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_CG-motif.gff) : `https://owl.fish.washington.edu/halfshell/genomic-databank/Olurida_v081_CG-motif.gff`

---

# _Panopea generosa_

## Genome:    

* [Pgenerosa_v074.fa](http://owl.fish.washington.edu/halfshell/genomic-databank/Pgenerosa_v074.fa) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Pgenerosa_v074.fa`

  - [ENA Accession: GCA_902825435](https://www.ebi.ac.uk/ena/data/view/GCA_902825435)

  - Version of 070 containing 18 largest scaffolds ([details on subsetting](https://robertslab.github.io/sams-notebook/2019/06/25/Data-Wrangling-FastA-Subsetting-of-Pgenerosa_v070.fa-Using-samtools-faidx.html))

  - MD5 = 32976550b9030126c07920d5f2db179c

  - BUSCO scores:

    - `C:71.6%[S:70.7%,D:0.9%],F:4.7%,M:23.7%,n:978`
    - [Notebook entry](https://robertslab.github.io/sams-notebook/2019/07/10/Genome-Assessment-BUSCO-Metazoa-on-Pgenerosa_v074-on-Mox.html)

  - FastA index (```samtools faidx```) - `http://owl.fish.washington.edu/halfshell/genomic-databank/Pgenerosa_v074.fa.fai`


## Bisulfite Genome


## Genome Feature Tracks

#### Panopea-generosa-vv0.74.a3

- _These originate from [GenSAS annotation on 20190710](https://robertslab.github.io/sams-notebook/2019/07/10/Genome-Annotation-Pgenerosa_v074-Using-GenSAS.html)_

- BUSCO:

  - 68.4% complete BUSCOs


* [Panopea-generosa-vv0.74.a3.gene.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.gene.gff3) :
  `https://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.gene.gff3`

    - [code](https://d.pr/n/RHThn4)

* [Panopea-generosa-vv0.74.a3.exon.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.exon.gff3) :
`https://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.exon.gff3`

  - [code](https://d.pr/n/RHThn4)

* [Panopea-generosa-vv0.74.a3.intragenic.bed](https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.intragenic.bed) : `https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.intragenic.bed`

* [Panopea-generosa-vv0.74.a3.intron.bed](https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.intron.bed) : `https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.intron.bed`

* [Panopea-generosa-vv0.74.a3.rm.gff3](https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.rm.gff3) : `https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.rm.gff3`

  - index: `https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Panopea-generosa-vv0.74.a3.rm.gff3.idx`

* [Pgenerosa_v074.CpG.gff](https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Pgenerosa_v074.CpG.gff) : `https://gannet.fish.washington.edu/seashell/wd/091319/tracks/Pgenerosa_v074.CpG.gff`

* [Panopea-generosa-vv0.74.a3.CDS.gff3](http://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.CDS.gff3) :
  `https://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.CDS.gff3`

    - [code](https://d.pr/n/RHThn4)

* [Panopea-generosa-vv0.74.a3.mRNA.gff3](https://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.mRNA.gff3) :
`https://owl.fish.washington.edu/halfshell/genomic-databank/Panopea-generosa-vv0.74.a3.mRNA.gff3`

  - [code](https://d.pr/n/RHThn4)

---



## Transcriptome:

* [Pgenerosa_transcriptome_v5.fasta](http://owl.fish.washington.edu/halfshell/genomic-databank/Pgenerosa_transcriptome_v5.fasta) : `http://owl.fish.washington.edu/halfshell/genomic-databank/Pgenerosa_transcriptome_v5.fasta`

  - MD5 = 5a21424ecbc88c3b01daefe56bed79da

Transcriptome generated from various libaries - details [here](https://robertslab.github.io/sams-notebook/2018/09/04/transcriptome-assembly-geoduck-rnaseq-data.html)

---

# _QPX_

## Genome:

 * [QPX_v017.fasta](http://eagle.fish.washington.edu/QPX_genome/QPX_v017.fasta) : `http://eagle.fish.washington.edu/QPX_genome/QPX_v017.fasta`

CLC v5.1 Mismatch cost = 2; Perform scaffolding = Yes; Mapping mode = Map reads back to contigs (slow); Deletion cost = 3; Similarity fraction = 0.9; Length fraction = 0.8; Insertion cost = 3; Update contigs = Yes; Automatic word size = Yes; Minimum contig length = 10000; Automatic bubble size = Yes; input: filtered_QPX_DNA_GTGAAA_L001_R1 trimmed.

* [QPX_v017.fasta](https://ndownloader.figshare.com/files/3085550) : `https://ndownloader.figshare.com/files/3085550`

CLC v5.1 Mismatch cost = 2; Perform scaffolding = Yes; Mapping mode = Map reads back to contigs (slow); Deletion cost = 3; Similarity fraction = 0.9; Length fraction = 0.8; Insertion cost = 3; Update contigs = Yes; Automatic word size = Yes; Minimum contig length = 10000; Automatic bubble size = Yes; input: filtered_QPX_DNA_GTGAAA_L001_R1 trimmed.

* [QPX_v015.fasta](https://doi.org/10.1371/journal.pone.0074196.s001) : `https://doi.org/10.1371/journal.pone.0074196.s001`

>De novo assembly was performed with Genomics Workbench v. 5.0 (CLC Bio, Germany) on quality trimmed sequences with the following parameters: mismatch cost = 2, deletion cost = 3, similarity fraction = 0.9, insertion cost = 3, length fraction = 0.8 and minimum contig size of 100 bp for genomic data and 200 bp for transcriptomic data. In order to remove ribosomal RNA sequences from the transcriptome data, consensus sequences were compared to the NCBI nt database using the BLASTn algorithm [59]. Sequences with significant matches (9) were removed and not considered in subsequent analyses.

Manuscript: https://doi.org/10.1371/journal.pone.0074196





## Transcriptome:

* [QPX_transcriptome_v1_clean.fasta](http://eagle.fish.washington.edu/cnidarian/QPX_transcriptome_v1_clean.fasta)

QPX_Transcriptome v2.1

Subset of version 1 (v1) that only includes sequences with e-value < 1E-20. Based on Swiss-Prot blastx output, all sequences are oriented 5' - 3'. nucleotides between stop codons; minimum size 200.


---
