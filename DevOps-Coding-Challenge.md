# Isentia DevOps - Static website generator and build flow

Make sure you read **all** of this document carefully, and follow the guidelines in it.

## Background

The purpose of this test is to:

- evaluate your technical knowledge
- evaluate your communication with the team
- evaluate your ability to learn

## Preamble

DevOps at Isentia involves a lot of different technologies and DevOps engineers are expected to be able to navigate through them efficiently.

## Technical stack

Here is the list of the technologies that we can use in the test:

- [**Ansible**](https://www.ansible.com/)
- [**Jekyll**](https://jekyllrb.com/) or [**Hugo**](https://gohugo.io/) static site generator
- **Git**
- Programming Language: **Python** / **Go** / **Shell** or any other language.

## Task

The test is composed of 2 components:
- a **dev** related task; where you'll be expected to prepare a simple site using a static site generator,
- an **ops** related task; where you'll be expected to spawn a server to run and operate the site you've created.

**Make sure you create appropriate documentation on how to run your code and playbook. Create a `README.md` file for that purpose, or store the documentation in a `docs/` folder.**

### Development task

You will need to create:
- a site, based on a static site generator (Jekyll or Hugo),
- a script that will create a new post in your site, and update some meta data information (version - see below), eventually pushing the changes back to github.

A few suggestions / recommendations:

- Choose whichever static site generator to use and prepare the basic site, plenty of tutorial are available online:
    - [Jekyll](https://jekyllrb.com)
    - [Hugo](https://gohugo.io)
- Prepare templates for your site generator:
    - base template for your site to display the `version` in the footer of the pages, and a list of the posts on the landing page,
    - post template that will display the content of individual pages
- Prepare a script (choose whichever language) that will take one parameter:
    - either `dev`, in which case, it will:
        - create a new post using markdown with yaml frontmatter format,
        - use the output of [`fortune`](http://manpages.ubuntu.com/manpages/xenial/man6/fortune.6.html) command as content,
        - and increment the version of the site by `0.0.1`,
        - compile the site, 
        - commit and push the sources (markdown files) and build site (html) back to github
    - or `staging`, in which case, it will:
        - take the last known version of the site,
        - increment the version of the site by `0.1.x` (e.g. move from `0.1.5` to `0.2.0`) 
        - compile the site
        - commit, tag and push to github

### Operation

You will need to:
- write an ansible playbook to configure a server:
    - either real cloud server (aws/digital ocean) 
    - or vagrant box, please include the Vagrantfile
- that server needs to serve:
    - the dev environment,
    - the staging (tag based) environment
- create an ansible playbook or a script that would:
    - fetch the codebase of your site from github every N minutes,
    - update the dev for every new commit
    - update the staging for every new tag
- get everything to run together!

A few suggestions / recommendations:

- Spawn a box with:
    - ubuntu 16.04
    - Nginx with configuration supporting two domains: dev & staging
    - Ruby / Jekyll or Go, this depend on the choice of your dev project above.

- Configure the box to run the compile steps on the box:
    - Compile and build the code (jekyll or hugo)
    - Deploy the dev / staging environments accordingly.

- Prepare automated tasks to run the created script mentioned in development part.
    - Generate new page and push to github every 10 minutes. (run the script for `dev`)
    - tag and push to github every 1 hour. (run the script for `staging`)

- Prepare automated tasks to auto update the served sites every 5 minutes following roles:
    - if there is a new commit, then update the dev server
    - if there is a new tag, then update the staging server

- Optional
    - Map a custom domain name on the server, install a Letsencrypt SSL/TLS certificate
    - Optimise content delivery by using client side or server side caching  


# Requirements

- With clear documentation on how to run the code
- Use git to manage code

# What We Care About

Feel free to schedule your work, ask questions.

We're interested in your method and how you approach the problem just as much as we're interested in the end result.

Here's what you should aim for:

- Comments in your scripts
- Comments in your playbooks
- Clean README file that explains how things work
- Extensible work / code (use variables, limit hardcoded values, etc.)

# Result
Candidate should put their test results on a public code repository hosted on Github. Once test is completed please share the Github repository URL to hiring team so they can review your work.
