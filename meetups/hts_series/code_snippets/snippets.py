import numpy as np
import pandas as pd
from scipy import stats
import pymc3 as pm

# Sample the distribution
x = stats.norm.rvs(
    size=1000,
    loc=0,
    scale=1,
)

# Fitting the distribution
mu_fit, sigma_fit = stats.norm.fit(data=x)


with pm.Model() as model:
    # Specify the distribution
    y = pm.Normal(name="y", mu=0, sigma=1)
    # Sample
    trace = pm.sample(draws=1000)

x_pm = trace.get_values(varname="y")


index = np.zeros(len(x), dtype=np.int8)

with pm.Model() as mod:
    # Prior
    mu = pm.Normal(
        name="mu",
        mu=0,
        sigma=10,
        shape=1,
    )
    # Likelihood
    obs = pm.Normal(
        name="x",
        observed=x,
        mu=mu[index],
        sigma=1,
    )
    # Posterior
    trace = pm.sample(draws=1000)

mu_pm = trace.get_values(varname="mu")