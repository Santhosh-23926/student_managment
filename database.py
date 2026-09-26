import os
from pathlib import Path
from dotenv import load_dotenv
import mysql.connector
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

def get_connection():
    db_host = os.getenv("DB_HOST", "localhost")
    db_user = os.getenv("DB_USER", "root")
    db_password = os.getenv("DB_PASSWORD", "root")  # <--- Put your actual MySQL root password here as fallback
    db_name = os.getenv("DB_NAME", "santhosh")
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )