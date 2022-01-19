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

-- Use this table to 
-- compute order_binary for the 30 day window after the test_start_date
-- for the test named item_test_2

-- 
SELECT test_assignment,
       test_number,
       COUNT(DISTINCT item) AS number_of_items,
       SUM(order_binary_30d) AS ordered_items_30days
FROM
  (SELECT final_assignments.item_id AS item,
          test_assignment,
          test_number,
          test_start_date,
          MAX((CASE
                   WHEN date(created_at) - date(test_start_date) BETWEEN 0 AND 30 THEN 1
                   ELSE 0
               END)) AS order_binary_30d
   FROM dsv1069.final_assignments
   LEFT JOIN dsv1069.orders
     ON final_assignments.item_id = orders.item_id
   WHERE test_number = 'item_test_2'
   GROUP BY final_assignments.item_id,
            test_assignment,
            test_number,
            test_start_date) AS order_binary_30d
GROUP BY test_assignment,
         test_number,
         test_start_date;