import numpy as np
import pandas as pd
from scipy import stats
import pymc3 as pm

# Sample the distribution
x_a = stats.norm.rvs(
    size=1000,
    loc=0,
    scale=1,
)
x_b = stats.norm.rvs(
    size=500,
    loc=5,
    scale=1,
)
x_hierarchy = np.append(x_a, x_b)

# Fitting the distribution
mu_fit, sigma_fit = stats.norm.fit(data=x_hierarchy)

index_a = np.zeros(len(x_a), dtype=np.int8)
index_b = np.ones(len(x_b), dtype=np.int8)
index = np.append(index_a, index_b)

with pm.Model() as mod:
    # Prior
    mu = pm.Normal(
        name="mu",
        mu=0,
        sigma=10,
        shape=2,
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


with pm.Model() as hierarchical_mod:
    # Set a global prior for the parameters     
    mu_glob = pm.Normal(
        name="mu_glob",
        mu=1,
        sigma=0.1,
    )
    
    # Prior
    mu = pm.Normal(
        name="mu",
        mu=mu_glob,
        sigma=0.1,
        shape=2,
    )
    # Likelihood
    obs = pm.Normal(
        name="x",
        observed=x_hierarchy,
        mu=mu[index],
        sigma=1,
    )
    # Posterior
    trace = pm.sample(draws=1000)