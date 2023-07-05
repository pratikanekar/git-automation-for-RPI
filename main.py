import subprocess

ssh_ip = '192.168.1.42'
ssh_pass = 'iamgw_#@!'
user_name = 'pi'
br_name = "next-release"
change_dir = 'cd /home/pi/gw_testing/iam-gateway'
git_status = 'git status'
active_venv = 'source venv/bin/activate'
install_req = 'pip3 install -r requirements.txt'
restart_iam_ser = 'sudo systemctl restart iam-gateway.service'
git_fetch = 'git fetch'
git_pull = 'git pull'
branch_name = str(input("Enter branch name :"))
git_checkout = f'git checkout {branch_name}'
git_user = 'DHEERAJ1423'
git_pass = 'glpat-G2BFZjJy76beubQamzqB'
# Construct the HTTPS URL with authentication information
git_remote_url = f'https://{git_user}:{git_pass}@gitlab.com/iam-dev/iam-gateway.git'
command = f"sshpass -p {ssh_pass} ssh {user_name}@{ssh_ip} '{change_dir} && {git_fetch} {git_remote_url} && {git_checkout} && {git_status} && {git_pull} {git_remote_url} && {active_venv} && {install_req} && {restart_iam_ser}'"

output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()

print(output)

