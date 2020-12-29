import numpy as np
import pandas as pd
import pymc3 as pm
from typing import Tuple


def create_dataset() -> Tuple:

    n = 20
    beta_opt_1 = 2.0
    beta_opt_2 = -5.0

    std_noise_x = 0.5

    x_1 = std_noise_x*np.random.randn(n)
    y_1 = beta_opt_1*x_1 + np.random.randn(n)

    x_2 = std_noise_x*np.random.randn(n)
    y_2 = beta_opt_2*x_2 + np.random.randn(n)


    df_1 = pd.DataFrame({"y": y_1, "x_1": x_1}).assign(**{"site": "site_A"}) 
    df_2 = pd.DataFrame({"y": y_2, "x_1": x_2}).assign(**{"site": "site_B"})

    data = pd.concat([df_1, df_2], axis="rows")

    return data



def main(): 
    return 1 
