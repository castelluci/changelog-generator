import datetime
import re

# Get unique build time
now = datetime.datetime.now()
# Get the version line pattern in CHANGELOG.md file
version_line_patten = re.compile('.+Release\s*(\d+\.\d+\.\d+\w?)\W*.*')
# Get the version pattern
version_patten = re.compile('(\d+\.\d+\.)\d+(\w?)')

def format_date():
	"""Return the date of the build as of YYYY-MM-DD"""
	return '%d-%02d-%02d' %(now.year, now.month, now.day)

def format_version(current_version):
	"""Return the next version of the release according to previous version or date of build"""
	supposed_ver = '%d.%d.%d' %(now.year % 100, now.month - 1, now.day)
	if supposed_ver in current_version :
		match = version_patten.match(current_version)
		fix_num = match.group(2)
		rest = match.group(1)
		if not fix_num:
			return supposed_ver + 'b'
		else:
			fix_num = chr(ord(fix_num) + 1)
			return supposed_ver + fix_num
	return supposed_ver

def format_build():
	"""Return the build number"""
	return '%04d%02d%02d%02d%02d%02d' %(now.year, now.month, now.day, now.hour, now.minute, now.second)

def get_lastest_version(content):
	"""Get the lastest version in a CHANGELOG.md"""
	for x in content:
		match = version_line_patten.match(x)
		if match:
			return match.group(1)
	return ''

def format(entry):
	"""Return the string representing an entry in the CHANGELOG.md file"""
	title, content = (entry.split(' - ')[0], ' - '.join(entry.split(' - ')[1:]))
	return '* _%s_ - %s\n' % (title, content)

def format_release_line(content):
	return '## %s : Release %s (build %s)\n' % (format_date(), format_version(get_lastest_version(content)), format_build())