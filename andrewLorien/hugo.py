#!/usr/bin/python3
# using python 3.5.2

from shutil import rmtree
from datetime import datetime, timezone
import re
import argparse
import subprocess

hugoSitePath = "/home/ubuntu/hugo_IsentiaChallenge/"
hugoSitePath = "/home/radagast/miscWorks/IsentiaSep2018/Coding-Challenge/andrewLorien/IsentiaChallenge/"


parser = argparse.ArgumentParser(prog='hugo.py')
parser.add_argument('environment', choices=['dev', 'staging'], help='dev or staging')
#parser.print_help()
args = parser.parse_args()

### DEV
def update_dev():

    # delete public/*
    rmtree(hugoSitePath + "public/", True)

    # edit content/fortune.md
    ## bug : python's %z returns a string like "0000", but hugo's timestamp wants "00:00"
    pageTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
    newPage = open(hugoSitePath + "content/fortune" + pageTime + ".md", "w")
    ## add header (date etc)
    # date: 2018-10-03T13:44:41+10:00
    newPage.write("+++\n")
    newPage.write("title = \"Your fortune at " + pageTime + "\"\n")
    newPage.write("date = \"" + pageTime + "\"\n")
    newPage.write("+++\n")

    ## add fortune text  (use markdown "two spaces at the end of a line makes a line break" formatting)
    fortuneResult = subprocess.run("fortune", stdout=subprocess.PIPE).stdout.decode().replace("\n","  \n")
    newPage.write(fortuneResult)

    newPage.close()


### STAGING
def update_footer(environment):
    # update version and footer (major.minor.dev)
    ## NOTE : footer.html MUST contain a line '<div class="version">' followed by a line like \d+.\d+.\d+
    with open(hugoSitePath + "layouts/partials/footer.html", "r+") as footerFile:
        for line in footerFile:
            if '<div class="version">' in line:
                oldVersion = next(footerFile)
                versions = re.split("\.",oldVersion)
                if environment == "dev":
                    newVersion = versions[0] + "." + versions[1] + "." + increment(versions[2])
                if environment == "staging":
                    newVersion = versions[0] + "." + increment(versions[1]) + ".0"

                break
    
            
    with open(hugoSitePath + "layouts/partials/footer.html", 'r') as footerFile :
        filedata = footerFile.read()

    # Replace the target string
    filedata = filedata.replace(oldVersion, newVersion + "\n")

    # Write the file out again
    with open(hugoSitePath + "layouts/partials/footer.html", 'w') as footerFile:
        footerFile.write(filedata)    

 

def build(environment):
    # build
    subprocess.run("hugo")
    # push to dev
    
    
def increment(v):
    return str((int(v)+1))


if args.environment == "dev":
    update_dev()
    
update_footer(args.environment)
build(args.environment)
