import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(os.getenv("CONN")) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM transactions")
        for row in cur.fetchall():
            print(row)