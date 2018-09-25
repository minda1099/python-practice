import sys
from PIL import Image
from pathlib import Path

def process_files( dir, x, y):
	for filename in Path(dir).iterdir():
		im = Image.open(str(filename))
		scaled = im.resize((int(x), int(y)))
		scaled.save(str(filename))

process_files(sys.argv[1], sys.argv[2], sys.argv[3])
