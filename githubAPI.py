"""
@author Michayla Ben-Ezra
September 23, 2018
SSW567 - HW04

I pledge my honor that I have abided by the Stevens Honor System.
"""

import requests
import json


def get_repos(user_id):

    r = requests.get('https://api.github.com/users/' + user_id + '/repos')
    repos = []
    repos_info = json.loads(r.text)

    for i in repos_info:
        try:
            repos += [i.get('name')]
        except AttributeError:
            print('Error: This user does not have any repositories.')
            return []
        return repos


def retrieve_commits(user_id, repository):

    repo_commits = requests.get('https://api.github.com/repos/' + user_id + '/' + repository + 'commits')
    pushTo_json = json.loads(repo_commits.text)

    return len(pushTo_json)


def main():

    user_id = input("Please input a GitHub username:")

    repos = get_repos(user_id)

    if len(repos) > 0:
       for i in repos:
            print("Repository: " + repos + "Number of Commits: " + str(retrieve_commits(user_id, repos)))