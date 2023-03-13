import streamlit as st
import mysql.connector
from mysql.connector import Error


def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Data_Logistik"
        )
        if conn.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(e)

    return conn

def view_data():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Data_Logistik")
    data = cursor.fetchall()

    conn.close()

    return data

def main():
    st.title("Logistics Dashboard")

    data = view_data()
    df = pd.DataFrame(data, columns=["ID", "Nama", "Penyimpanan", "quantity", "SN", "Tanggal", "Admin"])

    st.write("### Logistics Data")
    st.dataframe(df)

if __name__ == "__main__":
    main()

