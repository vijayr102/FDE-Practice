import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(os.getenv("CONN")) as conn:
    with conn.cursor() as cur:
        cur.execute("UPDATE transactions SET amount = 300 WHERE transaction_id = 'T001' RETURNING *")
        updated_row = cur.fetchone()
        print(updated_row)
        conn.commit()