-- 코드를 작성해주세요
select i.id, n.fish_name, i.length
from fish_info as i
join (select fish_type , max(length) as max_length 
 from fish_info group by fish_type) as m
on i.fish_type = m.fish_type and i.length=m.max_length
join fish_name_info as n
on i.fish_type = n.fish_type
order by i.id

