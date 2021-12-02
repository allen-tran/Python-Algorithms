/*
https://leetcode.com/problems/second-highest-salary/
*/

SELECT MAX(SALARY) AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee);