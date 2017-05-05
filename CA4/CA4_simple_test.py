# Thomas O'Brien ID 10354795

# Program to test the funtions that extracts data from a log file of support calls.


import unittest

# import the funtions from the commits program in CA4_simple.py

from CA4_simple import get_authors, get_commits, get_number_of_1_comment_lines, get_number_of_4_comment_lines, read_file

class TestCommits(unittest.TestCase):       # instantiate the test class and call test cases.

# Read the log file into varaible called self.data in memory
                 
    def setUp(self):
        self.data = read_file('changes_python.txt')
  
# Test that the log file has 5255 lines
      
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))     

# Test that there are 422 service calls (commits) identified in the log file

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

# Test that there are 10 authors in the log file and that Thomas handles 191 calls.

    def test_number_of_authors(self):
        commits = get_commits(self.data)
        authors = get_authors(commits)
        print authors
        self.assertEqual(10, len(authors))
        self.assertEqual(191, authors['Thomas'])

# Test that Vincent is the author of index 10 and the revision code is r1551332 

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Vincent', commits[10]['author'])
        self.assertEqual('r1551332', commits[10]['revision'])

#Test that the count commits with 1 comment line is 348

    def test_count_comments_with_1_line(self):
        commits = get_commits(self.data)
        self.assertEqual(348, get_number_of_1_comment_lines(commits))

#Test that the count of commits with 4 comment lines is 7 

    def test_count_comments_with_4_lines(self):
        commits = get_commits(self.data)
        self.assertEqual(7, get_number_of_4_comment_lines(commits))
     

if __name__ == '__main__':
    unittest.main()