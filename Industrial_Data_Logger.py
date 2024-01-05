# data_logger.py
import time
import random
from datetime import datetime
import sqlite3


def log_data_to_database() -> object:
    # Connect to the SQLite database
    conn = sqlite3.connect('industrial_data.db')
    cursor = conn.cursor()

    while True:
        # Simulate data from sensors
        sensor_data = random.uniform(20, 100)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute("INSERT INTO sensor_data (timestamp, value) VALUES (?, ?)", (timestamp, sensor_data))
        conn.commit()

        time.sleep(5)  # Log data every 5 seconds

    conn.close()


if __name__ == "__main__":
    log_data_to_database()
