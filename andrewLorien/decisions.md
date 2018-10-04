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
- install and configure hugo (some guys example)
    git clone https://github.com/jtreminio/hugoBasicExample.git
    cd hugoBasicExample
    git clone https://github.com/nanxiaobei/hugo-paper.git \
    themes/hugo-paper
- schedule using crontab on the ansible server?

### hugo
- create repo with base site manually
- script dev/staging steps

### web server
- configure nginx
- respond to DNS
- set up TLS
- caching?


## time tracking
- docs
- architecture
- research
- code
 