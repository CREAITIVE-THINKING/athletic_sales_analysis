#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries and Dependencies
import pandas as pd


# ### 1. Combine and Clean the Data
# #### Import CSVs

# In[29]:


# Load the CSV files into DataFrames
sales_2020 = pd.read_csv('/Users/mattobrien/Documents/AI_BOOTCAMP/M5_Starter_Code/Resources/athletic_sales_2020.csv')
sales_2021 = pd.read_csv('//Users/mattobrien/Documents/AI_BOOTCAMP/M5_Starter_Code/Resources/athletic_sales_2021.csv')

# Display the first few rows of the dataframes to understand their structure
sales_2020.head()


# In[30]:


sales_2021.head()


# In[31]:


# Display the 2020 sales DataFrame
sales_2020


# In[32]:


# Display the 2021 sales DataFrame
sales_2021


# #### Check the data types of each DataFrame

# In[33]:


# Check the 2020 sales data types.
data_types_2020 = sales_2020.dtypes
data_types_2020


# In[34]:


# Check the 2021 sales data types.
data_types_2021 = sales_2021.dtypes
data_types_2021


# #### Combine the sales data by rows.

# In[12]:


# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.
combined_sales = pd.concat([sales_2020, sales_2021], ignore_index=True)
combined_sales


# In[45]:


# Check if any values are null.
null_values = combined_sales.isnull().sum()
null_values


# In[14]:


# Check the data type of each column
data_types_before = combined_sales.dtypes
data_types_before


# In[44]:


# Convert the "invoice_date" to a datetime datatype
combined_sales['invoice_date'] = pd.to_datetime(combined_sales['invoice_date'])
combined_sales['invoice_date']


# In[40]:


# Confirm that the "invoice_date" data type has been changed.
data_types_after = combined_sales.dtypes
data_types_after


# ### 2. Determine which Region Sold the Most Products

# #### Using `groupby`

# In[17]:


# Show the number products sold for region, state, and city.

region_product_sales = combined_sales.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index()

# Rename the sum to "Total_Products_Sold".

region_product_sales.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)

# Show the top 5 results.

top_five_regions_by_products = region_product_sales.sort_values('Total_Products_Sold', ascending=False).head(5)
top_five_regions_by_products


# #### Using `pivot_table`

# In[18]:


# Show the number products sold for region, state, and city.
# Rename the "units_sold" column to "Total_Products_Sold"

pivot_table_products_sold = combined_sales.pivot_table(
    values='units_sold', 
    index=['region', 'state', 'city'], 
    aggfunc='sum'
).rename(columns={'units_sold': 'Total_Products_Sold'}).reset_index()

# Show the top 5 results.

top_five_regions_pivot = pivot_table_products_sold.sort_values('Total_Products_Sold', ascending=False).head(5)

top_five_regions_pivot


# In[52]:


# EXPERIMENTING Show the number products sold for region, state, and city.
# Rename the "units_sold" column to "Total_Products_Sold"

#pivot_table_products_sold = combined_sales.pivot_table(
    values='units_sold', 
    index=['region'],
    columns=['state', 'city'],
    aggfunc='sum'
)#.rename(columns={'units_sold': 'Total_Products_Sold'}).reset_index()

# Show the top 5 results.

#top_five_regions_pivot = pivot_table_products_sold.sort_values('Total_Products_Sold', ascending=False).head(5)

#top_five_regions_pivot
#pivot_table_products_sold


# ### 3. Determine which Region had the Most Sales

# #### Using `groupby`

# In[19]:


# Show the total sales for the products sold for each region, state, and city.
region_total_sales = combined_sales.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index()

# Rename the "total_sales" column to "Total Sales"
region_total_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)


# Show the top 5 results.
top_five_regions_by_total_sales = region_total_sales.sort_values('Total Sales', ascending=False).head(5)
top_five_regions_by_total_sales


# #### Using `pivot_table`

# In[20]:


# Show the total sales for the products sold for each region, state, and city.
pivot_table_total_sales = combined_sales.pivot_table(
    values='total_sales', 
    index=['region', 'state', 'city'], 
    aggfunc='sum'
).rename(columns={'total_sales': 'Total Sales'}).reset_index()

# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.
top_five_regions_total_sales_pivot = pivot_table_total_sales.sort_values('Total Sales', ascending=False).head(5)
top_five_regions_total_sales_pivot


# ### 4. Determine which Retailer had the Most Sales

# #### Using `groupby`

# In[21]:


# Show the total sales for the products sold for each retailer, region, state, and city.
retailer_region_total_sales = combined_sales.groupby(['retailer', 'region', 'state', 'city'])['total_sales'].sum().reset_index()

# Rename the "total_sales" column to "Total Sales"
retailer_region_total_sales.rename(columns={'total_sales': 'Total Sales'}, inplace=True)


# Show the top 5 results.
top_five_retailers_by_total_sales = retailer_region_total_sales.sort_values('Total Sales', ascending=False).head(5)
top_five_retailers_by_total_sales


# #### Using `pivot_table`

# In[22]:


# Show the total sales for the products sold for each retailer, region, state, and city.
pivot_table_retailer_total_sales = combined_sales.pivot_table(
    values='total_sales',
    index=['retailer', 'region', 'state', 'city'],
    aggfunc='sum'
).rename(columns={'total_sales': 'Total Sales'}).reset_index()


# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.
top_five_retailers_total_sales_pivot = pivot_table_retailer_total_sales.sort_values('Total Sales', ascending=False).head(5)
top_five_retailers_total_sales_pivot


# ### 5. Determine which Retailer Sold the Most Women's Athletic Footwear

# In[23]:


# Filter the sales data to get the women's athletic footwear sales data.
womens_footwear_sales = combined_sales[combined_sales['product'] == "Women's Athletic Footwear"]
womens_footwear_sales.head()


# #### Using `groupby`

# In[24]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
womens_footwear_units_sold = womens_footwear_sales.groupby(['retailer', 'region', 'state', 'city'])['units_sold'].sum().reset_index()


# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womens_footwear_units_sold.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}, inplace=True)


# Show the top 5 results.
top_five_retailers_womens_footwear = womens_footwear_units_sold.sort_values('Womens_Footwear_Units_Sold', ascending=False).head(5)
top_five_retailers_womens_footwear


# #### Using `pivot_table`

# In[25]:


# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
pivot_table_womens_footwear = womens_footwear_sales.pivot_table(
    values='units_sold',
    index=['retailer', 'region', 'state', 'city'],
    aggfunc='sum'
).rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'}).reset_index()

# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
top_five_retailers_womens_footwear_pivot = pivot_table_womens_footwear.sort_values('Womens_Footwear_Units_Sold', ascending=False).head(5)

# Show the top 5 results.
top_five_retailers_womens_footwear_pivot


# ### 5. Determine the Day with the Most Women's Athletic Footwear Sales

# In[26]:


# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.
pivot_table_invoice_date = womens_footwear_sales.pivot_table(
    values='total_sales',
    index='invoice_date',
    aggfunc='sum'
).rename(columns={'total_sales': 'Total Sales'})

# Optional: Rename the "total_sales" column to "Total Sales"


# Show the table.
pivot_table_invoice_date


# In[53]:


# Resample the pivot table into daily bins, and get the total sales for each day.
daily_total_sales = pivot_table_invoice_date.resample('D').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".
daily_total_sales_sorted = daily_total_sales.sort_values('Total Sales', ascending=True)
daily_total_sales_sorted


# ### 6.  Determine the Week with the Most Women's Athletic Footwear Sales

# In[28]:


# Resample the pivot table into weekly bins, and get the total sales for each week.
# https://calmcode.io/pandas-datetime/resample.html

weekly_total_sales = pivot_table_invoice_date.resample('W').sum()


# Sort the resampled pivot table in ascending order on "Total Sales".
weekly_total_sales_sorted = weekly_total_sales.sort_values('Total Sales', ascending=True)
weekly_total_sales_sorted


# In[ ]:




