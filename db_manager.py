import mariadb
import csv

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def create_connection(self):
        try:
            self.conn = mariadb.connect(
                user="root",
                password="password123",
                host="localhost",
                database="smart_products"
            )
            self.cursor = self.conn.cursor()
            print("Connected to MariaDB!")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INT PRIMARY KEY,
                    product_name VARCHAR(100),
                    category VARCHAR(50),
                    price DECIMAL(10, 2),
                    stock_quantity INT,
                    release_date DATE,
                    description TEXT
                )
            """)
            print("Table 'products' created successfully.")
        except mariadb.Error as e:
            print(f"Error creating table: {e}")

    def insert_products(self, products):
        try:
            self.cursor.executemany("""
                INSERT INTO products (product_id, product_name, category, price, stock_quantity, release_date, description)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, products)
            self.conn.commit()
            print("Products inserted successfully.")
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")

    def read_products(self):
        try:
            self.cursor.execute("SELECT * FROM products")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
        except mariadb.Error as e:
            print(f"Error reading data: {e}")

    def update_product(self, product_name, new_price, new_stock):
        try:
            self.cursor.execute("""
                UPDATE products SET price = ?, stock_quantity = ? WHERE product_name = ?
            """, (new_price, new_stock, product_name))
            self.conn.commit()
            print(f"Product '{product_name}' updated successfully.")
        except mariadb.Error as e:
            print(f"Error updating data: {e}")

    def delete_product(self, product_name):
        try:
            self.cursor.execute("""
                DELETE FROM products WHERE product_name = ?
            """, (product_name,))
            self.conn.commit()
            print(f"Product '{product_name}' deleted successfully.")
        except mariadb.Error as e:
            print(f"Error deleting data: {e}")

    def export_to_csv(self, filename):
        try:
            self.cursor.execute("SELECT * FROM products")
            rows = self.cursor.fetchall()
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['product_id', 'product_name', 'category', 'price', 'stock_quantity', 'release_date', 'description'])
                writer.writerows(rows)
            print(f"Data exported to {filename}")
        except mariadb.Error as e:
            print(f"Error exporting data: {e}")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Connection closed.")
