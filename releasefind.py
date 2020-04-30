from github import Github
from os import getenv
from time import sleep
g = Github(getenv("token"))
print("Waiting for GitHub")
sleep(10)
rels = g.get_organization("family-richards").get_repo("Python-Email-Helpers").get_releases()
tag = rels[0].tag_name
print("Latest version is "+tag)
setup = open("setup.py", "r").read()
setup = setup.split("\n")
setup[1] = 'version = "'+tag+'"'
setupW = open("setup.py", "w")
setupW.write("\n".join(setup))
setupW.close()
