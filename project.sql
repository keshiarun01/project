use emp;

#Get all the project which belongs to department 110.(Simple Query)
select project_id from project where department_id='110';


#Count the number of non-monetary rewards in the company.(Aggregate)
SELECT nonmonetary_desc, COUNT(*) AS reward_count
FROM emp.nonmonetary
GROUP BY nonmonetary_desc;


#Retrieve the names of employees who have a PhD qualification(Nested Query)
SELECT employee_id, employee_name
FROM EMPLOYEE
WHERE employee_id IN (SELECT employee_id FROM QUALIFIED WHERE
qualification_id IN (SELECT qualification_id FROM PhD));


#Retrieve the details of employees and their leave taken.(Inner Join)
SELECT e.employee_id, e.employee_name, l.leave_id, l.start_date, l.end_date, l.reason
FROM EMPLOYEE e
JOIN LEAVE_TAKEN l ON e.employee_id = l.employee_id
WHERE l.start_date BETWEEN '11/14/2022' AND '11/18/2022';


#Retrieve the details of employees and their qualifications(Left Outer Join)
SELECT e.employee_id, e.employee_name, q.qualification_id
FROM EMPLOYEE e
LEFT JOIN QUALIFIED q ON e.employee_id = q.employee_id;


#Retrieve the name, employee_id, reward type, score of employee whose score is greater than 4.(Corelated query Using Exists)
SELECT e.employee_id, e.employee_name, r.reward_type, p.score
FROM EMPLOYEE e
JOIN PERFORMANCE p ON e.performance_id = p.performance_id
JOIN REWARD r ON e.employee_id = r.employee_id
WHERE EXISTS (
     SELECT 1
     FROM PERFORMANCE p
     WHERE p.performance_id = e.performance_id 
     AND p.score >= 4
)
ORDER BY p.score DESC;


-- Names of employees who has ph.D. degree and has recieved a Non-monetary reward(Set operation, Union)
SELECT e.employee_name, 'PhD' AS qualification_type, NULL AS reward_type
FROM EMPLOYEE e
JOIN qualified q ON q.employee_id = e.employee_id
JOIN qualification q2 ON q2.qualification_id=q.qualification_id
WHERE q2.qualification_type = 'ph.d.'
UNION
SELECT e.employee_name, NULL AS qualification_type, r.reward_type AS reward_type
FROM EMPLOYEE e
JOIN works_on w ON w.employee_id = e.employee_id
JOIN reward r ON r.employee_id=e.employee_id
WHERE r.reward_type='Non-Monetary';


-- Subquery in the SELECT clause to retrieve the number of qualification for each employee
-- Subquery in the FROM clause to calculate the Maximum performance score
SELECT
  e.employee_id,
  e.employee_name,
  (
    SELECT COUNT(q.qualification_id)
    FROM QUALIFIED q
    WHERE q.employee_id = e.employee_id
  ) AS qualification_count,
  (
    SELECT MAX(p.score)
    FROM PERFORMANCE p
    WHERE p.performance_id = e.performance_id
  ) AS max_performance_score
FROM
  EMPLOYEE e;









