-- List Glam rock bands ranked by lifespan up to 2024
SELECT
    band_name,
    IFNULL(2024 - formed, 0) - IFNULL(split, 0) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;