import requests
import time

# Define the URL of the application
APP_URL = "http://example.com"

# Define the expected HTTP status code for a healthy application
EXPECTED_STATUS_CODE = 200

# Define the timeout for the HTTP request
TIMEOUT = 5

# Function to check the application's status
def check_app_status():
    try:
        response = requests.get(APP_URL, timeout=TIMEOUT)
        if response.status_code == EXPECTED_STATUS_CODE:
            return "up"
        else:
            return "down"
    except requests.ConnectionError:
        return "down"
    except requests.Timeout:
        return "down"
    except requests.RequestException:
        return "down"

# Main function
def monitor_app_uptime():
    while True:
        status = check_app_status()
        if status == "up":
            print(f"{APP_URL} is up and running!")
        else:
            print(f"{APP_URL} is down!")
        time.sleep(60)  # Check every 1 minute

# Run the script
monitor_app_uptime()