-- 코드를 작성해주세요
Select m.year, m.maxsize - o.size_of_colony as year_dev, o.id
from ecoli_data as o
join(
        select max(size_of_colony)as maxsize, YEAR(DIFFERENTIATION_DATE) AS YEAR from ecoli_data group by year(DIFFERENTIATION_DATE)) as m
on YEAR(o.DIFFERENTIATION_DATE)	= m.year
order by year, year_dev