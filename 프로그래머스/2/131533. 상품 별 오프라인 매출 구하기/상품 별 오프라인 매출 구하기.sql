-- 코드를 입력하세요
SELECT p.product_code, sum(p.price*o.sales_amount) as sales
from offline_sale as o
join product as p
on o.product_id = p.product_id
group by p.product_code
order by sales desc, product_code
