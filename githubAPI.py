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
    repos_info = json.loads(r.text)

    repos = []

    for i in repos_info:
        try:
            repos += [i.get('name')]
        except AttributeError:
            print('Error: Could not locate any repositories for this user.')
            return []
    return repos


def retrieve_commits(user_id, repository):

    repo_commits = requests.get('https://api.github.com/repos/' + user_id + '/' + repository + '/commits')
    push_to_json = json.loads(repo_commits.text)

    return len(push_to_json)


def main():

    user_id = input("Please input a GitHub username: ")
    print("Username: " + user_id)
    repositories = get_repos(user_id)

    for repos in repositories:
            print("Repository: " + repos + "Number of Commits: " + str(retrieve_commits(user_id, repos)))


if __name__ == "__main__":
    main()
