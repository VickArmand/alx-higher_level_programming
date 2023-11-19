-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tg.name FROM tv_genres tg WHERE tg.name NOT IN (SELECT tg.name FROM tv_shows ts JOIN tv_show_genres tsg ON ts.id = tsg.show_id JOIN tv_genres tg ON tsg.genre_id = tg.id WHERE ts.title = "Dexter") ORDER BY tg.name;
