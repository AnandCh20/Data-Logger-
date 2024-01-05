# dashboard.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def dashboard():
    # Connect to the SQLite database
    conn = sqlite3.connect('industrial_data.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()

    conn.close()

    return render_template('dashboard.html', sensor_data=data)


if __name__ == "__main__":
    app.run(debug=True)
