"""
Calculates predictions on diQTLs mapped in Kristjandottir et al. (2020) and used to
benchmark CLIPNET (He et al., 2024).
"""

import glob
import os

import numpy as np

import puffin

# create a puffin model
puffin_model = puffin.Puffin(use_cuda=True)

# get the list of files
files = glob.glob("data/diqtls/*.hs37d5.bwa.uniqueUMI.fna.gz")

# numpy arrays of size (num_peaks, 2 strands, 500bp)
pred_profs_puffin = {
    os.path.split(fname)[-1]: puffin.puffin_predict(fname, puffin_model)
    for fname in files
}

# save the predictions
np.savez_compressed("predictions/puffin_diqtl_predictions.npz", **pred_profs_puffin)
