#!python3
from __future__ import print_function
import os
import sys
import subprocess

def printerr(*args, **kwargs):
	print('\n########## ERROR ##########', file=sys.stderr)
	print(*args, file=sys.stderr, **kwargs)
	print('###########################\n', file=sys.stderr)

if not sys.argv or len(sys.argv) < 3 :
	printerr('This program syntax is : \n' +
				'\tchangelog-generator.py <PATH_TO_PROJECT> <RELEASE_BRANCH_NAME>')
	exit('0001')
elif not os.path.isdir(sys.argv[1]) :
	printerr('The project path does not exists or contains a typo error. Please double check first argument')
	exit('0002')

CHANGELOG_FILE_NAME = 'CHANGELOG.md'
PROJECT_ROOT_DIR = sys.argv[1]
RELEASE_BRANCH_NAME = sys.argv[2]
PIPE = subprocess.PIPE

def get_changelog_path() :
	if PROJECT_ROOT_DIR[1:] == '/' :
		changelog_path = PROJECT_ROOT_DIR + CHANGELOG_FILE_NAME
	else :
		changelog_path = PROJECT_ROOT_DIR + '/' + CHANGELOG_FILE_NAME
	return changelog_path

file = open(get_changelog_path(), 'a+')
file.write('')
file.close()
exit('0')