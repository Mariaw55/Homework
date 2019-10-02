-- Drop Tables if Existing

DROP TABLE IF EXISTS department_employee;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS salaries;
DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;

CREATE TABLE Departments (
    dept_no varchar(10)   NOT NULL,
    dept_name varchar(55)   NOT NULL,
    CONSTRAINT pk_Departments PRIMARY KEY (
        dept_no
     )
);

CREATE TABLE Department_Employee (
    emp_no int NOT NULL,
    dept_no varchar(10) NOT NULL,
    from_date date NOT NULL,
    to_date date NOT NULL,
    CONSTRAINT pk_Department_Employee PRIMARY KEY (
        emp_no, dept_no
     )
);


CREATE TABLE Dept_Manager (
    dept_no varchar(10)    NOT NULL,
    emp_no int   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
    CONSTRAINT pk_Dept_Manager PRIMARY KEY (
        dept_no, emp_no
     )
);

CREATE TABLE Employees (
    emp_no int   NOT NULL,
    birth_date date   NOT NULL,
    first_name varchar(100)   NOT NULL,
    last_name varchar(100)   NOT NULL,
    gender varchar(1)   NOT NULL,
    hire_date date   NOT NULL,
    CONSTRAINT pk_Employees PRIMARY KEY (
        emp_no
     )
);

CREATE TABLE Salaries (
    emp_no int   NOT NULL,
    salary int   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
    CONSTRAINT pk_Salaries PRIMARY KEY (
        emp_no
     )
);

CREATE TABLE Titles (
	id serial,
   emp_no int   NOT NULL,
    title varchar(100)   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
    CONSTRAINT pk_Titles PRIMARY KEY (
        id)
);

ALTER TABLE Department_Employee ADD CONSTRAINT fk_Department_Employee_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Department_Employee ADD CONSTRAINT fk_Department_Employee_dept_no FOREIGN KEY(dept_no)
REFERENCES Departments (dept_no);

ALTER TABLE Dept_Manager ADD CONSTRAINT fk_Dept_Manager_dept_no FOREIGN KEY(dept_no)
REFERENCES Departments (dept_no);

ALTER TABLE Dept_Manager ADD CONSTRAINT fk_Dept_Manager_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Salaries ADD CONSTRAINT fk_Salaries_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

ALTER TABLE Titles ADD CONSTRAINT fk_Titles_emp_no FOREIGN KEY(emp_no)
REFERENCES Employees (emp_no);

-- Query * FROM Each Table Confirming Data
SELECT * FROM departments;
SELECT * FROM department_employee;
SELECT * FROM dept_manager;
SELECT * FROM employees;
SELECT * FROM salaries;
SELECT * FROM titles;



