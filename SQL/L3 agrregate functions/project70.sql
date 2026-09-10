CREATE TABLE marine_observations (
    id INTEGER PRIMARY KEY,
    animal_group VARCHAR(50),
    animal_name VARCHAR(100),
    estimated_weight DECIMAL(10,2),
    depth DECIMAL(10,2)
);

INSERT INTO marine_observations
(id, animal_group, animal_name, estimated_weight, depth)
VALUES
(1, 'Mammals', 'Dolphin', 180.00, 25.00),
(2, 'Mammals', 'Whale', 1200.00, 80.00),
(3, 'Mammals', 'Seal', 90.00, 15.00),
(4, 'Fish', 'Tuna', 45.00, 40.00),
(5, 'Fish', 'Shark', 320.00, 65.00),
(6, 'Fish', 'Manta Ray', 200.00, 30.00),
(7, 'Reptiles', 'Sea Turtle', 110.00, 20.00),
(8, 'Reptiles', 'Sea Snake', 8.00, 35.00),
(9, 'Mammals', 'Dolphin', 175.00, 28.00),
(10, 'Fish', 'Tuna', 50.00, 45.00);

SELECT DISTINCT animal_group
FROM marine_observations;

SELECT COUNT(*) AS total_observations
FROM marine_observations;

SELECT SUM(estimated_weight) AS total_estimated_weight
FROM marine_observations;

SELECT AVG(depth) AS average_depth
FROM marine_observations;

SELECT
COUNT(*) AS total_observations,
SUM(estimated_weight) AS total_estimated_weight,
 AVG(depth) AS average_depth
FROM marine_observations;

SELECT
animal_group,
COUNT(*) AS observation_count,
 SUM(estimated_weight) AS total_estimated_weight,
 AVG(depth) AS average_depth
FROM marine_observations
GROUP BY animal_group;
