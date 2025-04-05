# SQL Query Retriever

## About Project
This project is a Retrieval-Augmented Generation (RAG) based application that allows to ask a question about an existing database via Gemini LLM inserting an input. The system, powered by the Gemini LLM (`gemini-1.5-flash`), processes the question, generates the corresponding query and then the query will be made which retrieves the information desired by the user.

## Features:

- Enter a question about database entries as input.
- Uses Gemini LLM for intelligent query generation
- Simple and user-friendly interface

## Installation & Setup:
1. Clone the Repository
```
git clone https://github.com/milad818/text2sql-llm-application.git
cd askme
```

2. Create Environment (Optional):
You can create and activate an isolate environment to keep dependencies in check.
```
conda create -n text2sql python=3.10 -y
conda activate text2sql
```

3. Install Dependencies
Make sure you have Python installed (>= 3.8). Then, run:

```
pip install -r requirements.txt
```
This installs all required dependencies, including local ones.

4. Run the Application

```
python app.py
```

This starts the application locally. You can then access it via the local host at your terminal after execution. At times, it automatically opens the browser.

Hope you enjoy the experience!

