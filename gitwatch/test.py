#!/usr/bin/python
from git import Repo
repodir = "../vagrant-xdata/"

repo = Repo(repodir)


commitIDs = []
#load in batches to prevent hangs? not sure if you should care - personally I wouldn't bother with this
start, max_count = 0, 100
while True:
    text = repo.git.rev_list("master", max_count=max_count, skip=start)
    lines = text.splitlines()
    start += len(lines)
    #append shas to commitIds
    commitIDs += lines

    if len(lines) < max_count:
        break
#print commitIDs[0]
#print repo.git.show(commitIDs[0])


'''
import git
from datetime import datetime
repodir = "../vagrant-xdata/"
repo = git.Git(repodir)
log = repo.log()

repo = git.Repo(repodir)

log = repo.heads.origin.log()
for entry in log:
    print "time:", datetime.utcfromtimestamp(entry[3][0])

heads = repo.heads
print heads
master = heads.master
log = master.log()
print log[0][0]
print log[-1]
'''
