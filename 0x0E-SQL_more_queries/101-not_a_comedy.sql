-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT ts.title FROM tv_shows ts WHERE ts.title NOT IN (SELECT ts.title FROM tv_shows ts JOIN tv_show_genres tsg ON ts.id = tsg.show_id JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE tg.name = "Comedy") ORDER BY ts.title;
