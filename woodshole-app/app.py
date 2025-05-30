from flask import Flask, render_template_string, request, redirect, url_for, session
import pandas as pd
from datetime import datetime, timedelta
import os
import uuid
import calendar

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Define the data folder path
DATA_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "availability_data")

# Ensure the data folder exists
try:
    os.makedirs(DATA_FOLDER, exist_ok=True)
except OSError as e:
    print(f"Error creating data directory: {e}")
    raise

# HTML Templates
form_template = '''
<!doctype html>
<html>
<head>
    <title>Wood's Hole Summer Plans!</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f4f8; margin: 0; padding: 20px; }
        h2 { color: #2c3e50; }
        form { background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        input[type=text], input[type=date] { margin: 10px 0; padding: 8px; width: 100%%; border: 1px solid #ccc; border-radius: 4px; }
        input[type=submit] { padding: 10px 20px; background-color: #2ecc71; color: white; border: none; border-radius: 4px; cursor: pointer; }
        a { display: block; margin-top: 20px; color: #2980b9; }
        .add-btn { margin-top: 10px; display: inline-block; background-color: #3498db; color: white; padding: 6px 10px; border-radius: 4px; text-decoration: none; }
    </style>
</head>
<body>
<h2>Wood's Hole Summer Plans! (Group: {{ group_id }})</h2>
<form action="/woodsholesummerplans/submit" method="post" id="availability-form">
    Name: <input type="text" name="name" required><br>
    <div id="date-sets">
        <div class="date-set">
            Start Date: <input type="date" name="start_date[]" required>
            End Date: <input type="date" name="end_date[]" required><br>
        </div>
    </div>
    <a href="#" class="add-btn" onclick="addDateSet()">+ Add More Dates</a><br><br>
    <input type="submit" value="Submit Availability">
</form>
<a href="/woodsholesummerplans/calendar">View Group Calendar</a>
<script>
    function addDateSet() {
        const div = document.createElement('div');
        div.classList.add('date-set');
        div.innerHTML = 'Start Date: <input type="date" name="start_date[]" required> End Date: <input type="date" name="end_date[]" required><br>';
        document.getElementById('date-sets').appendChild(div);
    }
</script>
</body>
</html>
'''

calendar_template = '''
<!doctype html>
<html>
<head>
    <title>Wood's Hole Summer Plans! Calendar</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f8f9fa; padding: 20px; }
        h2 { color: #34495e; }
        .calendar { display: flex; flex-wrap: wrap; gap: 30px; }
        .month { border: 1px solid #ccc; border-radius: 8px; padding: 10px; background-color: white; width: 300px; }
        .month h3 { text-align: center; }
        table { width: 100%%; border-collapse: collapse; }
        td { text-align: center; padding: 10px; border: 1px solid #eee; }
        .available { background-color: #2ecc71; color: white; }
        .unavailable { background-color: #e74c3c; color: white; }
    </style>
</head>
<body>
<h2>Availability Calendar (Group: {{ group_id }})</h2>
<div class="calendar">
    {% for month, weeks in calendar_data.items() %}
    <div class="month">
        <h3>{{ month }}</h3>
        <table>
            <tr>
                {% for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] %}
                <th>{{ day }}</th>
                {% endfor %}
            </tr>
            {% for week in weeks %}
            <tr>
                {% for day in week %}
                <td class="{{ 'available' if day[1] else 'unavailable' }}">{{ day[0] or '' }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    </div>
    {% endfor %}
</div>
<a href="/woodsholesummerplans">Submit More Availability</a>
</body>
</html>
'''

@app.route("/")
def home():
    return redirect(url_for("index"))

@app.route("/woodsholesummerplans")
def index():
    if "group_id" not in session:
        session["group_id"] = str(uuid.uuid4())[:8]
    return render_template_string(form_template, group_id=session["group_id"])

@app.route("/woodsholesummerplans/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    start_dates = request.form.getlist("start_date[]")
    end_dates = request.form.getlist("end_date[]")
    group_id = session.get("group_id")
    file_path = os.path.join(DATA_FOLDER, f"{group_id}.csv")

    try:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
        else:
            df = pd.DataFrame(columns=["name", "start_date", "end_date"])

        for start, end in zip(start_dates, end_dates):
            df = pd.concat([df, pd.DataFrame([{
                "name": name,
                "start_date": start,
                "end_date": end
            }])])

        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error processing submission: {e}")
        return "An error occurred while processing your submission.", 500

    return redirect(url_for("calendar"))

@app.route("/woodsholesummerplans/calendar")
def calendar():
    group_id = session.get("group_id")
    file_path = os.path.join(DATA_FOLDER, f"{group_id}.csv")
    if not os.path.exists(file_path):
        return "No availability submitted yet. <a
::contentReference[oaicite:3]{index=3}
 
