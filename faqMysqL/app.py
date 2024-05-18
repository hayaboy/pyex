import streamlit as st
import mysql.connector
from mysql.connector import Error

# MySQL 연결 설정
def create_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="1234",
        database="company_faq"
    )

# FAQ 데이터를 가져오는 함수
def get_faq_data():
    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM faq")
            result = cursor.fetchall()
            return result
    except Error as e:
        st.error(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Streamlit 앱 설정
st.title("기업 FAQ 조회 시스템")

faq_data = get_faq_data()

if faq_data:
    for faq in faq_data:
        st.subheader(faq['question'])
        st.write(faq['answer'])
else:
    st.write("FAQ 데이터를 가져올 수 없습니다.")