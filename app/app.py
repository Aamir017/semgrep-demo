import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Vulnerable route: SQL Injection
@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    result = cursor.fetchall()
    return {"result": result}

# Vulnerable hardcoded secret
API_KEY = "SUPERSECRETKEY123"
