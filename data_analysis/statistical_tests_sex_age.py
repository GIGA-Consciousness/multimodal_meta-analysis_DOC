# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 21:12:11 2025

@author: asala
"""

#test statistics for categorical variables, given a contingency tables (sex)

import numpy as np
from scipy.stats import chi2_contingency
obs = np.array([[797, 736, 294], [3052, 1940, 308]])
res = chi2_contingency(obs)
c=obs-res.expected_freq
print(res.statistic)
print(res.pvalue)
print(res.dof)
print(obs)
print(res.expected_freq)
print(c)

#test statistics for continuous variables, given n, mean and sd

#first test if variances are equal

import scipy.stats as stats

# Sample stats
n1, std1 = 1838, 13.95695513
n2, std2 = 5300, 14.80916513

# Ensure s1^2 is the larger variance
var1, var2 = std1**2, std2**2
df1, df2 = n1 - 1, n2 - 1

if var1 > var2:
    F = var1 / var2
    dfn, dfd = df1, df2
else:
    F = var2 / var1
    dfn, dfd = df2, df1

# Two-tailed p-value for F-test
p_value = 2 * min(stats.f.cdf(F, dfn, dfd), 1 - stats.f.cdf(F, dfn, dfd))

print(f"F-statistic: {F:.4f}")
print(f"Degrees of freedom: {dfn}, {dfd}")
print(f"P-value: {p_value:.4f}")

#variances NOT equal, p-val=0.0022

import numpy as np
from scipy import stats

# Sample data
n1, mean1, std1 = 1838, 42.68821054, 13.95695513
n2, mean2, std2 = 5300, 47.83615739, 14.80916513

# ---------------------------------------------------------
# Welch's t-test (does NOT assume equal variances)
# ---------------------------------------------------------

# Standard error of the difference
se = np.sqrt((std1**2 / n1) + (std2**2 / n2))

# t-statistic
t_stat = (mean1 - mean2) / se

# Welch-Satterthwaite degrees of freedom
df = (
    ((std1**2 / n1) + (std2**2 / n2))**2
    /
    (
        ((std1**2 / n1)**2 / (n1 - 1))
        +
        ((std2**2 / n2)**2 / (n2 - 1))
    )
)

# Two-tailed p-value
p_value = 2 * stats.t.sf(np.abs(t_stat), df)

print(f"T-statistic: {t_stat:.4f}")
print(f"Degrees of freedom: {df:.4f}")
print(f"P-value: {p_value:.16f}")


# ---------------------------------------------------------
# Effect size: Cohen's d using average variance
# ---------------------------------------------------------

# Standardizer based on the average of the two variances
s_avg = np.sqrt((std1**2 + std2**2) / 2)

# Cohen's d
cohen_d = (mean1 - mean2) / s_avg

print(f"Cohen's d (effect size): {cohen_d:.4f}")


# ---------------------------------------------------------
# Hedges' g (bias-corrected)
# ---------------------------------------------------------

# Small-sample correction based on Welch degrees of freedom
J = 1 - (3 / (4 * df - 1))

hedges_g = cohen_d * J

print(f"Hedges' g (bias-corrected effect size): {hedges_g:.4f}")

# ---------------------------------------------------------
# Approximate 95% confidence interval for Hedges' g
# (normal approximation; unequal group variances)
# ---------------------------------------------------------

from scipy.stats import norm

var_d = (
    (std1**2 / n1 + std2**2 / n2)
    / ((std1**2 + std2**2) / 2)
    + cohen_d**2 / (2 * (n1 + n2 - 2))
)
var_g = J**2 * var_d
se_g = np.sqrt(var_g)
z_critical = norm.ppf(0.975)
ci_lower_g = hedges_g - z_critical * se_g
ci_upper_g = hedges_g + z_critical * se_g

print(f"Hedges' g = {hedges_g:.4f}")
print(f"95% CI for Hedges' g: [{ci_lower_g:.4f}, {ci_upper_g:.4f}]")
