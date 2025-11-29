-- salam
SELECT id, name FROM cities
LEFT JOIN states ON cities.id = states.id
ORDER BY id ASC;
