CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INT
);

INSERT INTO products (product_id, product_name, category, price, quantity)
VALUES
(1, 'Gaming Laptop', 'Laptop', 1299.99, 10),
(2, 'MacBook Air', 'Laptop', 1099.99, 8),
(3, 'Desktop Computer', 'Desktop', 899.99, 15),
(4, 'Gaming Monitor', 'Monitor', 349.99, 20),
(5, 'Wireless Keyboard', 'Accessories', 79.99, 30),
(6, 'Wireless Mouse', 'Accessories', 49.99, 40),
(7, 'Office Laptop', 'Laptop', 699.99, 12),
(8, '4K Monitor', 'Monitor', 499.99, 7);

SELECT *
FROM products;

SELECT *
FROM products
WHERE category = 'Laptop'
AND price < 1200;

SELECT *
FROM products
WHERE product_name LIKE '%Gaming%';

SELECT MIN(price) AS lowest_price
FROM products;

SELECT MAX(price) AS highest_price
FROM products;

SELECT
    MIN(price) AS lowest_price,
    MAX(price) AS highest_price
FROM products;

UPDATE products
SET price = 1199.99
WHERE product_id = 1;

SELECT *
FROM products
WHERE product_id = 1;

DELETE FROM products
WHERE product_id = 6;

SELECT *
FROM products;
