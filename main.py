# main module to run the process and check the result
#
import time
#
from methods import *
#
project_token = token()
change_status = change_status_ecs(project_token)
stat_msg = "Waiting 15 seconds"
print(stat_msg)
time.sleep(15)
stat_msg = "Checking VM status"
status = check_ecs_status(project_token)
if status == "Success":
    stat_msg = "Operation completed succesfully"
elif status == "Failure":
    stat_msg = "Operation failed"
else:
    stat_msg = "Error"
print(stat_msg)
stat_msg = "Exitting..."
print(stat_msg)