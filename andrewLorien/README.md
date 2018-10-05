# Andrew Lorien's Isentia devOps challenge

There are three important files, all to be run from this folder

## IsentiaChallenge_ec2.yml
Sets up the environment, including all AWS components and the web server
Run it from an ansible host within a VPC like this:
ansible-playbook IsentiaChallenge_ec2-.yml --key-file "~/.aws/dev_staging.pem"

Run it again if you make changes to the environment, or if you want another web server (the old one will not be terminated)

## hugo.py
Adds a new fortune, updates the site version, compiles and copies to dev/ or staging/ folders
Run it using python3 like this:
python3 hugo.py dev 

## nginx.yml 
Copies the dev or staging folder to the matching folder on the web server.
Run it like this
AWS_PROFILE=radagast ansible-playbook -i ec2.py nginx.yml --key-file ~/.aws/dev_staging.pem

