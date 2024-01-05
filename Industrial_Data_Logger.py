# data_logger.py

import time
import random

from datetime import datetime
import mysql.connector


def log_data_to_database():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="192.168.217.105",
        user="root",
        password="123456",
        database="industrial_data"
    )
    cursor = conn.cursor()

    while True:
        # Simulate data from sensors
        sensor_data = random.uniform(20, 100)
        print(sensor_data)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Insert data into the database
        cursor.execute("INSERT INTO sensor_data (timestamp, value) VALUES (%s, %s)", (timestamp, sensor_data))
        conn.commit()

        time.sleep(5)  # Log data every 5 seconds

    conn.close()


if __name__ == "__main__":
    log_data_to_database()
