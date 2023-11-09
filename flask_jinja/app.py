from flask import Flask, render_template

app = Flask(__name__)


@app.route("/for_loop/list")
def for_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto",
    ]
    return render_template("for_loop.html", planets=planets)


todos = [("Get milk", True), ("Learn Programming", False)]


@app.route("/base_todo")
def base_todo():
    return render_template("base_home.html", todos=todos)


@app.route("/base_todo/<string:todo>")
def todo_item(todo: str):
    for text, completed in todos:
        if text == todo:
            complete_text = "[X]" if completed else "[]"
            title = f"{complete_text} - Todos"
            return render_template(
                "base_todo.html", todos=todos, text=todo, completed=completed
            )
        else:
            return render_template("base_nofound.html", text=todo)


@app.route("/to_do/")
def to_do():
    todos = [("Get milk", True), ("Learn Programming", False)]

    return render_template("to_do.html", todos=todos)


@app.route("/for_loop/dict")
def for_loop_condition():
    customers = {"Bob": "Windows", "Anna": "MacOS", "Adam": "Linux", "Alex": "Linux"}

    return render_template("for_loop_condition.html", customers=customers)


@app.route("/")
def hello():
    return "Hello, World! this application runing on http://127.0.0.1:5000/"


@app.route("/first")
def first():
    return render_template("first_page.html", name="Bob", content="my name is bob")


@app.route("/second")
def second():
    return render_template("second_page.html")


@app.route("/expression")
def expression():
    arg = {
        "fruit1_amount": 10,
        "fruit2_amount": 5,
        "object_amount": 1,
        "fruit1_colour": "red",
        "fruit2_colour": "yelllo",
        "object_colour": "green",
        "fruit1": "apple",
        "fruit2": "banana",
        "object": "ball",
    }

    return render_template("expression.html", **arg)


@app.route("/data_structure")
def data_structure():
    movies = ["Inception", "Forzen", "The Lion King"]

    car_info = {
        "color": "blue",
        "brand": "BMW",
        "year": "1993",
    }
    return render_template(
        "data_structure.html",
        movie=movies,
        car=car_info,
    )


@app.route("/conditional_basic/")
def conditional_basic():
    compony = "ARM"
    apple = ["iPad", "iPhone", "iMac"]
    microsoft = ["Microsoft Phone", "Surface Pro", "Surface Book"]
    args = {
        "compony": compony,
        "apple": apple,
        "microsoft": microsoft,
    }

    return render_template("conditional_basic.html", **args)
