import os

import joblib
import numpy as np
import pandas as pd

from utils import slice_procap

alleles_per_ind = pd.read_csv(
    "data/tiqtl/tiQTL_snps_per_individual.csv.gz", index_col=0
)
prefixes = list(alleles_per_ind.index)
snps = list(alleles_per_ind.columns)

# ref, alt, het
expt_tracks_per_snp_by_allele = {snps[i]: [[], []] for i in range(len(snps))}
pred_tracks_per_snp_by_allele = {snps[i]: [[], []] for i in range(len(snps))}
pred_quantity_per_snp_by_allele = {snps[i]: [[], []] for i in range(len(snps))}
expt_out = {snps[i]: [[], []] for i in range(len(snps))}
pred_track_out = {snps[i]: [[], []] for i in range(len(snps))}
pred_quantity_out = {snps[i]: [[], []] for i in range(len(snps))}

for pref in prefixes:
    expt_fp = os.path.join("/home2/ayh8/data/gse110638/", f"tiqtl/procap/{pref}.csv.gz")
    expt = pd.read_csv(expt_fp, index_col=0, header=None)
    for i in range(len(snps)):
        allele = alleles_per_ind[snps[i]][pref]
        if allele == 0:
            expt_tracks_per_snp_by_allele[snps[i]][0].append(expt.iloc[i])
        elif allele == 1:
            expt_tracks_per_snp_by_allele[snps[i]][1].append(expt.iloc[i])

for pref in prefixes:
    pred = np.load("predictions/puffin_tiqtl_predictions.npz")
    pred_scaled = (
        pd.DataFrame(pred["track"])
        .divide(pd.DataFrame(pred["track"]).sum(axis=1) + 1e-3, axis=0)
        .multiply(np.array(pred["quantity"]), axis=0)
    ).to_numpy()
    for i in range(len(snps)):
        allele = alleles_per_ind[snps[i]][pref]
        if allele == 0:
            pred_tracks_per_snp_by_allele[snps[i]][0].append(pred_scaled[i])
            pred_quantity_per_snp_by_allele[snps[i]][0].append(pred["quantity"][i][0])
        elif allele == 1:
            pred_tracks_per_snp_by_allele[snps[i]][1].append(pred_scaled[i])
            pred_quantity_per_snp_by_allele[snps[i]][1].append(pred["quantity"][i][0])
        elif allele == 0.5:
            pred_tracks_per_snp_by_allele[snps[i]][2].append(pred_scaled[i])
            pred_quantity_per_snp_by_allele[snps[i]][2].append(pred["quantity"][i][0])

for k in expt_tracks_per_snp_by_allele.keys():
    for i in range(len(expt_tracks_per_snp_by_allele[k])):
        expt_out[k][i] = slice_procap(
            np.array(expt_tracks_per_snp_by_allele[k][i]), 250
        )
    for i in range(len(pred_tracks_per_snp_by_allele[k])):
        pred_track_out[k][i] = np.array(pred_tracks_per_snp_by_allele[k][i])
        pred_quantity_out[k][i] = np.array(pred_quantity_per_snp_by_allele[k][i])

joblib.dump(
    expt_out,
    os.path.join(PREDICTDIR, "expt_tracks_per_snp_by_allele.joblib.gz"),
)
joblib.dump(
    pred_track_out,
    os.path.join(PREDICTDIR, "pred_tracks_per_snp_by_allele.joblib.gz"),
)
joblib.dump(
    pred_quantity_out,
    os.path.join(PREDICTDIR, "pred_quantity_per_snp_by_allele.joblib.gz"),
)
