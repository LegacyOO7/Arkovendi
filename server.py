from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def route_handler():
    return "Online"

