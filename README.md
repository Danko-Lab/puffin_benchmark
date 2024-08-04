
# Puffin benchmark

This fork of the Puffin repository contains a number of benchmarks of Puffin on the LCL PRO-cap dataset (https://doi.org/10.1038/s41467-020-19829-z) used to train the PRO-cap head of Puffin and CLIPNET (https://doi.org/10.1101/2024.03.13.583868). These benchmarks will be described in more detail in our CLIPNET manuscript (not yet added).

#### Installation
For running Puffin locally, clone this repository with the following command.

```
git clone https://github.com/jzhoulab/puffin.git
cd puffin
```

Install python dependencies of Puffin. We recommend creating a new environment (Python version >=3.6) and you can install dependencies using pip
```
pip install -r requirements.txt
```
or install these packages manually to your environment. For using GPU, install pytorch(>=1.7.0) according to [here](https://pytorch.org/get-started/locally/). 

####  Download model and relevant resource files

To download the genome fasta file run following commands
```
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz
mv  hg38.fa.gz ./resources
cd ./resources
gzip -d hg38.fa.gz
cd ../
```

To run the model prediciton use the following command, where input sequence length is 100Kbp
```
prediction = puffin_D.predict(sequence)
```
