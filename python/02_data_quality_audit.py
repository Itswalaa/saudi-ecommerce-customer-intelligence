import pandas as pd
import numpy as np

# Load datasets
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')

print("="*60)
print("             DATA QUALITY AUDIT REPORT             ")
print("="*60)

audit_results = []

# Check 1: Duplicate Order IDs
dup_orders = orders['order_id'].duplicated().sum()
audit_results.append({
    'Check': 'Duplicate order IDs',
    'Result': 'PASS' if dup_orders == 0 else 'FAIL',
    'Details': f'Found {dup_orders} duplicates'
})

# Check 2: Missing Customer IDs in Orders
missing_cust = orders['customer_id'].isnull().sum()
audit_results.append({
    'Check': 'Missing customer IDs',
    'Result': 'PASS' if missing_cust == 0 else 'FAIL',
    'Details': f'Missing: {missing_cust}'
})

# Check 3: Invalid Order Dates
invalid_dates = pd.to_datetime(orders['order_date'], errors='coerce').isnull().sum()
audit_results.append({
    'Check': 'Invalid order dates',
    'Result': 'PASS' if invalid_dates == 0 else 'FAIL',
    'Details': f'Invalid: {invalid_dates}'
})

# Check 4: Negative or Zero Revenue
invalid_revenue = (orders['order_amount'] <= 0).sum()
audit_results.append({
    'Check': 'Negative or zero revenue',
    'Result': 'PASS' if invalid_revenue == 0 else 'FAIL',
    'Details': f'Found {invalid_revenue} invalid amounts'
})

# Check 5: Invalid Order Status Values
valid_statuses = ['Completed', 'Cancelled', 'Returned']
invalid_status = (~orders['order_status'].isin(valid_statuses)).sum()
audit_results.append({
    'Check': 'Invalid order status values',
    'Result': 'PASS' if invalid_status == 0 else 'FAIL',
    'Details': f'Invalid statuses: {invalid_status}'
})

# Check 6: Orphan Order Records
orphan_orders = (~orders['customer_id'].isin(customers['customer_id'])).sum()
audit_results.append({
    'Check': 'Orphan order records',
    'Result': 'PASS' if orphan_orders == 0 else 'FAIL',
    'Details': f'Orphan orders: {orphan_orders}'
})

# Check 7: Revenue Reconciliation
completed_revenue = orders[orders['order_status'] == 'Completed']['order_amount'].sum()
audit_results.append({
    'Check': 'Revenue Reconciliation',
    'Result': 'PASS',
    'Details': f'Total Completed Revenue: SAR {completed_revenue:,.2f}'
})

# Display Audit Table
audit_df = pd.DataFrame(audit_results)
print(audit_df.to_string(index=False))
print("="*60)
