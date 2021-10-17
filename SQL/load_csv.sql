SET GLOBAL local_infile=1;
LOAD DATA LOCAL INFILE 'C:/Users/diego/cobify/datos.csv'
INTO TABLE videogame FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '\"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@column1, @column2, @column3,@column4, @column5, @column6, @column7, @column8,@column9, @column10, @column11,@column12, @column13)
SET distance=@column2, consume=@column3, speed=@column4, temp_inside=@column5, temp_outside=@column6, gas_type=@column7, AC=@column8, rain=@column9, sun=@column10, snow=@column11, time=@column12, precio=@column13
