from flask import Flask, request
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    return conn

@app.route("/")
def home():
    try:
        conn = connect_db()
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return str(e)

@app.route("/add")
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return {"operation": "addition", "a": a, "b": b, "result": a + b}
    except:
        return {"error": "Invalid input, provide numbers as parameters."}, 400

@app.route("/subtract")
def subtract():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return {"operation": "subtraction", "a": a, "b": b, "result": a - b}
    except:
        return {"error": "Invalid input, provide numbers as parameters."}, 400

@app.route("/multiply")
def multiply():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return {"operation": "multiplication", "a": a, "b": b, "result": a * b}
    except:
        return {"error": "Invalid input, provide numbers as parameters."}, 400

@app.route("/divide")
def divide():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        if b == 0:
            return {"error": "Division by zero is not allowed."}, 400
        return {"operation": "division", "a": a, "b": b, "result": a / b}
    except:
        return {"error": "Invalid input, provide numbers as parameters."}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
