-- SQL script to rank country origins of bands based on the number of fans.

-- Assuming the 'metal_bands' table has already been imported:

SELECT
    origin AS "origin",           -- Rename the column as required
    SUM(fans) AS "nb_fans"        -- Aggregate the number of fans by country of origin and rename the column
FROM
    metal_bands                  -- Source table that has been imported
GROUP BY
    origin                       -- Grouping by country of origin
ORDER BY
    nb_fans DESC;                -- Ordering by the number of fans in descending order

-- Notes:
-- 1. This script assumes that the 'metal_bands' table has columns named 'origin' and 'fans'.
-- 2. The 'GROUP BY' clause groups the data by country of origin.
-- 3. The 'SUM' function aggregates the number of fans for each country.
-- 4. The 'ORDER BY' clause ensures the results are sorted in descending order of the number of fans.
