from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/calculator/<int:num1>/<int:num2>")
def calculator(num1,num2):
    return render_template("calc.html", n1 = num1, n2 = num2)

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return render_template("add.html",title="Addition",n1=num1,n2=num2)

@app.route("/sub/<int:num1>/<int:num2>")
def sub(num1, num2):
    return render_template("sub.html",title="Substraction",n1=num1,n2=num2)

@app.route("/mul/<int:num1>/<int:num2>")
def mul(num1, num2):
    return render_template("mul.html",title="Multiplication",n1=num1,n2=num2)

@app.route("/div/<int:num1>/<int:num2>")
def div(num1, num2):
    return render_template("div.html",title="Division",n1=num1,n2=num2)

if __name__ == "__main__":
    app.run(debug=True)