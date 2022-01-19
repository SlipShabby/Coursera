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

-- Use this table to 
-- compute view_binary for the 30 day window after the test_start_date
-- for the test named item_test_2

SELECT 
  test_assignment,
  COUNT(DISTINCT item_id) AS items,
  SUM(view_binary_30days) AS viewed_items_30_days,
  SUM(views) as views,
  SUM(views)/COUNT(item_id) AS avg_views_per_item,
  CAST(100*SUM(view_binary_30days)/COUNT(item_id) AS FLOAT) AS views_percent
  
FROM 
(
SELECT 
  assignments.item_id,
  assignments.test_assignment,
  MAX(CASE WHEN views.event_time > assignments.test_start_date
    THEN 1
    ELSE 0
    END) AS view_binary_30days,
  COUNT(views.event_id) as views
FROM 
  dsv1069.final_assignments AS assignments
  
  LEFT OUTER JOIN 
  (
    SELECT 
      event_time,
      event_id,
      CAST(parameter_value AS INT) AS item_id
    FROM
      dsv1069.events
    WHERE 
      event_name = 'view_item'
    AND
      parameter_name = 'item_id'
  ) views
  ON 
    assignments.item_id = views.item_id 
  AND
    views.event_time >= assignments.test_start_date
  AND
    DATE_PART('day', views.event_time - assignments.test_start_date) <= 30
  WHERE 
    assignments.test_number = 'item_test_2'
  GROUP BY 
    assignments.item_id,
    assignments.test_assignment 
) item_level
GROUP BY
  test_assignment;

--Use the https://thumbtack.github.io/abba/demo/abba.html to compute the lifts in metrics and the p-values for the binary metrics ( 30 day order binary and 30 day view binary) using a interval 95% confidence. 

-- 30 day order binary: 
-- lift: -10% – 12%, p.value 0.86. nonsignificant change. 

-- 30 day view binary:
-- lift: -2.1% – 5.9%, p-value 0.36. 	nonsignificant change. 

-- for item_test_2 there is no difference in views/orders  between control and treatment groups


  
  