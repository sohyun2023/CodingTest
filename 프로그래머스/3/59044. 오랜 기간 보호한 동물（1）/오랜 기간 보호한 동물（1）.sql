-- 코드를 입력하세요
SELECT i.name, i.datetime
from animal_ins as i
left join (select animal_id,name, datetime as new_date from animal_outs) as o
on i.animal_id=o.animal_id
where o.new_date is null
order by datetime
limit 3;