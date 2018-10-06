"""
@author: Michayla Ben-Ezra


"""
from githubAPI import get_repos, retrieve_commits
from unittest import mock
import unittest


class MockGitHubAPI(unittest.TestCase):

    @mock.patch('githubAPI.get_repos')
    def mock_get_repos_1(self, mock_repo_names):
        mock_repo_names.return_value = ['567-hw2a', 'SSW-567', 'python-gedcom', 'SSW-567', 'SSW215', 'Triangle-SSW567']

        repos = get_repos('Mbenezra18')
        self.assertGreaterEqual(len(repos), 5, "User 'Mbenezra18' has 6 repositories")
        self.assertIn('SSW215', repos)
        self.assertIn('SSW-567', repos)
        self.assertIn('Triangle-SSW567', repos)
        self.assertIn('python-gedcom', repos)
        self.assertIn('567githubAPI', repos)

    @mock.patch('githubAPI.get_repos')
    def mock_get_repos_2(self, mock_repo_names):
        mock_repo_names.return_value = ['567-hw2a', 'SSW-567', 'python-gedcom', 'SSW-567', 'SSW215', 'Triangle-SSW567']

        repos = get_repos('richkempinski')
        self.assertGreaterEqual(len(repos), 5, "User 'richkempinski' has 4 repositories")
        self.assertIn('hellogitworld', repos)
        self.assertIn('helloworld', repos)
        self.assertIn('Project1', repos)
        self.assertIn('threads-of-life', repos)

    @mock.patch('githubAPI.retrieve_commits')
    def mock_retrieve_commits(self, mock_repo_commits):
        mock_repo_commits.return_value = 12
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', '567-hw2a'), 12)
        mock_repo_commits.return_value = 24
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', '567githubAPI'), 24)
        mock_repo_commits.return_value = 30
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', 'python-gedcom'), 30)
        mock_repo_commits.return_value = 5
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', 'SSW-567'), 5)
        mock_repo_commits.return_value = 1
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', 'SSW215'), 1)
        mock_repo_commits.return_value = 13
        self.assertGreaterEqual(retrieve_commits('Mbenezra18', 'Triangle-SSW567'), 13)

    @mock.patch('githubAPI.get_repos')
    def mock_invalid_user(self, mock_repo_name):
        mock_repo_name.return_value = []
        repos = get_repos('sdvnjnWfassvav')
        self.assertEqual(len(repos), 0, "Error: Invalid Username")


if __name__ == '__main__':
    print("Unit Test: Start")
    unittest.main()
