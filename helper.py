import sqlite3

import google.generativeai as genai




def get_response(prompt, question):
    
    # model = genai.GenerativeModel("gemini-pro")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text


def read_sql_query(sql, db):

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows
