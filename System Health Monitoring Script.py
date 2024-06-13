import psutil
import datetime
import smtplib
from email.mime.text import MIMEText

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

# Define email settings
SMTP_SERVER = "your_smtp_server"
SMTP_PORT = 587
FROM_EMAIL = "your_from_email"
TO_EMAIL = "your_to_email"
PASSWORD = "your_password"

# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

# Function to get memory usage
def get_memory_usage():
    return psutil.virtual_memory().percent

# Function to get disk usage
def get_disk_usage():
    return psutil.disk_usage('/').percent

# Function to get running processes
def get_running_processes():
    return len(psutil.pids())

# Function to send email alert
def send_email_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(FROM_EMAIL, PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
    server.quit()

# Main function
def monitor_system_health():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    running_processes = get_running_processes()

    message = ""

    if cpu_usage > CPU_THRESHOLD:
        message += f"CPU usage: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)\n"
    if memory_usage > MEMORY_THRESHOLD:
        message += f"Memory usage: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)\n"
    if disk_usage > DISK_THRESHOLD:
        message += f"Disk usage: {disk_usage}% (Threshold: {DISK_THRESHOLD}%)\n"
    if running_processes > PROCESS_THRESHOLD:
        message += f"Running processes: {running_processes} (Threshold: {PROCESS_THRESHOLD})\n"

    if message:
        subject = "System Health Alert"
        send_email_alert(subject, message)
        print(f"Alert sent: {subject}\n{message}")
    else:
        print("System health is normal.")

# Run the script every 1 minute
while True:
    monitor_system_health()
    time.sleep(60)