import re


def match_regex(filename, regex):
	with open(filename) as file:
		lines = file.readlines()
	for line in lines:
		match = re.match(regex, line.strip())
		if(match):
			regex = yield match.groups()

def get_contents(filename):
	start_tag = '^<([^/]*)>([\s\w]*)?(</\w*>)?$'
	matcher = match_regex(filename, start_tag)
	tag = next(matcher)
	while True:
		yield tag
		tag = matcher.send(start_tag)
		# print(tag)

for tag in get_contents('simple.xml'):
	if(tag[1]):
		print(tag[0] + ': ' + tag[1])
	else:
		print(tag[0])
