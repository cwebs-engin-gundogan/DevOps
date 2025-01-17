from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# PostgreSQL connection using environment variables
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST', 'localhost'),  # Default to localhost if not set
        port=os.getenv('DB_PORT', '5432')        # Default to 5432 if not set
    )
    return conn

@app.route('/')
def hello():
    return "Merhaba, Dünya!"

@app.route('/users')
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
