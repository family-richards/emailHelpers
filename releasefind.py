from github import Github
from os import getenv
from time import sleep
print("Waiting...")
sleep(15)
print("Done waiting...")
g = Github(getenv("token"))
rels = g.get_organization("family-richards").get_repo("emailHelpers").get_releases()
tag = rels[0].tag_name.replace("v", "")
print("Latest version is "+tag)
setup = open("setup.py", "r").read()
setup = setup.split("\n")
setup[1] = 'version = "'+tag+'"'
setupW = open("setup.py", "w")
setupW.write("\n".join(setup))
setupW.close()
