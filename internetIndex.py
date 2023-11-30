import glob
import json
import os

files = glob.glob("**/**", recursive=True)
files = [file for file in files if file not in ["internetIndex.py", "index.json"]]
files = [os.path.normpath(file).replace("\\", "/") for file in files]

print(files)

index = {}
for file in files:
	file = file.strip("/")
	if file in index:
		continue
	index[file] = {
		"d": os.path.isdir(file),
		"e": os.path.getmtime(file),
		"c": os.path.getctime(file),
		"s": os.path.getsize(file),
	}

print(index)

with open("index.json", "w") as w:
	json.dump(index, w, separators=(',', ':'))