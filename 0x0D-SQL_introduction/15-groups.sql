-- Lists number of records with the same score in second_table of the database hbtn_0c_0
SELECT score, count(score) AS number FROM second_table GROUP BY score;
