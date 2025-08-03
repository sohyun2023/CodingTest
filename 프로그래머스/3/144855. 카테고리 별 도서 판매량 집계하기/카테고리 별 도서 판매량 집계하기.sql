-- 코드를 입력하세요
SELECT category, sum(s.sales)
From book as b
join book_sales as s
on b.book_id = s.book_id
where s.sales_date between '2022-01-01' and '2022-01-31'
group by category
order by category