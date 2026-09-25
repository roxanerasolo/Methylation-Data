"""Rebuild the full ssnoob-normalized beta matrix (915,748 CpGs x 21 samples) from its parts."""
import glob
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def load_betas():
    parts = sorted(glob.glob(os.path.join(HERE, "ssnoob_betas_part*.csv.gz")))
    if not parts:
        raise FileNotFoundError("No ssnoob_betas_part*.csv.gz files found in " + HERE)
    return pd.concat(pd.read_csv(p, index_col=0) for p in parts)


if __name__ == "__main__":
    print(load_betas().shape)
