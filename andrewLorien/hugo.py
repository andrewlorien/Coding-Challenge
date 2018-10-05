#!/usr/bin/python3
# using python 3.5.2

# run me like this
# /usr/bin/python3 hugo.py {dev|staging}

from shutil import rmtree, copytree
from datetime import datetime, timezone
import re
import argparse
import subprocess
import os

hugoSitePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"IsentiaChallenge/")

parser = argparse.ArgumentParser(prog='hugo.py')
parser.add_argument('environment', choices=['dev', 'staging'], help='dev or staging')
#parser.print_help()
args = parser.parse_args()

### DEV
def update_dev():

    print("adding new fortune to dev")
    # delete compiled sites

    # edit content/fortune.md
    ## bug : python's %z returns a string like "0000", but hugo's timestamp wants "00:00"
    pageTime = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
    print("{}content/fortune{}.md".format(hugoSitePath,pageTime))
    newPage = open("{}content/fortune{}.md".format(hugoSitePath,pageTime), "w")
    ## add header (date etc)
    # date: 2018-10-03T13:44:41+10:00
    newPage.write("+++\n")
    newPage.write("title = \"Your fortune at {}\"\n".format(pageTime))
    newPage.write("date = \"{}\"\n".format(pageTime))
    newPage.write("+++\n")

    ## add fortune text  (use markdown "two spaces at the end of a line makes a line break" formatting)
    fortuneResult = subprocess.run("fortune", stdout=subprocess.PIPE).stdout.decode().replace("\n","  \n")
    newPage.write(fortuneResult)

    newPage.close()


### STAGING
def update_footer(environment):
    # update version and footer (major.minor.dev)
    ## NOTE : footer.html MUST contain a line '<div class="version">' followed by a line like \d+.\d+.\d+
    print("updating footer version")
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
    
            
    with open("{}layouts/partials/footer.html".format(hugoSitePath), 'r') as footerFile :
        filedata = footerFile.read()

    # Replace the target string
    filedata = filedata.replace(oldVersion, newVersion + "\n")

    # Write the file out again
    with open("{}layouts/partials/footer.html".format(hugoSitePath), 'w') as footerFile:
        footerFile.write(filedata)    
        
    return newVersion

 

def build(environment,newVersion):
    print("running hugo")
    # build
    subprocess.run("hugo",cwd=hugoSitePath)
    print("pushing to git")
    # copy to dev/staging
    copytree("{}public".format(hugoSitePath), "{}{}".format(hugoSitePath,environment))
    # add to git repo for deployment to remote server
    # TODO : check for git errors
    print(hugoSitePath)
    subprocess.run(["git","-C",hugoSitePath,"add","content"])
    subprocess.run(["git","-C",hugoSitePath,"add",environment])
    subprocess.run(["git","-C",hugoSitePath,"commit","-m","\"hugo.py checking in version {}".format(newVersion)])
    # this is cheap, but in a real-world situation we'd have separate repos
    subprocess.run(["git","-C","{}../../".format(hugoSitePath),"push"])
   
    
def increment(v):
    return str((int(v)+1))

#############  BEGIN ##################
# Clean up
rmtree(hugoSitePath + "public/*", True)
rmtree(hugoSitePath + "dev/", True)
rmtree(hugoSitePath + "staging/", True)

if args.environment == "dev":
    update_dev()
    
newVersion = update_footer(args.environment)

build(args.environment,newVersion)
