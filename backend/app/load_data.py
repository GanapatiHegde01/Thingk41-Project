import csv
import psycopg2

# Update with your DB credentials
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="ecommerce",
    user="postgres",
    password="12345"
)

cursor = conn.cursor()

csv_file = '../products.csv'

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dept_name = row['department'].strip()

        # Check if department exists
        cursor.execute("SELECT id FROM departments WHERE name = %s", (dept_name,))
        dept = cursor.fetchone()

        if dept:
            dept_id = dept[0]
        else:
            # Insert new department
            cursor.execute("INSERT INTO departments (name) VALUES (%s) RETURNING id", (dept_name,))
            dept_id = cursor.fetchone()[0]

        # Insert product
        cursor.execute("""
            INSERT INTO products (name, brand, category, mrp, retail_price, dept_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row['name'],
            row['brand'],
            row['category'],
            float(row['mrp']) if row['mrp'] else None,
            float(row['retail_price']) if row['retail_price'] else None,
            dept_id
        ))

conn.commit()
cursor.close()
conn.close()
print("✅ Data loaded successfully.")
