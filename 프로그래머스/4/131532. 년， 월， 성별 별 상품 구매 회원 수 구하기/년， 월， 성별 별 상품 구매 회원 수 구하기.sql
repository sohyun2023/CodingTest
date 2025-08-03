-- 코드를 입력하세요
SELECT year(o.sales_date) as year, month(o.sales_date) as month, i.gender , count(distinct o.user_id) as users
from online_sale as o
join user_info as i
on o.user_id = i.user_id
where i.gender=0 or i.gender=1
group by year(o.sales_date), month(o.sales_date), i.gender
order by year,month,gender
