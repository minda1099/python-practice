import sys

inname, outname = sys.argv[1:3]

with open(inname) as infile:
	with open(outname, 'w') as outfile:
		errors = ( l for l in infile if 'ERROR' in l )
		for l in errors:
			outfile.write(l)