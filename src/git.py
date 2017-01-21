import subprocess

PIPE = subprocess.PIPE

class FatalGitSubProcessError(Exception):
	def __init__(self, message):
		self.returncode = 1002
		self.message = message


def get_log(origin_branch, target_branch):
	process = subprocess.Popen(['git', 'log', target_branch + '..' + origin_branch, '--no-merges', '--pretty=format:%s'], stdout=PIPE, stderr=PIPE)
	stdoutput, stderroutput = process.communicate()

	stdoutput = stdoutput.decode('utf-8')

	if 'fatal' in stdoutput:
		raise FatalGitSubProcessError(message = stdoutput)
	elif 'fatal' in str(stderroutput):
		raise FatalGitSubProcessError(message = stderroutput.decode('utf-8'))
	else:
		formatted_output = stdoutput.split('\n')
		return formatted_output
