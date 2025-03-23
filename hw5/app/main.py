from fastapi import FastAPI

import psycopg2
import os

app = FastAPI()

def get_db_connection():
    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        database=os.getenv("POSTGRES_DB", "testdb"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password")
    )
    return connection

@app.get("/records")
async def get_records():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table;")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"records": records}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
