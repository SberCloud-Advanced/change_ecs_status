# main module with all the api calls and methods, if needed
#
import requests
#
from variables import *
from urllib3.exceptions import HeaderParsingError, InsecureRequestWarning, ReadTimeoutError
#
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
#
iam = "https://iam.ru-moscow-1.hc.sbercloud.ru"
ecs = "https://ecs.ru-moscow-1.hc.sbercloud.ru"
#

# api call to get project token with all the needed variables
# see more: https://support.hc.sbercloud.ru/api/iam/en-us_topic_0057845583.html
def token():
	url = iam + "/v3/auth/tokens"
	headers = {
		"Content-Type": "application/json;charset=utf8"
	}
	data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                    "password": {
                        "user": {
                                "name": iam_name,
                                "password": account_password,
                            "domain": {
                                "name": account_name
                        }
                    }
                }
            },
            "scope": {
                "project": {
                    "id": project_id
                }
            }
        }
    }
	token = requests.post(
		url, 
		headers = headers, 
		json = data,
		verify = False
		).headers['X-Subject-Token']
	return token
#
# api call to change status of VM
# START: see more https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0020212648.html
# RESTART: see more https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0020212650.html
# STOP: see more https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0020212652.html
def change_status_ecs(project_token):
	url = ecs + "/v2.1/" + project_id + "/servers/" + ecs_id + "/action"
	headers = {
		"Content-Type": "application/json;charset=utf8",
		"X-Auth-Token": project_token
	}
	#
	if ecs_status == 'start':
		data = {
			"os-start": {}
		}
	elif ecs_status == 'restart':
		data = {
			"reboot": {
				"type": "SOFT"
			}
		}
	elif ecs_status == 'stop':
		data = {
			"os-stop": {}
		}
	else:
		print('Unknown command')
	#
	response = requests.post(
		url, 
		headers = headers,
		json = data,
		verify=False
	)
	return response
#
# api call to check the status of virtual machine
# see more: https://support.hc.sbercloud.ru/en-us/api/ecs/en-us_topic_0094148849.html
def check_ecs_status(project_token):
	url = ecs + '/v1/' + project_id + '/cloudservers/' + ecs_id
	headers = {
		"Content-Type": "application/json;charset=utf8",
		"X-Auth-Token": project_token
	}
	response = requests.get(
		url,
		headers = headers, 
		verify = False
	).json()
	checker = response['server']['status']
	if ecs_status == 'start':
		status = 'ACTIVE'
		if checker == status:
			result = "Success"
		else:
			result = "Failure"
	elif ecs_status == 'restart':
		status = 'REBOOT'
		if checker == status:
			result = "Success"
		else:
			result = "Failure"
	elif ecs_status == 'stop':
		status = 'SHUTOFF'
		if checker == status:
			result = "Success"
		else:
			result = "Failure"
	return result