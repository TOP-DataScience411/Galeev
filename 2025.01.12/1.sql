-- 1. Вывести средний оклад (salary) всех сотрудников

select avg(salary) 
  from doctors;
  
-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего (взять явное значение из результата предыдущего запроса)

select avg(premium) 
  from doctors 
 where salary + premium > 55337.355857142857; 

 -- 3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника — в MySQL используйте функцию datediff(), в PostgreSQL используйте вычитание с помощью оператора -
 
  select avg(end_date - start_date) as avg_vac 
    from vacations 
group by doctor_id 
order by avg_vac asc;

-- 4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями

  select min(extract(year from "start_date")) as min_year,       
         max(extract(year from "start_date")) as max_year
    from vacations 
group by doctor_id 
order by 
        max(extract(year from "start_date")) 
	  - min(extract(year from "start_date")) asc;
	  
	  
-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений

  select sum(amount) 
    from donations 
group by dep_id 
order by dep_id;

-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов

  select sum(amount)
    from donations
group by extract(year from "date"), sponsor_id
order by sponsor_id, extract(year from "date") asc;