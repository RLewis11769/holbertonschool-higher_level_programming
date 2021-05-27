-- Display 3 hottest cities during July and August
SELECT TOP 3 city, avg(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC;
