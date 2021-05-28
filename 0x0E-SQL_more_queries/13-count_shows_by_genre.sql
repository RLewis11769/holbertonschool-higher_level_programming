-- Use join to find count of shows for each genre
SELECT tv_genres.name as genre, count(*) as number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
