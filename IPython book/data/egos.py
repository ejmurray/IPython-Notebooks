import os
import sys

# retrieve the folder as the first argument to the command line callable

if len(sys.argv) > 1:
	folder = sys.argv[1]

# list all the files in the specified folder
files = os.listdir(folder)

# ids contain the sorted list of all uniquee identifiers
ids = sorted(set(map(lambda file: int(file.split('.')[0]), files)))
