from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "postgres")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")


def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn


@app.route('/')
def home():
    return jsonify({"message": "Backend is running successfully"})


@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/api/data')
def get_data():
    return jsonify({
        "service": "backend",
        "db_host": DB_HOST,
        "db_name": DB_NAME
    })


@app.route('/api/db-check')
def db_check():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"database": "connected"}), 200
    except Exception as e:
        return jsonify({"database": "error", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
