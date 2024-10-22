SELECT Prod_name ,Total_sales ,day
FROM ((Fact_sales

INNER JOIN Product_dw
ON Fact_sales.prod_id =Product_dw.prod_id) JOIN Time_dw
ON Fact_sales.time_id =Time_dw.time_id)