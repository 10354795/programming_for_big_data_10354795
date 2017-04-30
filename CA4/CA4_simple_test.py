import unittest

from CA4_simple import get_authors, get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_number_of_authors(self):
        commits = get_commits(self.data)
        authors = get_authors(commits)
        print authors
        self.assertEqual(10, len(authors))
        self.assertEqual(191, authors['Thomas'])

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])

if __name__ == '__main__':
    unittest.main()