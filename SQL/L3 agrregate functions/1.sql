CREATE TABLE IF NOT EXISTS zoo_animal (
    ANIMAL_ID  INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    SPECIES TEXT NOT NULL,
    AGE_YEARS INTEGER NOT NULL,
    WEIGHT_KG REAL NOT NULL
);

INSERT INTO Zoo_ANIMAL VALUES (1, 'Lion',  'Big cat', 5, 190.0);
INSERT INTO Zoo_ANIMAL VALUES (2, 'Tiger',  'Big cat', 3, 220.0);
INSERT INTO Zoo_ANIMAL VALUES (3, 'Elephant',  'Pachyderm', 12, 4500.0);
INSERT INTO Zoo_ANIMAL VALUES (4, 'Giraffe',  'Ungulate', 7, 800.0);
INSERT INTO Zoo_ANIMAL VALUES (5, 'Penguin',  'Bird', 2, 5.0);
INSERT INTO Zoo_ANIMAL VALUES (6, 'Panda',  'Bear', 6, 95.0);
INSERT INTO Zoo_ANIMAL VALUES (7, 'Cheetah',  'Big cat', 4, 55.0);
INSERT INTO Zoo_ANIMAL VALUES (8, 'Rhino',  'Pachyderm', 9, 2300.0);

SELECT * FROM zoo_animal;

SELECT SPECIES FROM zoo_animal;
SELECT DISTINCT species FROM zoo_animal;
SELECT COUNT(DISTINCT species) AS unique_species FROM zoo_animal;
SELECT COUNT(DISTINCT animal_id) AS older_than_5 FROM zoo_animal WHERE age_years > 5;
SELECT SUM(weight_kg) AS total_weight_kg FROM zoo_animal;
SELECT AVG(age_years) AS avg_age_years FROM zoo_animal;

SELECT 
COUNT(ANIMAL_ID) AS total_animals,
COUNT(DISTINCT SPECIES) AS unique_species,
SUM(weight_kg) AS total_weight_kg,
AVG(age_years) AS avg_age_years,
FROM zoo_animal;