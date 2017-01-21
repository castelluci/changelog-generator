import os
import sys
import chlgprsr

def write_title(file):
	file.write('# CHANGELOG\n===========\n\n')

def write(changelog_path, content, unique_jira_list):
	print(content)
	with open(changelog_path, 'w+') as file:
		write_title(file)
		file.write(chlgprsr.format_release_line(content))
		for jira in unique_jira_list:
			file.write(chlgprsr.format(jira))
		for old_line in content[2:]:
			file.write(old_line)
	print(chlgprsr.format_build())
	print()
	print(chlgprsr.format_date())
	print([chlgprsr.format(x) for x in unique_jira_list])