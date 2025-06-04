from app import app
from flask import request

@app.route('/')
def index():
    return "Welcome!"

@app.route('/vuln')
def vuln():
    user_input = request.args.get('input')
    eval(user_input)  # BAD: insecure eval usage
    return "Executed!"
