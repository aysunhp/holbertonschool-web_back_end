<<<<<<< HEAD
-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
=======
-- Rank country origins of bands by number of fans
SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
>>>>>>> d85190c55f486235c3b2dc1887cede9ba7ee4e1c
