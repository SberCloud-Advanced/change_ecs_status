python3 -m pip install requests
#
cat <<EOF
############################################################################################
# The present BASH script and all used libraries come with no warranties and support.      #
# Use them for further development or as an example of how to use Sbercloud Advanced APIs. #
# For more APIs please visit: https://support.hc.sbercloud.ru/index.html                   #
############################################################################################
EOF
#
read -p "IAM Username (might coincede with account name): " iam_user
read -p "Sbercloud Advanced account name: " domain_name
read -s -p "User password: " domain_pass
read -p "Sbercloud Advanced IAM project ID (example: 0c7867f1XXXX26df2f66c00f3XXXXd39): " project_id
read -p "ECS resource ID (example: 3696dec9-2975-4fe8-be26-93261cdbb578): " ecs_id
read -p "Operation to do with ECS (operations: start / restart / stop): " ecs_status
#
export iam_user domain_name domain_pass project_id ecs_id ecs_status
#
python3 main.py