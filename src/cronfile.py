from crontab import CronTab
from config import config

cron = CronTab(user = True)
my_user = CronTab(user = 'User')

python_path = config.PYTHON_PATH
project_path = config.PROJECT_PATH


weather_job = cron.new(command = f'{python_path} {project_path}')

weather_job.setall('0 10 */15 * *')

cron.write()

print("Cron job added successfully! It will run every 15 days at 10:00 AM.")


