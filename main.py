import subprocess
import requests
from datetime import datetime, timedelta
import time

#enter bot data here
id = 123456
token = "SlavaRodu"

# Function for getting ssh login attempts
def ssh_analyze():
    start_time = datetime.now() - timedelta(minutes=1)
    since_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
    command = ['journalctl', '--since', since_time, '/var/log/auth.log']
    logs = subprocess.run(command, capture_output=True, text=True).stdout
    for line in logs.split('\n'):
        if 'Failed password' in line:
            notification("Uncompleted login attempt via SSH")

#Function for message sending
def notification(text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {"chat_id": id, "text": text}
    response = requests.post(url, params=params)

while True:
    ssh_analyze()
    time.sleep(60)
