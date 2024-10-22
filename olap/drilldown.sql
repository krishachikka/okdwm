Select time_dw.qt,sum(total_sales)
From Fact_sales JOIN Product_dw
ON Fact_sales.Prod_id = Product_dw.Prod_id
JOIN Time_dw ON fact_sales.time_id= time_dw.time_id

Group by time_dw.qt;