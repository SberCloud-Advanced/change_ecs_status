# module containing all the variables
# variables gonna be taken from bash vars
import os
# iam user name, if created
iam_name = os.environ['iam_user']
# account or domain name, might be the same as username
account_name = os.environ['domain_name']
# account or user password, simple as that
account_password = os.environ['domain_pass']
# project id, could be found in iam service page, projects section
project_id = os.environ['project_id']
# virtual machine id, could be found in ecs list page
ecs_id = os.environ['ecs_id']
# what operation to do with virtual machine
ecs_status = os.environ['ecs_status']