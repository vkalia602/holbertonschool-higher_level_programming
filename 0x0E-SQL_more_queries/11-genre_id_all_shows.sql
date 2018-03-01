-- Script that lists all shows contained in the database hbtn_0d_tvshows 
SELECT genre_id, tv_shows.title
FROM tv_show_genres
RIGHT OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, tv_show_genres.genre_id
