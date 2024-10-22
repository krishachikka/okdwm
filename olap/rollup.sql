Select Time_dw.yr, sum(Total_sales)

From Fact_sales
JOIN Product_dw ON
Fact_sales.prod_id = Product_dw.prod_id
JOIN Time_dw ON Fact_sales.time_id= time_dw.time_id
Group by time_dw.yr;