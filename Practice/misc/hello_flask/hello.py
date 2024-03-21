from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func}</b>"
    return wrapper


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold()
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greeting(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
