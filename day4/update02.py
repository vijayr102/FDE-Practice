import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

with psycopg.connect(os.getenv("CONN")) as conn:
    with conn.cursor() as cur:
        cur.execute("UPDATE transactions SET amount = 400 WHERE transaction_id = 'T001' returning *")
        updated_row = cur.fetchone()
        print(updated_row)
        conn.commit()
