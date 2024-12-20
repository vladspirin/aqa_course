"""
HW 20.1. SQL.

1. Create a database for an online store with the following tables:
- 'products': a table to store information about products,
            including name, description, price, etc.
- 'categories': a table for product categories.
- the 'products' table should have a foreign key
referencing the 'categories' table.

2. Write an SQL script to create the specified tables.
3. Add a few rows of data to each table.
4. Execute a JOIN query that returns information
about the products and their category names.
"""

import sqlite3

conn = sqlite3.connect('online_store.db')
cursor = conn.cursor()

# Create a table 'categories'
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    description TEXT
    )
""")

# Create a table 'products'
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    name TEXT NOT NULL,
    brand TEXT,
    description TEXT,
    year INTEGER,
    price REAL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
    )
""")

# Add data to the table 'categories'
cursor.execute(
    'INSERT INTO categories (category_name, description) VALUES (?, ?)',
    ('Electronics', 'Electronic devices'),
)
cursor.execute(
    'INSERT INTO categories (category_name, description) VALUES (?, ?)',
    ('Clothing', 'Clothes and accessories'),
)
cursor.execute(
    'INSERT INTO categories (category_name, description) VALUES (?, ?)',
    ('Books', 'Books and magazines'),
)

# Add data to the table 'products'
cursor.execute(
    """INSERT INTO products (category_id, name, brand, description, price)
    VALUES (?, ?, ?, ?, ?)""",
    (1, 'Smartphone', 'Apple', 'iPhone 15 Pro 256G', 1249.99),
)
cursor.execute(
    """INSERT INTO products (category_id, name, brand, description, price)
    VALUES (?, ?, ?, ?, ?)""",
    (2, 'T-shirt', 'Nike', 'Cotton t-shirt', 9.99),
)
cursor.execute(
    """INSERT INTO products (category_id, name, brand, description, price)
    VALUES (?, ?, ?, ?, ?)""",
    (3, 'Book', 'No Starch Press', 'Python Crach Course', 12.00),
)

# Save (commit) the changes
conn.commit()

# Execute a JOIN query
cursor.execute("""
SELECT products.name,
        products.brand,
        products.description,
        products.price, categories.category_name
FROM products
JOIN categories ON products.category_id = categories.id
""")

if __name__ == '__main__':
    rows = cursor.fetchall()
    for row in rows:
        print(row)
