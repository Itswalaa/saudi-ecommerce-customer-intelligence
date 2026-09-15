# Saudi E-Commerce Customer Intelligence & Retention Platform

## Business Context & Executive Summary
E-commerce retention strategies require balancing customer lifetime value (LTV) against the cost of promotional campaigns. This project delivers an end-to-end customer intelligence platform designed for the Saudi e-commerce market (Riyadh, Jeddah, Dammam, Khobar, Madinah, Mecca).

Rather than simply classifying churn, this decision engine calculates **Revenue at Risk**, evaluates **Retention Economics (ROI)**, and assigns actionable intervention strategies to maximize net incremental revenue.

---

## Key Financial & Analytics Metrics
- **Total Revenue Reconciliation:** SAR 25,174,580.00 (Verified)
- **Total Revenue at Risk:** SAR 27,030.14
- **High-Priority Target Customers (P1):** 22 High-LTV / High-Risk Accounts
- **P1 Expected Incremental Net Value:** +SAR 2,113.19
- **Optimization Insight:** Unfiltered broad promotional campaigns (P2 tier) yield net negative ROI (-SAR 91,766.47). Interventions must be strictly targeted at High-LTV cohorts (P1) to maintain profitability.

---

## Technical Stack & Architecture
- **Data Engineering & Quality:** Python (Pandas, NumPy), SQLite, BigQuery
- **Analytical Modeling:** Advanced SQL (CTEs, Window Functions, NTILE for RFM Segmentation)
- **Predictive Analytics:** Logistic Regression (Leakage-Aware Churn Prediction)
- **Business Intelligence:** Power BI (DAX Measures, Cohort Retention Heatmaps, Decision Engine Deck)

---

## Project Structure
```text
saudi-ecommerce-customer-intelligence/
├── README.md
├── sql/
│   ├── 01_clean_orders.sql
│   ├── 02_customer_360.sql
│   ├── 03_rfm_scores.sql
│   └── 04_cohort_retention.sql
├── python/
│   ├── 01_data_generation.py
│   ├── 02_data_quality_audit.py
│   ├── 03_churn_model.py
│   └── 04_retention_economics.py
└── powerbi/
    └── dax_measures.md
---

**Developed by:** Walaa Saleh Al-Ghamdi  
*Data Analytics & Analytics Engineering Portfolio*
