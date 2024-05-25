import streamlit as st
import pandas as pd
import sqlite3

# Connect to database
conn = sqlite3.connect("../data/quotes.db")

# Load data into a pandas dataframe
df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

# Close connection
conn.close()

# Main page titles, headers and columns
st.set_page_config(layout="wide")
st.title("Price Monitoring - Mercado Livre")
st.subheader("Main System KPIs")
col1, col2, col3 = st.columns(3)

# KPI 1: Total number of items
total_items = df.shape[0]
col1.metric(label="Total Number of Items", value=total_items)

# KPI 2: Number of Single Brands
unique_brands = df['brand'].nunique()
col2.metric(label="Number of Single Brands", value=unique_brands)

# KPI 3: New Average Price 
average_new_price = df['new_price'].mean()
col3.metric(label="New Average Price (R$)", value=f"{average_new_price:.2f}")

# Most found brands
st.subheader('Most Found Brands')
col1, col2 = st.columns([6, 2])
top_10_pages_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Average price per brand
st.subheader('Average Price per Brand')
col1, col2 = st.columns([6, 2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Average satisfaction(rating) by brand
st.subheader('Average Rating by Brand')
col1, col2 = st.columns([6, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)