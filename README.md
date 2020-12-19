# naive-bayesians
Repo for the Naive Bayesian Meetup Group




```python
import pymc3 as pm

with pm.Model() as model: # model specifications in PyMC3 are wrapped in a with-statement
    # Define priors
    sigma = pm.HalfCauchy('sigma', beta=10, testval=1.)
    intercept = pm.Normal('intercept', 0, sd=20)
    x_coeff = pm.Normal('x', 0, sd=20)
    
    # Define likelihood
    likelihood = pm.Normal('y', 
                        mu=intercept + x_coeff * x, 
                        sd=sigma, 
                        observed=y)
    
    # Inference!
    trace = pm.sample(progressbar=False)

```