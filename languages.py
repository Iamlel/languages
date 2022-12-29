import json, sys, os
from itertools import islice

HELP_MESSAGE = (
        "Usage:",
        "python size.py <directory>",
        "python size.py <directory> ignore:<language names seperated by commas>",
        "",
        "Example",
        "python size.py aoc2022",
        "python size.py aoc2022 ignore:Text,D,Assembly",
        ""
        )

match len(sys.argv):
    case 1:
        exit('\n'.join(HELP_MESSAGE) + "\nPlease include the directory!\n")

    case 2:
        ignores = []

    case 3:
        try:
            ignores = sys.argv[2].split(':')[1].split(',')
        except:
            exit('\n'.join(HELP_MESSAGE))

    case other:
        exit('\n'.join(HELP_MESSAGE))

fdir = sys.argv[1]
if not os.path.isdir(fdir):
    exit('\n'.join(HELP_MESSAGE) + "\nInclude a valid directory!\n")

if not os.path.isfile("langs.json"):
    exit('\n'.join(HELP_MESSAGE) + "\nCan't find langs.json!\n")

PERCENTAGE_CHAR = "▇"
data = {}
total = 0

with open("langs.json", "r") as f:
    langs = json.load(f)

if len(sys.argv) > 2:
    ignores = sys.argv[2].split(':')[1].split(',')
else:
    ignores = []

for subdir, dirs, files in os.walk(fdir):
    for file in files:
        if file.split('.')[-1] in langs:
            lang = langs[file.split('.')[-1]]
            size = os.path.getsize(os.path.join(subdir, file))

            if not lang in ignores:
                total += size
                if lang in data:
                    data[lang] += size
                else:
                    data[lang] = size

data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

print(f"\nDirectory {sys.argv[1]}")
for x, (k, v) in enumerate(data.items(), 1):
    print(f"{x}. {k}: {round(v / total * 100, 3)}% | {v} bytes")

print("\n--Keys--")
for x, k in enumerate(islice(data.keys(), 9), 0):
    print(f"{k}: \u001b[3{x}m{PERCENTAGE_CHAR}\u001b[0m")

print("\nPercentage: [", end="")
for x, v in enumerate(islice(data.values(), 9), 0):
    print(f"\u001b[3{x}m", end="")
    print(PERCENTAGE_CHAR * round(v / total * 100), end="")
    print("\u001b[0m", end="")
print("]\n")
