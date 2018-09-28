import sys

inname, outname = sys.argv[1:3]

def errors_filter(infilename):
	with open(infilename) as infile:
		yield from (
			l for l in infile if 'ERROR' in l
			)


filter = errors_filter(inname)

with open(outname, 'w') as outfile:
	for l in filter:
		outfile.write(l)