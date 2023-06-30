import subprocess

ssh_ip = '192.168.1.42'
ssh_pass = 'iamgw_#@!'
user_name = 'pi'

change_dir = 'cd /home/pi/iam-gateway'
git_status = 'git status'
active_venv = 'source venv/bin/activate'
git_checkout = 'git checkout main'
command = f"sshpass -p {ssh_pass} ssh {user_name}@{ssh_ip} '{change_dir} && {git_status} && {active_venv} && {git_checkout}'"

output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode()

print(output)

