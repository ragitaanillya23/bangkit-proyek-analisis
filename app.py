import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Proyek Analisis Data: E-commerce Public Dataset')

    # Pertanyaan
    st.header('Pertanyaan')

    st.write("""
    - Which City has the highest number of customers placing orders?
    - Which City has the highest number of sellers?
    """)

    # Data Wrangling
    st.header('Data Wrangling')

    ## Baca data dari file CSV
    df_product = pd.read_csv('content/products_dataset.csv')
    df_order_item = pd.read_csv('content/order_items_dataset.csv')
    df_category = pd.read_csv('content/product_category_name_translation.csv')
    df_orders = pd.read_csv('content/orders_dataset.csv')
    df_customer = pd.read_csv('content/customers_dataset.csv')
    df_seller = pd.read_csv('content/sellers_dataset.csv')

    ## Menampilkan informasi dataset
    st.subheader('Informasi Dataset Produk:')
    st.write("Jumlah Baris:", df_product.shape[0])
    st.write("Jumlah Kolom:", df_product.shape[1])
    st.write("Tipe Data:")
    st.write(df_product.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_product.isnull().sum())

    st.subheader('Informasi Dataset Order Item:')
    st.write("Jumlah Baris:", df_order_item.shape[0])
    st.write("Jumlah Kolom:", df_order_item.shape[1])
    st.write("Tipe Data:")
    st.write(df_order_item.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_order_item.isnull().sum())

    st.subheader('Informasi Dataset Kategori:')
    st.write("Jumlah Baris:", df_category.shape[0])
    st.write("Jumlah Kolom:", df_category.shape[1])
    st.write("Tipe Data:")
    st.write(df_category.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_category.isnull().sum())

    st.subheader('Informasi Dataset Orders:')
    st.write("Jumlah Baris:", df_orders.shape[0])
    st.write("Jumlah Kolom:", df_orders.shape[1])
    st.write("Tipe Data:")
    st.write(df_orders.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_orders.isnull().sum())

    st.subheader('Informasi Dataset Customer:')
    st.write("Jumlah Baris:", df_customer.shape[0])
    st.write("Jumlah Kolom:", df_customer.shape[1])
    st.write("Tipe Data:")
    st.write(df_customer.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_customer.isnull().sum())

    st.subheader('Informasi Dataset Seller:')
    st.write("Jumlah Baris:", df_seller.shape[0])
    st.write("Jumlah Kolom:", df_seller.shape[1])
    st.write("Tipe Data:")
    st.write(df_seller.dtypes)
    st.write("Jumlah Nilai yang Hilang:")
    st.write(df_seller.isnull().sum())

    # EDA (Exploratory Data Analysis)
    st.header('Exploratory Data Analysis (EDA)')

    ## 1. mengexplore Tabel df_product & df_order_items
    st.subheader('Explore Tabel df_product & df_order_items')
    st.write("Informasi df_product:")
    st.write(df_product.info())
    st.write("Statistik Deskriptif df_product:")
    st.write(df_product.describe())

    st.write("Informasi df_order_item:")
    st.write(df_order_item.info())
    st.write("Statistik Deskriptif df_order_item:")
    st.write(df_order_item.describe())

    ## 2. Mengexplore Tabel df_customer
    st.subheader('Explore Tabel df_customer')
    st.write("Informasi df_customer:")
    st.write(df_customer.info())
    st.write("Statistik Deskriptif df_customer:")
    st.write(df_customer.describe())

    ## 3. mengxplore Tabel df_seller
    st.subheader('Explore Tabel df_seller')
    st.write("Informasi df_seller:")
    st.write(df_seller.info())
    st.write("Statistik Deskriptif df_seller:")
    st.write(df_seller.describe())

    # Visualization

    ## 1. Histogram untuk city that has the highest number of customers placing orders
    st.subheader('city that has the highest number of customers placing orders : ')
    city_customers = df_customer['customer_city'].value_counts().nlargest(5) #menggunakan nlargest(5) utk mendapatkan 5 kota teratas
    color = ['green', 'red', 'red', 'red', 'red']
    plt.figure(figsize=(10,6))
    plt.title('Top 5 Customer City')
    plt.bar(x=city_customers.index, height=city_customers.values, color=color)
    plt.ylabel('The amount of customer orderr')
    plt.xticks(rotation=90)
    st.pyplot(plt)

    ## 2. Histogram untuk city that has the highest number of sellers
    st.subheader('city that has the highest number of sellers : ')
    seller_city = df_seller['seller_city'].value_counts().nlargest(5)
    color = ['blue', 'red', 'red', 'red', 'red']
    plt.figure(figsize=(10,6))
    plt.title('Top 5 Seller City')
    plt.bar(x=seller_city.index, height=seller_city.values, color=color)
    plt.ylabel('The amount of sellers')
    plt.xticks(rotation=90)
    st.pyplot(plt)

    # Konklusi dari Analisis Data
    st.header('Conclusion')

    st.write("""
    Base on the analysis above, we can conclude that:
    - Based on the analysis of customer orders, five cities stand out with high order volumes: Sao Paulo, Rio de Janeiro, Belo Horizonte, Brasília, and Curitiba. This indicates a significant contribution to total customer orders, providing a strong insight into high purchasing activity in these areas.
      Knowing these cities as hubs of high order activity, business strategies can focus on improving services and distribution in these regions. Emphasizing product availability, delivery efficiency, and customer service enhancements in these cities can strategically attract more customers and enhance overall business performance.
    - The presence of large-scale sellers in several cities signifies significant business potential. By focusing on collaboration with sellers in those areas, we can enhance product availability, improve delivery efficiency, and reach out to more customers. These actions will help expand market share and boost business competitiveness.
      Identifying cities with strong seller presence allows us to plan targeted expansion strategies. Strategic collaboration with these sellers will strengthen sales infrastructure, enrich product offerings, and enhance overall business attractiveness and operational efficiency.
    """)

if __name__ == "__main__":
    main()