import os
from config import Config

config = Config()

python_path = config.PYTHON_PATH
project_path = config.PROJECT_PATH

# Task Name
task_name = "WeatherScriptTask"

# Corrected Task Scheduler command
task_command = (
    f'schtasks /create /tn "{task_name}" '
    f'/tr "{python_path} {project_path}" '
    f'/sc DAILY /st 10:00 /F'
)

# Execute the command
os.system(task_command)

print(f" Task '{task_name}' added successfully! It will run **daily at 10:00 AM**.")
