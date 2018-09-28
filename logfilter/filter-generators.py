import sys

inname, outname = sys.argv[1:3]

def errors_filter(log):
	for l in log:
		if 'ERROR' in l:
			yield l

with open(inname) as infile:
	with open(outname, 'w') as outfile:
		filter = errors_filter(infile)
		for l in filter:
			outfile.write(l)