-- Final assignment was made with Report Builder by mode.com, using public database. 
-- Postgre sql

--We are running an experiment at an item-level, which means all users who visit will see the same page, but the layout of different item pages may differ.
--Compare this table to the assignment events we captured for user_level_testing.
--Does this table have everything you need to compute metrics like 30-day view-binary?

SELECT 
  * 
FROM 
  dsv1069.final_assignments_qa;
  
-- I also need date and time of the assignment



--Reformat the final_assignments_qa to look like the final_assignments table, filling in any missing values with a placeholder of the appropriate data type.

-- SELECT 
--   * 
-- FROM 
--   dsv1069.final_assignments

-- item_id, test_assignment, test_number, test_start_date

SELECT item_id,
       test_a AS test_assignment,
       'item_test_a' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa
UNION ALL
SELECT item_id,
       test_b AS test_assignment,
       'item_test_b' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa
UNION ALL
SELECT item_id,
       test_c AS test_assignment,
       'item_test_c' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa
UNION ALL
SELECT item_id,
       test_d AS test_assignment,
       'item_test_d' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa
UNION ALL
SELECT item_id,
       test_e AS test_assignment,
       'item_test_e' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa
UNION ALL
SELECT item_id,
       test_f AS test_assignment,
       'item_test_f' AS test_number,
       CAST('2020-01-01' AS date) AS test_start_date
FROM dsv1069.final_assignments_qa;

