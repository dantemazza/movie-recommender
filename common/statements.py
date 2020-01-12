table_creation = 'CREATE TABLE ratings(title varchar(50), rating tinyint, PRIMARY KEY(title));'
insert_rating = 'REPLACE INTO ratings(title, rating) VALUES("{}", {});'
get_ratings = "SELECT * FROM ratings"
