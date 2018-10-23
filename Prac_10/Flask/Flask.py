from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<temp>')
def f(temp=""):
    return "{} celsius = {} fahrenheit ".format(temp, str(convert_to_fahrenheit(float(temp))))


def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
