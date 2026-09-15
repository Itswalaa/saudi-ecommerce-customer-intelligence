import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score

# 1. Load Customer 360 Dataset
df = pd.read_csv('customer_360.csv')

# 2. Define Target Variable (Churn: Inactive for > 90 days)
df['is_churned'] = (df['recency'] > 90).astype(int)

# 3. Select Features for Leakage-Aware Prediction
features = ['frequency', 'monetary', 'aov', 'age']
X = df[features]
y = df['is_churned']

# 4. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 5. Train Predictive Model
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# 6. Model Predictions & Probability Scores
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# 7. Output Model Performance Metrics
print("="*50)
print("          CHURN MODEL PERFORMANCE EVALUATION          ")
print("="*50)
print(classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_prob):.4f}")
print("="*50)

# Save predictions for Retention Economics layer
df['churn_probability'] = model.predict_proba(X)[:, 1]
df.to_csv('churn_predictions.csv', index=False)
