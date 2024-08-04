import numpy as np
import pandas as pd
from scipy.spatial.distance import jensenshannon as jsd
from scipy.stats import pearsonr

# os.environ["CUDA_VISIBLE_DEVICES"] = "1"
import puffin

puffin_model = puffin.Puffin(use_cuda=True)

pred_profs_puffin = puffin.puffin_predict(
    "data/clipnet_test/fixed_uniq_windows_puffin_clipnet_test.fa.gz", puffin_model
)

# save the predictions
np.savez_compressed(
    "clipnet_test_predictions/puffin_clipnet_test_predictions.npz", pred_profs_puffin
)

expt = pd.read_csv(
    "/home2/ayh8/data/lcl/fixed_windows/concat_procap_0_mean.csv.gz", header=None
)
pred_profs = pd.DataFrame(
    np.concatenate([pred_profs_puffin[:, 0, :], pred_profs_puffin[:, 1, :]], axis=1)
)
print("JSD: ", jsd(pred_profs, expt, axis=1))
print(
    "Pearson Quantity: ",
    pearsonr(np.log(expt.sum(axis=1)), np.log(pred_profs.sum(axis=1))),
)
