"""
@author Michayla Ben-Ezra
September 23, 2018
SSW567 - HW04

I pledge my honor that I have abided by the Stevens Honor System.
"""

import unittest
from githubAPI import get_repos, retrieve_commits


class TestGitHubAPI(unittest.TestCase):

    def test_1_Repo(self):
        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 4, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)

    def test_2_Repo(self):
        repos = get_repos('Mbenezra18')
        self.assertGreaterEqual(len(repos), 5, "User 'Mbenezra18' has 5 repositories")
        self.assertIn('SSW215', repos)
        self.assertIn('SSW-567', repos)
        self.assertIn('Triangle-SSW567', repos)
        self.assertIn('python-gedcom', repos)
        self.assertIn('567githubAPI', repos)

    def test_3_Commits(self):
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', 'SSW215'), 1)

    def test_4_Commits(self):
        self.assertGreaterEqual(retrieve_commits('richkempinski', 'threads_of_life'), 1)

    def test_5_invalid_user(self):
        self.assertEqual(get_repos("aervnoDNJsdvn"), [])
        self.assertEqual(get_repos("awnonebjnivk a"), [])
        self.assertEqual(get_repos("svnsna egv n "), [])
