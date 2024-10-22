# Steps to Create a Star Schema in SQL Server Management Studio
![StarSchema](https://github.com/user-attachments/assets/3f05aeff-e96e-4646-9750-080a6d45df65)

## Open SQL Server Management Studio (SSMS)
- Launch SSMS and connect to your SQL Server instance.

## Create a New Database
1. Right-click on the **Databases** node in Object Explorer.
2. Select **New Database**.
3. Enter a name for your database and click **OK**.

## Create Fact and Dimension Tables
1. Right-click on your newly created database.
2. Select **New Table** to create a new table. This will be your **Fact Table**.
   - Define the columns for your fact table (e.g., `SalesAmount`, `Quantity`, `DateKey`, `ProductKey`).
   - Save the table with an appropriate name (e.g., `SalesFact`).
3. Repeat the process to create your **Dimension Tables** (e.g., `DateDimension`, `ProductDimension`, `CustomerDimension`).
   - Each dimension table should have a primary key that links to the fact table (e.g., `DateKey`, `ProductKey`).

## Set Primary Keys
- For each dimension table, right-click on the column that you want to set as the primary key.
- Select **Set Primary Key**.
- This will ensure that the dimension keys are unique.

## Create Relationships
1. After creating your tables, go to the **Database Diagram**.
2. Right-click on the database in Object Explorer and select **New Database Diagram**.
3. Add your fact and dimension tables to the diagram.
4. Drag and drop the primary key from each dimension table to the corresponding foreign key in the fact table to create relationships.
   - This visually represents the star schema structure.

## Save the Database Diagram
- Save the diagram with an appropriate name for future reference.

## Example Structure of Star Schema

### Fact Table: SalesFact
- **SalesID** (Primary Key)
- **DateKey** (Foreign Key)
- **ProductKey** (Foreign Key)
- **CustomerKey** (Foreign Key)
- **SalesAmount**
- **Quantity**

### Dimension Tables:
- **DateDimension**
  - **DateKey** (Primary Key)
  - **Date**
  - **Month**
  - **Year**

- **ProductDimension**
  - **ProductKey** (Primary Key)
  - **ProductName**
  - **Category**

- **CustomerDimension**
  - **CustomerKey** (Primary Key)
  - **CustomerName**
  - **Region**

## Final Steps

### Review the Structure
- Ensure that your fact and dimension tables are correctly linked and that relationships are accurately defined.

### Use the Schema
- You can now use your star schema for data analysis, reporting, and other BI tasks.

---
# Creating a Database Diagram in SQL Server Management Studio (SSMS)

## Steps to Create a Database Diagram

1. **Open Database Diagram:**
   - Right-click on your database in SSMS.
   - Select **New Database Diagram**.

2. **Add Tables to the Diagram:**
   - In the dialog box, select the tables you want to include (e.g., fact and dimension tables).
   - Click **Add** to include them in the diagram workspace.

3. **Arrange the Tables:**
   - Drag and drop tables in the diagram to arrange them for clarity.

4. **Create Relationships:**
   - Drag the primary key from a dimension table to the corresponding foreign key in the fact table.
   - A line will appear, indicating the relationship.

5. **Save the Diagram:**
   - Save your diagram by clicking the **Save** icon or going to **File > Save**.
     
## Important Notes
- **No Specific File Needed:** The diagram is created directly in SSMS.
- **Permissions Required:** Ensure you have the necessary permissions to create diagrams.
