from dotenv import load_dotenv

import streamlit as st
import os

import google.generativeai as genai

from helper import *



load_dotenv()

# configure google api key
genai.configure(api_key=os.getenv("GOOGLE_API-KEY"))

prompt = [
    """
        You are an expert in converting English Questions to SQL query.
        The SQL database is named as STUDENT and has the following columns NAME,
        CLASS, SECTION \n\n Below are the examples: \n\n Example 1: How many entries are present in the table?
        The SQL command will be something like this SELECT COUNT(*) FROM STUDENT; \n
        Example 2: How many students are taking the Computer Science course? The SQL command will be something like
        SELECT * FROM STUDENT WHERE CLASS="Computer Science"; 
        also the SQL code should not have ''' in the beginning or end neither the SQL word in output.
    """
]


# streamlit app
st.set_page_config(page_title="Retrieve SQL Query via Gemini Model")
st.header("Gemini Application to Retrieve SQL Query")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask Question")

if submit:
    db = "student.db"
    response = get_response(prompt, question)
    response = read_sql_query(response, db)
    st.subheader("The response is: ")

    st.markdown("""
                <style>
                .card {
                background-color: #f0f2f6;
                padding: 1rem;
                margin-bottom: 1rem;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                </style>
                """, unsafe_allow_html=True)

    for row in response:
        print(row)
        st.markdown(f"<div class='card'>📝 {row}</div>", unsafe_allow_html=True)