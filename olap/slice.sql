SELECT Prod_name ,Total_sales
FROM Fact_sales
INNER JOIN Product_dw
ON Fact_sales.prod_id=Product_dw.prod_id