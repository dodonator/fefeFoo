import os
# os.system('')
commitMessage = raw_input('CommitMessage: \n')
os.system('git add --all')
os.system('git commit -a -m "' + commitMessage + '"')
os.system('git push')
os.system('clear')