import sqlite3, pandas as pd
conn = sqlite3.connect(":memory:")

conn.execute("CREATE TABLE orders (order_id INTEGER, customer_name TEXT, county TEXT, product TEXT, quantity INTEGER, unit_price REAL, order_date TEXT)")
conn.executemany("INSERT INTO orders VALUES (?,?,?,?,?,?,?)", [
    (1,"Akinyi Otieno","Kisumu","Maize Flour 5kg",2,1850,"2022-01-05"),
    (2,"John Kamau","Nairobi","Beans 2kg",3,450,"2022-06-06"),
    (3,"Chebet Rono","Nakuru","Cooking Oil 3L",1,1200,"2022-07-07"),
    (4,"Omar Ali","Mombasa","Rice 10kg",1,2100,"2023-01-08"),
    (5,"Wafula Njoroge","Bungoma","Sugar 2kg",5,320,"2023-03-10"),
    (6,"Njeri Mwangi","Kiambu","Maize Flour 2kg",10,180,"2023-05-12"),
    (7,"Atieno Odhiambo","Kisumu","Cooking Oil 5L",2,1800,"2023-08-15"),
    (8,"Kiplangat Bett","Kericho","Tea Leaves 500g",6,400,"2023-10-18"),
    (9,"Hassan Yusuf","Garissa","Beans 10kg",2,2100,"2023-11-20"),
    (10,"Mwikali Mutua","Machakos","Green Grams 2kg",4,300,"2024-01-22"),
    (11,"Barasa Wekesa","Kakamega","Maize Flour 5kg",8,1850,"2024-02-01"),
    (12,"Faith Cherop","Uasin Gishu","Milk 1L",20,65,"2024-02-03"),
    (13,"Peter Ochieng","Siaya","Omena 1kg",15,250,"2024-02-05"),
    (14,"Grace Auma","Kisumu","Sugar 5kg",3,780,"2024-02-10"),
    (15,"Kamau Kariuki","Nairobi","Rice 5kg",6,1100,"2024-02-12"),
    (16,"Linet Kerubo","Kisii","Maize Flour 10kg",4,3500,"2024-02-15"),
    (17,"Juma Bakari","Kilifi","Cooking Oil 3L",5,1200,"2024-02-18"),
    (18,"Wanjiku Kimani","Murang'a","Avocado 2kg",10,150,"2024-02-20"),
    (19,"Otieno Okello","Homa Bay","Fish Tilapia 1kg",8,600,"2024-03-01"),
    (20,"Akinyi Otieno","Kisumu","Beans 5kg",5,1100,"2024-03-10")
])

conn.execute("CREATE TABLE customers (customer_id INTEGER, customer_name TEXT, county TEXT, account_tier TEXT)")
conn.executemany("INSERT INTO customers VALUES (?,?,?,?)", [
    (101,"Akinyi Otieno","Kisumu","Gold"),
    (102,"John Kamau","Nairobi","Gold"),
    (103,"Chebet Rono","Nakuru","Silver"),
    (104,"Omar Ali","Mombasa","Bronze"),
    (105,"Wafula Njoroge","Bungoma","Gold"),
    (106,"Njeri Mwangi","Kiambu","Gold"),
    (107,"Atieno Odhiambo","Kisumu","Silver"),
    (108,"Kiplangat Bett","Kericho","Bronze"),
    (109,"Hassan Yusuf","Garissa","Silver"),
    (110,"Mwikali Mutua","Machakos","Bronze"),
    (111,"Barasa Wekesa","Kakamega","Gold"),
    (112,"Faith Cherop","Uasin Gishu","Silver"),
    (113,"Peter Ochieng","Siaya","Bronze"),
    (114,"Grace Auma","Kisumu","Gold"),
    (115,"Kamau Kariuki","Nairobi","Silver"),
    (116,"Linet Kerubo","Kisii","Gold"),
    (117,"Juma Bakari","Kilifi","Silver"),
    (118,"Wanjiku Kimani","Murang'a","Bronze"),
    (119,"Otieno Okello","Homa Bay","Gold")
])
conn.commit()

r = '=' *38
print(r)
print('NAIROBI DISTRIBUTORS.')
print(r)
print()

orders_customer_tier= """
SELECT o.order_id, o.customer_name, c.account_tier
FROM orders o
LEFT JOIN customers c ON o.customer_name = c.customer_name
ORDER BY order_id DESC
"""
quiz_1 = pd.read_sql_query(orders_customer_tier, conn)
print("1.ALL CUSTOMERS WITH THEIR ACCOUNT TIER:")
print(r)
print(quiz_1.to_string(index=False))
print(r)

total_customer= """
SELECT o.customer_name, SUM(o.quantity * o.unit_price) AS total_per_customer
FROM orders o
WHERE o.order_date >= date('now', '-3 years')
GROUP BY o.customer_name
ORDER BY total_per_customer DESC
"""
quiz_2 = pd.read_sql_query(total_customer, conn)
print("2.TOTAL PER CUSTOMER LAST 3 YEARS CONSECUTIVELY:")
print(r)
print(quiz_2.to_string(index=False))
print(r)

top_customer= """
SELECT customer_name, county, total_value FROM (
    SELECT customer_name, county, SUM(quantity * unit_price) AS total_value
    FROM orders
    GROUP BY county, customer_name
)
ORDER BY total_value DESC
"""
quiz_3 = pd.read_sql_query(top_customer, conn)
print("3.TOP CUSTOMER BY COUNTY:")
print(r)
print(quiz_3.to_string(index=False))
print(r)

