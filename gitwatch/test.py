#!/usr/bin/python
from __future__ import print_function
from git import Repo
from datetime import datetime
import yaml

configfile = "config-example.yaml"
runfile = "runfile-example.yaml"

# Set up configuraiton
conf = yaml.safe_load(open(configfile))
repo = Repo(conf['repodir'])
now = datetime.now()

def write_runfile(run):
    try:
        with open(runfile, 'w') as outfile:
            outfile.write( yaml.dump(run, default_flow_style=False) )
    except IOError:
        logtime = datetime.now().isoformat()
        print(logtime, "ERROR - Unable to write runfile.")
        exit(1)

try:
    run = yaml.safe_load(open(runfile))
except IOError:
    run = dict(lastrun = int(now.strftime("%s")))
    logtime = datetime.now().isoformat()
    print(logtime, "First run, just creating runfile and exiting.")
    print(logtime,
        "Tracking new commits from this moment in time:",
        now.isoformat())
    write_runfile(run)
    exit(0)

commits = list(repo.iter_commits('master'))

for commit in commits:
    if commit.committed_date > run['lastrun']:
        print(commit.author.email)
        print(datetime.utcfromtimestamp(commit.committed_date).isoformat())

run['lastrun'] = int(now.strftime("%s"))
write_runfile(run)
exit(0)
