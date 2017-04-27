
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

# open file and strip off the /n from the end of the line.
# Read all 5522 lines into a variable called data

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

# Create variable called sep that has 72 hyphens in it

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'

# create public member variable not private member variabls as this avoids having to create Setters and getters.	
 
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)


# Test to see if class Commit is working 
#a_commit =Commit('r1551925', 'Thomas', '2015-15-01', 1, comment = 'Rename folder')
#print a_commit.author
#print a_commit.revision				
#print a_commit.comment			
#print a_commit.changes   # Prints none as no value entered	
				
commits = []  # set up an array to capture commits
current_commit = None
index = 0

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()    # use class Commit here with parameters value = none
        details = data[index + 1].split('|')   # details is a variable to capture values in loop. split line at each character "|". Index is line no starting at zero as python counter
		# details is a temporary variable to capture the values at each split of the "|" symbol
        current_commit.revision = int(details[0].strip().strip('r')) # index strips spaces and r from revision number
        current_commit.author = details[1].strip()  # strips spaces
        current_commit.date = details[2].strip() 
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])   # strip blank spaces
        current_commit.changes = data[index+2:data.index('',index+1)]   # split at line that has blank space
        #print(current_commit.changes)
        index = data.index(sep, index + 1)  # find the line that has the line of hyphens using "sep"
        current_commit.comment = data[index-current_commit.comment_line_count:index] # Selects comment from index - count of lines that comment is above the "sep" hyphen characters
        commits.append(current_commit)
    except IndexError:      # you could say except: to trap all errors, but the liklihood is that it fails with an index error
        break

print(len(commits))

#commits.reverse()

#for index, commit in enumerate(commits):
#    print(commit.get_commit_comment())
