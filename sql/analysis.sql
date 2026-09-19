-- 1. Average Sales by Promotion

SELECT
    promo,
    ROUND(AVG(sales),2) AS avg_sales
FROM rossmann
GROUP BY promo;

-- 2. Total Sales by Day of Week

SELECT
    dayofweek,
    SUM(sales) AS total_sales
FROM rossmann
GROUP BY dayofweek;

-- 3. Top 5 Stores by Total Sales

SELECT
    store,
    SUM(sales) AS total_sales
FROM rossmann
GROUP BY store
ORDER BY total_sales DESC
LIMIT 5;

-- 4. Top 5 Stores by Average Sales

SELECT
    store,
    AVG(sales) AS avg_sales
FROM rossmann
GROUP BY store
ORDER BY avg_sales DESC
LIMIT 5;

-- 5. Average Sales When Promotion is Running

SELECT
    store,
    AVG(sales) AS avg_sales
FROM rossmann
WHERE promo = 1
GROUP BY store;

-- 6. Open Days per Store

SELECT
    store,
    COUNT(*) AS open_days
FROM rossmann
WHERE open = 1
GROUP BY store;

-- 7. Average Sales by Day of Week

SELECT
    dayofweek,
    AVG(sales) AS avg_sales
FROM rossmann
GROUP BY dayofweek;

-- 8. Maximum Sales by Day of Week

SELECT
    dayofweek,
    MAX(sales) AS max_sales
FROM rossmann
GROUP BY dayofweek;

-- 9. Sales During Promotion and Open Stores

SELECT
    store,
    SUM(sales) AS total_sales
FROM rossmann
WHERE promo = 1
AND open = 1
GROUP BY store;

-- 10. High Performing Stores

SELECT
    store,
    AVG(sales) AS avg_sales,
    SUM(customers) AS total_customers
FROM rossmann
GROUP BY store
HAVING AVG(sales) > 8000
AND SUM(customers) > 100000;