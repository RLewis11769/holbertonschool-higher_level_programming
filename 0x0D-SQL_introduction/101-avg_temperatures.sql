-- Display avg temp by city in descending order
SELECT city, avg(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
