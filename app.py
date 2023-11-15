from flask import Flask, request

app = Flask(__name__)
def add(x, y):

    return x + y
 
def subtract(x, y):

    return x - y

@app.route('/addition')
def addition():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    return f"{add(x, y)}"

@app.route('/substraction')
def substraction():
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    return f"{subtract(x, y)}"

if __name__ == '__main__':
    app.run(debug=True)