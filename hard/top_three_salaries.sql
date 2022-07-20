/*************************
* Best runtime: 706 ms
* Title: Top Three Department Salaries
* Question: 185
* URL: https://leetcode.com/problems/department-top-three-salaries/
*************************/
SELECT name AS Department
	,Employee
	,Salary
FROM (
	SELECT emp.departmentId
		,emp.name AS Employee
		,emp.salary AS Salary
	FROM (
		(
			SELECT id
				,name
				,salary
				,departmentId
			FROM employee
			) AS emp LEFT JOIN (
			SELECT min(salary) AS min_salary
				,departmentId
			FROM (
				SELECT salary
					,departmentId
					,row_number() OVER (
						PARTITION BY departmentID ORDER BY salary DESC
						) AS val
				FROM (
					SELECT DISTINCT salary
						,departmentId
					FROM employee
					) AS a
				) AS b
			WHERE val <= 3
			GROUP BY departmentId
			) AS min_salary ON emp.departmentId = min_salary.departmentId
		)
	WHERE emp.salary >= min_salary.min_salary
	) b
LEFT JOIN (
	SELECT id
		,name
	FROM department
	) AS dept ON b.departmentId = dept.id
