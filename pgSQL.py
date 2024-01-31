import os
import psycopg2
from dotenv import load_dotenv
import datetime

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
cur.execute("SELECT last_check_in FROM controller.state WHERE script = 'nft-miner'")
result = cur.fetchone()

current_time = datetime.datetime.now(datetime.timezone.utc)
print(current_time - datetime.timedelta(1) > result[0])


cur.close()
conn.close()
