/*1 -незрозуміло: чи перерахувати вакансії (список) чи розрахувати кількість вакансій - тому 2 варіанти*/
SELECT DISTINCT JOB_ID
FROM employees
;
SELECT COUNT(DISTINCT JOB_ID) number_of_job_vacation
FROM employees
;

 /*2*/
SELECT round(avg(SALARY),2) avg_salary , count(DISTINCT EMPLOYEE_ID) number_empl
FROM employees
WHERE DEPARTMENT_ID = 90
;

/*3*/
SELECT JOB_ID, count(DISTINCT EMPLOYEE_ID) number_empl
FROM employees
GROUP BY JOB_ID
ORDER BY 2 DESC
;

/*4 - cowokers in base of department - теж не дуже зрозуміле питання щодо співробітників.
чи потрібні дублі - той же співробітник в 1й колонці і останній.
 Оскільки вирішила, що працівник не може бути сам собі співробітником, то такі кейси убрала.
 як ні - убрати в джоїні все після связки*/
SELECT  a.FIRST_NAME as empl_name, a.LAST_NAME as empl_surname, a.DEPARTMENT_ID as  department,
b.FIRST_NAME as coworker_name, b.LAST_NAME as coworker_surname
FROM employees a LEFT JOIN employees b on a.DEPARTMENT_ID = b.DEPARTMENT_ID and a.FIRST_NAME <> b.FIRST_NAME and  a.LAST_NAME <> b.LAST_NAME
;

/*5*/
SELECT DISTINCT a.FIRST_NAME as empl_name, a.LAST_NAME empl_surname, a.JOB_ID job, a.DEPARTMENT_ID department,
b.FIRST_NAME coworker_name, b.LAST_NAME coworker_surname
FROM employees a left join employees b on a.DEPARTMENT_ID = b.DEPARTMENT_ID and a.FIRST_NAME <> b.FIRST_NAME and  a.LAST_NAME <> b.LAST_NAME
					left join departments d on a.DEPARTMENT_ID = d.DEPARTMENT_ID
						left join locations l on d.LOCATION_ID = l.LOCATION_ID
WHERE city = 'London'
;