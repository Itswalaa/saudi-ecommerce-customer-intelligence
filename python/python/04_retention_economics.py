import pandas as pd
import numpy as np

# 1. Load Churn Model Predictions
df = pd.read_csv('churn_predictions.csv')

# 2. Retention Economics Calculation Engine
def calculate_economics(row):
    prob = row['churn_probability']
    ltv = row['monetary']
    
    # Expected Revenue Loss
    rev_at_risk = prob * ltv
    
    # Tiering & Campaign Optimization Logic
    if prob >= 0.60 and ltv >= 1500:
        tier = 'P1 - High Priority'
        cost = 150.0
        success_rate = 0.35
    elif prob >= 0.40:
        tier = 'P2 - Medium Priority'
        cost = 50.0
        success_rate = 0.15
    elif prob < 0.40 and ltv >= 1000:
        tier = 'P3 - Low Priority'
        cost = 20.0
        success_rate = 0.05
    else:
        tier = 'P4 - Organic'
        cost = 0.0
        success_rate = 0.0
        
    exp_inc_val = (ltv * success_rate) - cost
    
    return pd.Series([tier, rev_at_risk, exp_inc_val, cost])

# 3. Apply Decision Logic
df[['priority_tier', 'revenue_at_risk', 'expected_incremental_value', 'campaign_cost']] = df.apply(calculate_economics, axis=1)

# 4. Generate Business ROI Summary
summary = df.groupby('priority_tier').agg(
    customer_count=('customer_id', 'count'),
    total_revenue_at_risk=('revenue_at_risk', 'sum'),
    expected_incremental_val=('expected_incremental_value', 'sum'),
    total_campaign_cost=('campaign_cost', 'sum')
).reset_index()

print("="*60)
print("            RETENTION INVESTMENT ROI SUMMARY             ")
print("="*60)
print(summary.to_string(index=False))
print("="*60)

# Save output for BI dashboarding
df.to_csv('customer_decision_engine.csv', index=False)
