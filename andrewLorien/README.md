# Andrew Lorien's Isentia devOps challenge

There are three important files, all to be run from this folder

## IsentiaChallenge_ec2.yml
Sets up the environment, including all AWS components and the web server
Run it from an ansible host within a VPC like this:
`ansible-playbook IsentiaChallenge_ec2-.yml --key-file "~/.aws/dev_staging.pem"`

Run it again if you make changes to the environment, or if you want another web server (the old one will not be terminated)

## hugo.py
Adds a new fortune, updates the site version, compiles and copies to dev/ or staging/ folders
Run it using python3 like this:
`python3 hugo.py dev `

## nginx.yml 
Copies the dev or staging folder to the matching folder on the web server.
Run it like this
`AWS_PROFILE=radagast ansible-playbook -i ec2.py nginx.yml --key-file ~/.aws/dev_staging.pem`

To fulfil the challenge, the IsentiaChallenge_ec2.yml creates a crontab on the ansible host which:
every five minutes runs
`AWS_PROFILE=radagast ansible-playbook -i ec2.py nginx.yml --key-file ~/.aws/dev_staging.pem`
every ten minutes runs
`python3 hugo.py dev `
every hour runs
`python3 hugo.py staging `

There are a couple of race conditions
- the dev and staging builds are deleted before the hugo build.  The crontab gets around this by ensuing that the three jobs are out of sync, but it could be fixed by more robust file management.
- hugo takes a few seconds to compile, so if the nginx script ran while it was compiling the site would break.  the hugo script should include a lock
