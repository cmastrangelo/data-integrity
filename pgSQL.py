import os
import psycopg2
from dotenv import load_dotenv


# Function to establish a database connection
def get_db_connection():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve credentials
    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT")

    # Establish and return a database connection
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


# Example usage
conn = get_db_connection()

cur = conn.cursor()

cur.execute('SELECT * FROM state')
for item in cur.fetchone():
    print(item)

cur.close()
conn.close()
