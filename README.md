
# Puffin benchmark

This fork of the Puffin repository contains a number of benchmarks of Puffin on the LCL PRO-cap dataset (https://doi.org/10.1038/s41467-020-19829-z) used to train the PRO-cap head of Puffin and CLIPNET (https://doi.org/10.1101/2024.03.13.583868). These benchmarks will be described in more detail in our CLIPNET manuscript (not yet added).

## Installation

Clone the repo:

```
git clone https://github.com/Danko-Lab/puffin_benchmark.git
cd puffin_benchmark
```

Install python dependencies (ideally in a new environment) using pip. If you have an existing Puffin environment, the only new packages are `tqdm` and `pyfastx`, so you can just install those on top of the existing dependencies.

```
pip install -r requirements.txt
```

For GPU support, make sure to install the version of Pytorch compiled to work on your CUDA version (https://pytorch.org/get-started/locally/). 

## CLIPNET test set prediction

TODO

## LCL initiation QTL prediction

TODO
