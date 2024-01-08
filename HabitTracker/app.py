from flask import Flask, render_template, request
from collections import defaultdict
import datetime

app = Flask(__name__)


completions = defaultdict(list)
habits_list = ["tmp habbit", "tmp2 habbit"]


@app.context_processor
def add_calc_data_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}


@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
        print(date_str)
    else:
        selected_date = datetime.date.today()
        print("none")

    return render_template(
        "index.html",
        habits=habits_list,
        title="Habit Tracker -- Home",
        selected_date=selected_date,
    )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits_list.append(request.form.get("habit"))

    return render_template(
        "add_habit.html",
        title="Habit Tracker -- Add Habit",
        selected_date=datetime.date.today(),
    )
