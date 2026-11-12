## Nairobi Distributors - Sales Tracker

A daily sales performance tracker for Nairobi Distributors.
Logs orders, counties, customer tiers and revenue. Predicts top customers and retention using SQL queries.

## What It Does

- Accepts order data (customer_name, county, product, quantity, unit_price, order_date)
- Links orders to customer tiers (Gold, Silver, Bronze)
- Calculates total spend per customer and per county
- Identifies loyal customers and top performers per county

## Setup
pip install pandas
python3 tracker.py
## Usage
import sqlite3, pandas as pd
conn = sqlite3.connect(":memory:")

1. All customers with their account tier
2. Total per customer last 3 years
3. Top customer by county (using subquery)
Queries Explained - What Each Query Answers And Why A Sales Manager Cares

**:*Query 1: ALL CUSTOMERS WITH THEIR ACCOUNT TIER*
SELECT o.order_id, o.customer_name, c.account_tier FROM orders o LEFT JOIN customers c ON o.customer_name = c.customer_name
- *Answers:* Which tier does each order belong to?
- *Why sales manager cares:* To prioritize Gold customers for retention offers and push Silver/Bronze to upgrade.

*Query 2: TOTAL PER CUSTOMER LAST 3 YEARS CONSECUTIVELY*
SELECT customer_name, SUM(quantity * unit_price) AS total FROM orders WHERE order_date >= date('now', '-3 years') GROUP BY customer_name
- *Answers:* How much has each customer spent in the last 3 consecutive years?
- *Why sales manager cares:* To identify consistent revenue drivers vs one-time buyers and forecast revenue.

*Query 3: TOP CUSTOMER BY COUNTY (Subquery)*
SELECT customer_name, county, total_value FROM (SELECT customer_name, county, SUM(quantity * unit_price) AS total_value FROM orders GROUP BY county, customer_name) ORDER BY total_value DESC
- *Answers:* Who is the highest spending customer in each county?
- *Why sales manager cares:* To assign the best sales rep to the biggest county customer and plan county-level promotions.

## Sample Output

NAIROBI DISTRIBUTORS.


1.ALL CUSTOMERS WITH THEIR ACCOUNT TIER:
 order_id     customer_name account_tier
       20      Akinyi Otieno         Gold

2.TOTAL PER CUSTOMER LAST 3 YEARS CONSECUTIVELY:
     customer_name  total
      Akinyi Otieno     .TOP CUSTOMER BY COUNTY:
     customer_name    county  total_value
      Barasa Wekesa  Kakamega        14800
## Stack

Python, sqlite3, pandas, SQL
 
