
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
#    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[0],
                'changes': data[index+2:data.index('',index+1)],
                'comment' : data[data.index(sep, index + 1) - int(details[3].strip().split(' ')[0]) : data.index(sep, index + 1)]
                }
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits

def get_authors(commits):
    authors = {}
    for commit in commits:
        author = commit['author']
        if author not in authors:
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1
    return authors

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.txt'
    data = read_file(changes_file)
    commits = get_commits(data)

    # print the number of lines read
    print(len(data))
    #print(commits)
    print(commits[11])
#    print(commits[2]['author'])
    print(len(commits))