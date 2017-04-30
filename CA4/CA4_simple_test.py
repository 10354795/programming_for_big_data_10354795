import unittest

from CA4_simple import get_authors, get_commits, get_number_of_1_comment_lines, get_number_of_4_comment_lines, read_file

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

    def test_count_comments_with_1_line(self):
        commits = get_commits(self.data)
        self.assertEqual(348, get_number_of_1_comment_lines(commits))
#        print ("*** The count of 1 comment lines is ", get_number_of_1_comment_lines(commits))
 
    def test_count_comments_with_4_lines(self):
        commits = get_commits(self.data)
        self.assertEqual(7, get_number_of_4_comment_lines(commits))
#        print ("*** The count of 4 comment lines is ", get_number_of_4_comment_lines(commits))
     

if __name__ == '__main__':
    unittest.main()