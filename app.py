from flask import Flask, render_template as rt

app = Flask(__name__)


@app.get("/fizzbuzz")
def fizzbuzz():
    return rt("fizz.html")