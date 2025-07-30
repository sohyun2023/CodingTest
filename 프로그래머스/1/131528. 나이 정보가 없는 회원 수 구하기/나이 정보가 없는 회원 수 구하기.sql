-- 코드를 입력하세요
SELECT count(user_id) from user_info
group by age
having age is null;