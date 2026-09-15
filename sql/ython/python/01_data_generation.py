import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# 1. Customers Generation
num_customers = 10000
customer_ids = [f"CUST_{i:05d}" for i in range(1, num_customers + 1)]

cities = ['Riyadh', 'Jeddah', 'Dammam', 'Khobar', 'Madinah', 'Mecca']
city_probs = [0.40, 0.25, 0.15, 0.10, 0.05, 0.05]

channels = ['Direct', 'Paid Search', 'Social Media', 'Referral', 'Organic']
channel_probs = [0.20, 0.35, 0.25, 0.10, 0.10]

profiles = ['Champion', 'At_Risk', 'Low_Value', 'Regular']
profile_probs = [0.15, 0.20, 0.35, 0.30]

start_date = datetime(2024, 1, 1)
signup_dates = [start_date + timedelta(days=int(np.random.randint(0, 500))) for _ in range(num_customers)]

df_customers = pd.DataFrame({
    'customer_id': customer_ids,
    'signup_date': signup_dates,
    'city': np.random.choice(cities, size=num_customers, p=city_probs),
    'age': np.random.randint(18, 65, size=num_customers),
    'acquisition_channel': np.random.choice(channels, size=num_customers, p=channel_probs),
    'behavioral_profile': np.random.choice(profiles, size=num_customers, p=profile_probs)
})

# 2. Products Generation
categories = ['Electronics', 'Apparel', 'Home & Kitchen', 'Beauty', 'Groceries']
products_data = []

p_id = 1
for cat in categories:
    for i in range(1, 11):
        price = np.random.uniform(20, 1500) if cat in ['Electronics', 'Home & Kitchen'] else np.random.uniform(10, 300)
        products_data.append({
            'product_id': f"PROD_{p_id:03d}",
            'category': cat,
            'base_price': round(price, 2)
        })
        p_id += 1

df_products = pd.DataFrame(products_data)

# 3. Orders Generation
orders_list = []
order_counter = 1
end_observation_date = start_date + timedelta(days=730)

payment_methods = ['Credit Card', 'Mada', 'Apple Pay', 'COD']
order_statuses = ['Completed', 'Completed', 'Completed', 'Cancelled', 'Returned']

for _, cust in df_customers.iterrows():
    c_id = cust['customer_id']
    profile = cust['behavioral_profile']
    signup = cust['signup_date']
    c_city = cust['city']
    
    if profile == 'Champion':
        n_orders = np.random.randint(10, 25)
        days_active_range = 600
    elif profile == 'At_Risk':
        n_orders = np.random.randint(8, 18)
        days_active_range = 300
    elif profile == 'Low_Value':
        n_orders = np.random.randint(1, 4)
        days_active_range = 400
    else:
        n_orders = np.random.randint(3, 8)
        days_active_range = 550
        
    for _ in range(n_orders):
        order_date = signup + timedelta(days=int(np.random.randint(0, days_active_range)))
        if order_date > end_observation_date:
            continue
            
        prod = df_products.sample(1).iloc[0]
        multiplier = np.random.uniform(1.1, 1.8) if profile == 'Champion' else np.random.uniform(0.8, 1.2)
        amount = round(prod['base_price'] * multiplier, 2)
        
        orders_list.append({
            'order_id': f"ORD_{order_counter:07d}",
            'customer_id': c_id,
            'order_date': order_date.strftime('%Y-%m-%d'),
            'product_id': prod['product_id'],
            'category': prod['category'],
            'city': c_city,
            'order_amount': amount,
            'payment_method': np.random.choice(payment_methods),
            'order_status': np.random.choice(order_statuses, p=[0.85, 0.05, 0.05, 0.03, 0.02])
        })
        order_counter += 1

df_orders = pd.DataFrame(orders_list)

# Save output
df_customers.drop(columns=['behavioral_profile']).to_csv('customers.csv', index=False)
df_products.to_csv('products.csv', index=False)
df_orders.to_csv('orders.csv', index=False)
