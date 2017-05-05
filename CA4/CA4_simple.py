# Thomas O'Brien ID 10354795

# Program to extract data from a log of support calls and analyse the activites involved.

# Define function to read in file and strip out spaces and trim end of line characters.
# Save the information into a file called data.

def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

# Define function to extract the required data from the log (text) file

def get_commits(data):
    sep = 72*'-'          # Create a variable (sep) to use in identifying the separators between support calls (line of 72 hyphens)
    commits = []          # Set up list to store the extracted data.
    index = 0             # initialise index counter to zero to start counting lines in the log file
    while index < len(data):      # Loop through the data until you reach the number of lines in the data
        try:                      # Use try except to protect failure of program if index errors occur
#
            details = data[index + 1].split('|')        # Split the first four elements of the support calls using "|" character to separate the elements and put them into a list called commits
            commit = {'revision': details[0].strip(),   # strip and save the zero'th element as "revision" in the list 
                'author': details[1].strip(),           # Strip and save the 2nd element as name as the 
                'date': details[2].strip(),             # Strip and save the 3rd element as date
                'number_of_lines': details[3].strip().split(' ')[0],    # Split the 4th element to remove word "line" and strip spaces. This indicates the number of lines in the comment at end of the support cal text 
                'changes': data[index+2:data.index('',index+1)],        # Split out the changes starting on the second line (index +1) and continue until you reach a blank (empty) line.
#
# The following line splits out the comments.
# It finds the separator (hyphens) line (sep) and then counts back by the number of comments lines ('number_of_lines') in the support call to identfy the comments.
# It then extracts the comments from that line forward to separator line.
#
                'comment' : data[data.index(sep, index + 1) - int(details[3].strip().split(' ')[0]) : data.index(sep, index + 1)]
                }
            commits.append(commit)              # Append all the elements to the list (commits)
            index = data.index(sep, index + 1)  # increment the index to the next support call (index line) based on the location of the separator line
        except IndexError:
            break
    return commits         # Returns the list of data in the commits list when it reaches the end of the file.

# The following function counts the number of calls that each author (help desk agents) performs. 

def get_authors(commits):
    authors = {}            # initialise list to identify and count entries for each author.
    for commit in commits:
        author = commit['author']   # loop through commits list and identify each author 
        if author in authors:       # if the author already exists in authors list, increment the counter by 1.
            authors[author] = authors[author] + 1
        else:                       
            authors[author] = 1     # if the author does not exist in authors list, initialise the count to 1.

    return authors                  # return list of authors and the count of their occurance in the file.

# The following functions counts the number of help desk cals that have 1 comment line at the end of the call
# It is used for test purposes.
#
def get_number_of_1_comment_lines(commits):
    comment_lines_1 = 0
    for commit in commits:
        if commit['number_of_lines'] == "1":
            comment_lines_1 = comment_lines_1 + 1
        else:
            continue
    return comment_lines_1

# The following functions counts the number of help desk cals that have 4 comment line at the end of the call
# It is used for test purposes
#
def get_number_of_4_comment_lines(commits):
    comment_lines_4 = 0
    for commit in commits:
        if commit['number_of_lines'] == "5":
            comment_lines_4 = comment_lines_4 + 1
        else:
            continue
    return comment_lines_4

# The following calls the funtions to run the program

if __name__ == '__main__':
#
    changes_file = 'changes_python.txt'     # open the file and read all of the lines.
    data = read_file(changes_file)          # This reads the information into a variable called data in meomory
    commits = get_commits(data)             # call the funtion to strip the data.

# Save data in the commits list to a CSV file for further processing.

    output = open("CA4_out.csv", 'w')
    index = 0
    for commit in commits:
        output.write(commits[index]['author'])        
        output.write(';')
        output.write(commits[index]['revision'])
        output.write(';')
        output.write(commits[index]['date'])
        output.write(';')
        output.write(commits[index]['number_of_lines'])
        output.write(';')
        output.write(str(commits[index]['comment']))  
        output.write(';')
        output.write(str(commits[index]['changes']))
        output.write('\n')
        index = index +1
    output.close()
    
                 
    print("")
    print("Below is the total number of lines in the log file and the number of helpdesk calls(commits)")
    print(len(data))        # print the number of lines read from the log file changes_python.txt
    print(len(commits))     # print the number of helpd desk calls (commits) in the log file
#    print("")
#    print(commits[10])      # does a sample print of the data in index 10 of the commits list
    print("")
    print("Below is a list of the help desk agents (authors) and the number of calls that they handle.")
    print (get_authors(commits))

#    print(commits[0]['comment'])
