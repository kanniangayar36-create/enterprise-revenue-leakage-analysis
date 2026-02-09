import pandas as pd

orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
discounts = pd.read_csv("discounts.csv")
logistics = pd.read_csv("logistics.csv")
returns = pd.read_csv("returns.csv")
support = pd.read_csv("support.csv")

df = orders.merge(products, on="product_id") \
           .merge(discounts, on="order_id") \
           .merge(logistics, on="order_id") \
           .merge(returns, on="order_id")

df["profit"] = (
    df["revenue"]
    - df["base_cost"]
    - df["discount_amount"]
    - df["shipping_cost"]
    - df["return_cost"]
)

customer_profit = df.groupby("customer_id").agg(
    revenue=("revenue", "sum"),
    profit=("profit", "sum")
).reset_index()

customer_profit = customer_profit.merge(support, on="customer_id")
customer_profit["net_profit"] = (
    customer_profit["profit"] - customer_profit["support_cost"]
)

toxic = customer_profit[customer_profit["net_profit"] < 0]

print("TOTAL PROFIT:", customer_profit["net_profit"].sum())
print("TOXIC CUSTOMERS:", toxic.shape[0])
customer_profit.to_csv("customer_profitability.csv", index=False)
toxic.to_csv("toxic_customers.csv", index=False)
print("csv files saved successfully")

