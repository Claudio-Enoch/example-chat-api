import time

import psycopg2


def check_postgres_connection(url: str, tries: int = 10, delay: int = 1):
    print("Attempting to connect to Postgres...")
    for _ in range(tries):
        try:
            conn = psycopg2.connect(url)
            conn.close()
            print("Connection to Postgres successful")
            return
        except psycopg2.OperationalError:
            time.sleep(delay)
    raise psycopg2.OperationalError("Could not connect to Postgres")
