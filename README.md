# DawidMaziarskiAiBD

Rezultaty zapytań wykonanych w programie pgAdmin 4

1. Ile rekordów znajduje się w tabeli nyc_streets?
SELECT COUNT(*) FROM nyc_streets

odpowiedź = 19091


2. Ile ulic w Nowym Jorku ma nazwy zaczynające się na „B”, „Q” i „M”?
SELECT COUNT(name) FROM nyc_streets
WHERE name LIKE 'B%'
OR name LIKE 'Q%'
OR name LIKE 'M%'

odpowiedź = 2102


3. Jaka jest populacja miasta Nowy Jork?
SELECT SUM(popn_total) FROM nyc_census_blocks

odpowiedź = 8175032


4. Jaka jest populacja Bronxu, Manhattanu i Queens?
SELECT SUM(popn_total) FROM nyc_census_blocks
WHERE boroname='The Bronx'

odpowiedź = 1385108


SELECT SUM(popn_total) FROM nyc_census_blocks
WHERE boroname='Manhattan'

odpowiedź = 1585873


SELECT SUM(popn_total) FROM nyc_census_blocks
WHERE boroname='Queens'

odpowiedź = 2230621


5. Ile dzielnic ("neighborhoods") znajduje się w każdej gminie (borough)?
SELECT boroname, COUNT(*) FROM nyc_neighborhoods
GROUP BY boroname

odpowiedź =
"Queens"	30
"Brooklyn"	23
"Staten Island"	24
"The Bronx"	24
"Manhattan"	28

