from github import Github
from os import getenv
g = Github(getenv("token"))
rels = g.get_user().get_repo("Python-Email-Helpers").get_releases()
tag = rels[rels.totalCount-1].tag_name
setup = open("setup.py", "r").read()
setup = setup.split("\n")
setup[1] = 'version = "'+tag+'"'
setupW = open("setup.py", "w")
setupW.write("\n".join(setup))
setupW.close()
