import pandas as pd
import mysql.connector

#Jhon Patrick Tacio
#BSIT-3

excel_file = "groceryItems.xlsx"
data = pd.read_excel(excel_file)


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="grocery_db"
)

cursor = connection.cursor()

sql = """
INSERT INTO products (item_id, item_name, category, price, quantity)
VALUES (%s, %s, %s, %s, %s)
"""

for _, row in data.iterrows():

    values = (
        row["item_id"],
        row["item_name"],
        row["category"],
        row["price"],
        row["quantity"]
    )

    cursor.execute(sql, values)

connection.commit()

print("Grocery data successfully transferred to MySQL!")

cursor.close()
connection.close()
