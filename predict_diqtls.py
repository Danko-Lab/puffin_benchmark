"""
Calculates predictions on diQTLs mapped in Kristjandottir et al. (2020) and used to benchmark CLIPNET (He et al., 2024).
"""

import glob

import numpy as np
import pyfastx
import tqdm
from puffin import Puffin

puffin = Puffin(use_cuda=True)


def puffin_predict(fa_path, puffin_model, silence=False):
    """
    Code shamelessly *borrowed* from Kelly Cochran.
    """
    seqs = pyfastx.Fasta(fa_path)
    preds = []
    for rec in tqdm.tqdm(seqs, desc=f"Predicting on {fa_path}", disable=silence):
        raw_pred_df = puffin_model.predict(rec.seq)
        # select for the PRO-cap + and - strands from all outputs
        pred = np.array(
            [np.array(raw_pred_df)[6], np.array(raw_pred_df)[-1]]  # fwd strand
        )  # rev strand
        preds.append(pred)
    return np.array(preds).astype(float)


files = glob.glob("data/diQTLs/*.hs37d5.bwa.uniqueUMI.fna.gz")

pred_profs_puffin = {fname: puffin_predict(fname, puffin) for fname in files}

# numpy arrays of size (num_peaks, 2 strands, 500bp)

# save the predictions
np.savez_compressed("predictions/puffin_diQTL_predictions.npz", pred_profs_puffin)
