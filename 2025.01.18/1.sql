-- 1. Вывести названия стран и названия сопоставленных им столиц

select c.name as country, 
       city.name as city 
from country as c 
join city 
on c.capital = id;

-- 2. Сравнить по регионам сумму населения стран и сумму населения городов

  select region, 
         sum(c.population), 
	     sum(city.population) 
    from country as c
    join city 
	  on c.code = countrycode 
group by region 
order by region;

-- 3. Вывести десять языков, на которых разговаривает больше всего людей

  select sum(population * percentage / 100) as total_speakers,
         language
    from country as c 
    join countrylanguage as cl 
      on code = countrycode 
group by language
order by total_speakers desc 
   limit 10;
   
-- 4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска

  select s.name, 
         sum(end_date - start_date) as days
    from specializations as s
    join doctors_specs as d	
	  on s.id = d.spec_id
    join vacations as v 
	  on v.doctor_id = d.doctor_id
group by s.name 
order by days asc;

-- 5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы

   select round(sum(amount) / count(name)) as amount_of_funds 
     from wards as w 
left join donations as d on w.dep_id = d.dep_id 
 group by w.dep_id 
 order by amount_of_funds desc;
       