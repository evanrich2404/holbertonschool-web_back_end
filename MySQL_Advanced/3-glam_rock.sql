-- SQL script to list all bands with "Glam rock" as their main style, ranked by their longevity.

-- Assuming the 'metal_bands' table has already been imported:

WITH Longevity AS (
    SELECT
        band_name AS "band_name",              -- Band name column
        CASE
            WHEN split IS NOT NULL THEN split - formed
            ELSE YEAR(CURRENT_DATE) - formed  -- Using the current year if the band has not split
        END AS "lifespan"                     -- Compute lifespan in years
    FROM
        metal_bands                           -- Source table that has been imported
    WHERE
        main_style = 'Glam rock'              -- Filtering bands with main style as "Glam rock"
)

SELECT
    band_name,
    lifespan
FROM
    Longevity
ORDER BY
    lifespan DESC;                           -- Ordering by lifespan in descending order

-- Notes:
-- 1. This script assumes that the 'metal_bands' table has columns named 'band_name', 'formed', 'split', and 'main_style'.
-- 2. The CASE statement checks if the 'split' value is present; if not, it calculates the lifespan using the current year.
-- 3. The 'WITH' clause is used to create a temporary result set, which is then used in the main query.
