from github import Github
from os import getenv
g = Github(getenv("token"))
rels = g.get_user().get_repo("Python-Email-Helpers").get_releases()
tag = rels[rels.totalCount-1].tag_name
