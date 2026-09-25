"""Rebuild the full ssnoob-normalized beta matrix (930,596 CpGs x 21 samples, clock input) from its parts."""
import glob
import os

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))


def load_clock_betas():
    parts = sorted(glob.glob(os.path.join(HERE, "ssnoob_betas_clocks_part*.csv.gz")))
    if not parts:
        raise FileNotFoundError("No ssnoob_betas_clocks_part*.csv.gz files found in " + HERE)
    return pd.concat(pd.read_csv(p, index_col=0) for p in parts)


if __name__ == "__main__":
    print(load_clock_betas().shape)
