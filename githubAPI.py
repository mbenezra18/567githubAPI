'''
@author Michayla Ben-Ezra
September 23, 2018

SSW567 - HW04
'''

import requests
import json

def GetRepos(user_id):

    r = requests.get('https://api.github.com/users/' + user_id + '/repos')
    repos = []
    repos_info = json.loads(r.text)

    for i in repos_info:
        try:
            repos += [i.get('name')]
        except (attributeError):
            print ('Error: This user does not have any repositories.')
            return []
        return repos

def retrieve_commits(user_id, Repository):
    repo_commits = requests.get('https://api.github.com/repos/' +user_id+ '/' +Repository+ 'commits')
    pushTo_json = json.load(repo_commits.text)

    return len(pushTo_json)

def main():

    user_id = input("Please input a GitHub username:")


    repos = Repository(user_id)

    if len(repos) > 0:
        for i in repos:
            print("Repository: " +r+ "Number of Commits: " +str(retrieve_commits(user_id, r)))