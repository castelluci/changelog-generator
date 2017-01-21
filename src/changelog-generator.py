import os
import sys
import err
import git
import chlgprsr
import chlgwrtr

if not sys.argv or len(sys.argv) < 4:
	err.printe('This program syntax is : \n' +
				'\tchangelog-generator.py <PATH_TO_PROJECT> <DEVELOP_BRANCH_NAME> <RELEASE_BRANCH_NAME>')
	exit('0001')
elif not os.path.isdir(sys.argv[1]):
	err.printe('The project path does not exists or contains a typo error. Please double check first argument')
	exit('0002')

CHANGELOG_FILE_NAME = 'CHANGELOG.md'
PROJECT_ROOT_DIR = sys.argv[1]
DEVELOP_BRANCH_NAME = sys.argv[2]
RELEASE_BRANCH_NAME = sys.argv[3]

def get_changelog_path():
	if PROJECT_ROOT_DIR[1:] == '/':
		changelog_path = PROJECT_ROOT_DIR + CHANGELOG_FILE_NAME
	else:
		changelog_path = PROJECT_ROOT_DIR + '/' + CHANGELOG_FILE_NAME
	return changelog_path

changelog_path = get_changelog_path()
with open(changelog_path, 'a+') as file :
	file.seek(0)
	content = file.readlines()

try:
	git_log = git.get_log(DEVELOP_BRANCH_NAME, RELEASE_BRANCH_NAME);
except git.FatalGitSubProcessError as error:
	err.printe('The git subprocess failed to execute\n', error.message)
	exit(str(error.returncode))

chlgwrtr.write(changelog_path, content, list(set(git_log)))

exit('0')