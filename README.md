
# Athletic Sales Analysis Project

## Project Overview
This project delves into analyzing sales data from a fictional e-commerce company specializing in athletic wear. The primary goal is to extract insights about sales trends across different U.S. cities over two years, pinpoint the retailers with the highest sales, and identify the most lucrative days and weeks for women's athletic footwear sales.

## Challenge Instructions

### Data Preparation and Cleaning
- **Data Importation**: CSV files for the years 2020 and 2021 are imported and read into Pandas DataFrames.
- **Dataframe Merging**: Ensuring uniform column names and data types, the DataFrames are merged and indexed correctly.
- **Data Cleaning**: Null values are addressed, and the "invoice_date" column is converted to a datetime data type for accurate time series analysis.

### Sales Analysis
- **Regional Sales Analysis**: Identifying regions with the highest product sales and revenue generation.
- **Retailer Analysis**: Determining the top retailers based on total sales and sales of women's athletic footwear.
- **Temporal Analysis**: Pinpointing the day and week with the highest sales for women's athletic footwear to optimize marketing and stock strategies.

## Getting Started

### Prerequisites
- Python 3.x
- Pandas library
- Jupyter Notebook or JupyterLab

### Running the Analysis
1. **Clone the Project Repository**
   ```bash
   git clone https://github.com/CREAITIVE-THINKING/athletic_sales_analysis.git
   ```
2. **Navigate to the Project Directory**
   ```bash
   cd athletic_sales_analysis
   ```
3. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook athletic_sales_analysis_starter_code.ipynb
   ```
   OR
   ```bash
   jupyter lab athletic_sales_analysis_starter_code.ipynb
   ```

Follow the instructions in the notebook to execute the analysis.

## Contributing
Contributions, improvements, and bug fixes are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.
