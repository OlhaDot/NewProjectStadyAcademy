/* 1. sort by name - asc*/
select *
from employees
ORDER BY last_name, first_name
;


/*2. name and tax*/
select first_name, last_name, sum(salary) empl_salary, sum(salary)*0.15 as empl_tax
from employees
group by first_name, last_name
;

/*3. total salary*/
select  sum(salary) total_salary
from employees
;

/*4. min and max salary*/
select  min(salary) min_salary, max(salary) max_salary
from employees
;

/*5. min and max salary*/
select  max(salary) max_salary, min(salary) min_salary
from employees
;

/*6. avg sal and number of cln */
select  avg(salary) avg_salary, count(EMPLOYEE_ID) number_of_cln
from employees
;
