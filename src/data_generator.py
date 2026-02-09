import pandas as pd
import numpy as np

np.random.seed(1)

customers = pd.DataFrame({
    "customer_id": range(1, 101)
})

products = pd.DataFrame({
    "product_id": range(1, 21),
    "base_cost": np.random.randint(200, 800, 20)
})

orders = pd.DataFrame({
    "order_id": range(1, 501),
    "customer_id": np.random.choice(customers.customer_id, 500),
    "product_id": np.random.choice(products.product_id, 500),
    "revenue": np.random.randint(500, 3000, 500)
})

discounts = pd.DataFrame({
    "order_id": orders.order_id,
    "discount_amount": np.random.randint(0, 500, 500)
})

logistics = pd.DataFrame({
    "order_id": orders.order_id,
    "shipping_cost": np.random.randint(50, 300, 500)
})

returns = pd.DataFrame({
    "order_id": orders.order_id,
    "return_cost": np.random.choice([0, 300], 500)
})

support = pd.DataFrame({
    "customer_id": customers.customer_id,
    "support_cost": np.random.randint(50, 400, 100)
})

customers.to_csv("customers.csv", index=False)
products.to_csv("products.csv", index=False)
orders.to_csv("orders.csv", index=False)
discounts.to_csv("discounts.csv", index=False)
logistics.to_csv("logistics.csv", index=False)
returns.to_csv("returns.csv", index=False)
support.to_csv("support.csv", index=False)

print("DATA CREATED SUCCESSFULLY")
