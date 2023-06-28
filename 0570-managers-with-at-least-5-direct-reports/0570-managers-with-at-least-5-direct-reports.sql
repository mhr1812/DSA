# Write your MySQL query statement below
Select Name from Employee where Id in
(
    Select ManagerId from Employee 
    group by ManagerId having count(*) >= 5
)
    