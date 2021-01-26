```
$/gscratch/srlab/programs 
2bRAD_GATK		      DRAP				     macau				      perl			    smrtanalysis_2.3.0.140936.run
anaconda3		      exonerate-2.2.0-x86_64		     maker-2.31.10			      picard_2.18.4		    snap-2013-11-29
argparse-1.4.0		      express-1.5.1-linux_x86_64	     maker-3.01.03			      picard-2.9.1		    SOAPdenovo2
Augustus-3.3.2		      FastaIndex			     MaSuRCA-3.2.3			      pigz-2.4			    SOAPec_bin_v2.03
bamtools-2.5.1		      fastp-0.20.0			     mawk-1.3.4-20190203		      pilon			    SPAdes-3.13.0-Linux
bbmap_38.34		      FastQC-0.11.5			     mdust				      pitchfork			    SparseAssembler
bcftools-1.9		      fastqc_v0.11.8			     megahit_v1.1.4_LINUX_CPUONLY_x86_64-bin  platanus_1.2.4		    sqlite
bcl2fastq-v2.20		      fastqc_v0.11.9			     MEGAN6				      pstl			    sratoolkit.2.10.6-centos_linux64
bedtools-2.27.1		      freebayes-v.1.3.0-1		     MEGAN-6.18.3			      pyfaidx-0.5.5.2		    SSPACE-LongRead_v1-1
bin			      gapcloser-1.12			     MEGAN_Community_unix_6_17_0.sh	      pyScaf			    SSPACE-STANDARD-3.0_linux-x86_64
Bismark-0.19.0		      GARM_v0.7.5			     MEGAN_Community_unix_6_18_3.sh	      quast-4.5			    stacks-2.41
Bismark-0.21.0		      GATK				     MetaGeneMark_linux_64_3.38		      R-3.6.2			    STAR-2.7.6a
Bismark-0.21.0_dev	      gcc				     Metassembler			      racon			    stringtie-1.3.6.Linux_x86_64
Bismark-0.22.3		      get-pip.py			     miniconda3				      rainbow_2.0.4		    stringtie-2.1.4.Linux_x86_64
blast-2.2.17		      gffread-0.11.4.Linux_x86_64	     minimap2-2.17_x64-linux		      reago-1.1-release-2015.12.18  supernova-2.0.0
blat-v36x2		      git-sym				     modules				      redundans			    tbb
blat-v36x5		      graphviz-2.40.1			     mummer				      RepeatMasker-4.1.0	    tguenther-bayenv2_public-2b2b7f20bb62
bowtie2-2.1.0		      gt-1.5.10-Linux_x86_64-64bit-complete  MUMmer3.23				      resources			    tmhmm-2.0c
bowtie2-2.3.4.1-linux-x86_64  hisat2-2.1.0			     mummer-4.0.0beta2			      rmblast-2.10.0		    transdecoder
bowtie2-2.3.5.1-linux-x86_64  hisat2-2.2.0			     NanoPlot-1.29.1			      RNAMMER-1.2		    TransDecoder-v5.3.0
bowtie2-2.4.1-linux-x86_64    hmmer-2.3				     ncbi-blast-2.10.1+			      RSEM-1.3.3		    TransDecoder-v5.5.0
bsmap-2.89		      hmmer-3.1b2			     ncbi-blast-2.6.0+			      salmon-0.11.2-linux_x86_64    tree-1.8.0
busco-v3		      hmmer-3.2.1			     ncbi-blast-2.8.1+			      salmon-1.1.0_linux_x86_64     trf409.linux64
bwa-0.7.15		      hmmer-3.3				     ncbi-blast-2.8.1+_orginal		      salmon-1.2.1_linux_x86_64     TrimGalore-0.4.5
bwa-0.7.17		      htslib-1.9			     networkx-1.11			      samtools-1.10		    TrimGalore-0.6.6
canu			      infernal-1.1.1			     networkx2				      samtools-1.4		    Trimmomatic-0.33
cd-hit-v4.8.1-2019-0228       interproscan-5.31-70.0		     nseg				      samtools-1.9		    Trimmomatic-0.36
celera			      jellyfish-1.1.11			     ont-guppy_3.4.4			      scripts			    trinityrnaseq-v2.9.0
cmake-3.12.1		      jellyfish-2.2.10			     ont-guppy_4.0.15_linux64		      sedef			    Trinity-v2.8.3
dDocent-2.7.8		      jellyfish-2.3.0			     parallel-20180822			      seqtk-1.3			    Trinotate-v3.1.1
decorator-4.0.11	      jsoncpp-1.8.4			     parallel-20190922			      setuptools-36.0.1		    Trinotate-v3.2.0
detonate-1.11		      kmergenie-1.7048			     pblat-2.1				      Sibelia-3.0.7-Source	    vcflib
diamond-0.9.26		      krakenuniq-0.5.8			     PBSuite				      signalp-4.1		    vcftools-0.1.16
diamond-0.9.29		      last-852				     pear-0.9.11-linux-x86_64		      signalp-5.0b		    wtdbg-2.1_x64-linux
diamond-2.0.4		      likelybin-0.1.0			     pecan				      simuPOP-1.1.10.9
```

---

```
$/gscratch/srlab/programs/bin
argparse.py  bowtie2  bsmap  cutadapt  fastqc  multiqc	quast.py  README.txt  samtools	trim_galore
```

This directory  contains symlinks (i.e. shortcuts) to various programs and will simplify adding programs to your "system" $PATH (for many programs, this is not necessary, so you may not need/want to bother).

To add this directory (and it's programs) to your system $PATH, type the following in your Mox login node command prompt:

```printf "%s\n%s" "# Prepend bioinformatics stuff to PATH" "PATH=/gscratch/srlab/programs/bin:$PATH" >> ~/.bash_profile```

<em>To make the above command active, type ```bash``` at the command prompt (you only need to do this one time; your changes will be loaded each time you login).</em>

---

You should also add our custom modules directory to your `~/.bashrc` file. Modules are useful for certain software that has specific $PATH requirements. See the modules directory for more info on what custom modules are available (`/gscratch/srlab/programs/modules`).

```
printf "\n%s\n%s\n%s" "# Prepend custom modules to system ${MODULEPATH}" "MODULEPATH=/gscratch/srlab/programs/modules:${MODULEPATH}" "export MODULEPATH" \
>> ~/.bashrc
```

<em>To make the above command active, type ```bash``` at the command prompt (you only need to do this one time; your changes will be loaded each time you login).</em>