-- Query * FROM Each Table Confirming Data
SELECT * FROM departments;
SELECT * FROM department_employee;
SELECT * FROM dept_manager;
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT * FROM titles;

-- List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM employees 
inner JOIN salaries on
employees.emp_no=salaries.emp_no;

-- List employees who were hired in 1986.
select employees.emp_no, employees.last_name, employees.first_name
from employees
where hire_date BETWEEN '1986-01-01' AND '1987-01-01';

-- List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, 
employees.first_name, dept_manager.from_date, dept_manager.to_date
FROM departments
JOIN dept_manager
ON departments.dept_no = dept_manager.dept_no
JOIN employees
ON dept_manager.emp_no = employees.emp_no;

-- List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT department_employee.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM departments
INNER JOIN department_employee
ON department_employee.dept_no = departments.dept_no
INNER JOIN employees
ON department_employee.emp_no=employees.emp_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."

SELECT first_name, last_name
FROM employees
WHERE first_name = 'Hercules' AND
last_name LIKE 'B%';


-- List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT employees.emp_no as "Employee No." , employees.last_name as "Last Name", employees.first_name as "First Name", departments.dept_name as "Dept. Name"
from employees
inner join department_employee on employees.emp_no=department_employee.emp_no
inner join departments
on department_employee.dept_no=departments.dept_no
WHERE departments.dept_name='Sales';

-- List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT employees.emp_no as "Employee No." , employees.last_name as "Last Name", employees.first_name as "First Name", departments.dept_name as "Dept. Name"
from employees
inner join department_employee on employees.emp_no=department_employee.emp_no
inner join departments
on department_employee.dept_no=departments.dept_no
WHERE departments.dept_name='Sales' 
OR departments.dept_name='Development';

-- In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) AS "Employee Count"
FROM employees
GROUP BY last_name
ORDER BY "Employee Count" DESC;



