-- Use two joins to find possible genres "Dexter" does not have
SELECT name
FROM tv_genres
WHERE name 
NOT IN
    (SELECT name 
    FROM tv_shows
    INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id 
    INNER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id 
    WHERE tv_shows.title = 'Dexter') 
ORDER BY name;
