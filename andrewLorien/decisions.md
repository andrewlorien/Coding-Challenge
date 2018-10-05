# DevOps challenge thoughts:


## Folder structure
Using a single git repo because i'm only working on this for a couple of days
Using a monolithic ansible playbook because I'm only doing this once

DevOpsChallenge
- playbook
-- etc

- site
-- fetch
-- update
--- dev 
--- staging

## Architecture
### AWS 
ap-southeast-2
t2.micro  (t3 is out now, but not in the free tier)
Ubuntu 16.04
ami-0be0161e4ddec9e56 
ELB -> web servers

### Ansible server 
"ansible hugo" has more google hits than "ansible jekyll". Using hugo

use EC2 systems manager to install packages and run playbooks? https://aws.amazon.com/blogs/mt/running-ansible-playbooks-using-ec2-systems-manager-run-command-and-state-manager/
 
on bootstrap:
- configure AWS resources
- create slave machine
- install and configure hugo (some guys example)
- schedule using crontab on the ansible server?
- *TODO* git credentials are stored insecurely using the default git credential helper.  I wouldn't do that if I wasn't the only person with access
- *TODO* copy ansible and python logs to S3

### hugo
- create repo with base site manually
- script dev/staging steps
- nginx.yml does NOT check out again from git.  It should, but since it runs from the same folder on the same server I didn't do it

### web server
- configure nginx
- respond to DNS
- not setting up SSL/TLS on the web server because it should be terminated at the ELB
- caching?


## time tracking
- docs
- architecture
- research
- code
 
# Retrospective Thoughts
- For this task, Ansible was overkill. cloudformation would have been simpler and more portable
- And for my first exposure to Ansible, it was surprisingly hard to set up.  I'm sure there's an AMI or a Docker image or something, I'd definitely use that in the future.  Ansible appears often enough in the CVE lists that you'd want to make sure you were maintaining it
- Security wasn't mentioned in the requirements at all, so I didn't pay it too much attention.  But there would be another day's work securind the environment, the user and EC2 IAM accounts, and the github and Linux keys.  My design assumes that I am the only person with access to any of that.  I didn't lock down the Ansible host or the web server.
- Obviously it would be much easier to serve the static files from S3, but in the real world I guess that nginx server would be doing other work.
