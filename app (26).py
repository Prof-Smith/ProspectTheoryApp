#!/usr/bin/env python
# coding: utf-8

# 
# # Prospect Theory Utility Elicitation
# This notebook allows students to input their certainty equivalents for risky prospects and compares them to corrected utility values using Prospect Theory. It calculates deviations and provides feedback on rationality.
# 

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Prospect Theory parameters
loss_aversion = 2.25  # lambda
alpha = 0.88          # curvature for gains
beta = 0.88           # curvature for losses

def weight(p):
    gamma = 0.61
    return np.exp(-(-np.log(p))**gamma)

def value(x):
    if x >= 0:
        return x**alpha
    else:
        return -loss_aversion * ((-x)**beta)


# In[ ]:


# Input student data: [amount, probability, certainty equivalent]
data = [
    [100, 0.9, 85],
    [200, 0.5, 90],
    [-100, 0.8, -70],
    [500, 0.1, 40],
    [-50, 0.5, -30]
]

results = []
for x, p, ce in data:
    pt_val = weight(p) * value(x)
    ce_val = value(ce)
    deviation = abs(pt_val - ce_val)
    feedback = "Rational" if deviation < 5 else ("Minor Bias" if deviation < 15 else "Significant Bias")
    results.append({
        'Prospect': f"{int(p*100)}% chance to {'win' if x>0 else 'lose'} ${abs(x)}",
        'Certainty Equivalent': ce,
        'PT Value': round(pt_val, 2),
        'CE Value': round(ce_val, 2),
        'Deviation': round(deviation, 2),
        'Feedback': feedback
    })

report_df = pd.DataFrame(results)
report_df


# In[ ]:


# Plot deviation
plt.figure(figsize=(8,5))
plt.bar(report_df['Prospect'], report_df['Deviation'], color='skyblue')
plt.ylabel('Deviation from PT Value')
plt.title('Rationality Deviation per Prospect')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# 
# ### Interpretation
# - **Deviation < 5**: Rational choice
# - **Deviation 5–15**: Minor bias detected
# - **Deviation > 15**: Significant behavioral bias
# Use this feedback to reflect on how your certainty equivalents align with Prospect Theory predictions.
# 
