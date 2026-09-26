import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from database import get_connection

load_dotenv()

def setup_admin():
    username = os.getenv("ADMIN_USERNAME", "admin")
    password = os.getenv("ADMIN_PASSWORD", "admin123")

    con = get_connection()
    cur = con.cursor(dictionary=True)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            branch VARCHAR(50),
            address TEXT,
            email VARCHAR(100)
        )
    """)
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cur.fetchone():
        print(f"Admin user '{username}' already exists. Skipping.")
    else:
        hashed = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed))
        con.commit()
        print(f"Admin user '{username}' created successfully!")

    cur.close()
    con.close()

if __name__ == "__main__":
    setup_admin()