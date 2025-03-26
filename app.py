from flask import Flask, render_template, request, redirect, url_for
import random
import csv
from datetime import datetime
import uuid
import os

# Create the Flask app
app = Flask(__name__)

# File where we'll store user interaction logs
DATA_FILE = 'data/user_logs.csv'

# Create 'data' folder if it doesn't exist
os.makedirs('data', exist_ok=True)

# If the CSV doesn't exist yet, create it with column headers
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'user_id', 'group', 'clicked'])


@app.route('/')
def index():
    # Randomly assign user to Group A or Group B
    group = random.choice(['A', 'B'])

    # Generate a unique user ID for tracking
    user_id = str(uuid.uuid4())

    # Log the visit to the CSV with clicked = 0 (not clicked yet)
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), user_id, group, 0])

    # Redirect user to their landing page with group & user_id in the URL
    return redirect(url_for('landing', group=group, user_id=user_id))


@app.route('/landing/<group>/<user_id>')
def landing(group, user_id):
    # Show different HTML templates based on group
    if group == 'A':
        return render_template('index_a.html', user_id=user_id, group=group)
    else:
        return render_template('index_b.html', user_id=user_id, group=group)


@app.route('/click/<user_id>/<group>')
def click(user_id, group):
    # Load all rows from the CSV
    rows = []
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            # If the row matches the user and group, update clicked to 1
            if row[1] == user_id and row[2] == group and row[3] == '0':
                row[3] = '1'
            rows.append(row)

    # Save all rows back (with updated click)
    with open(DATA_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    return "✅ Thanks for signing up! Your action has been recorded."


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
