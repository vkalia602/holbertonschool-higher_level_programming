-- script that lists all shows and all genres linked to that show
SELECT tv_shows.title, tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name
