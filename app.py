from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv(""))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name PATIENT and has the following columns - NAME, ROOM, 
    DISEASENAME, DATE_OF_ADMIT \n\nFor example,\n
    Example 1 - How many entries of records are present? 
    The SQL command will be something like this: SELECT COUNT(*) FROM PATIENT ;
    \n
    Example 2 - Tell me all the patients admitted for Data Science class? 
    The SQL command will be something like this: SELECT * FROM PATIENT 
    WHERE CLASS="Data Science"; 
    also, the SQL code should not have ``` in the beginning or end, and SQL word in the output.
    """
]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"hospital.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
