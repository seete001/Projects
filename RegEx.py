import re


with open("/Users/sepehretemadi/Desktop/combined.txt", "r") as f:
    lines = f.read()

#print(lines)

digitPattern = r"\d+"
matches = re.findall(digitPattern, lines)
#print(matches)

namePattern = r"S\w+"
matches_2=re.finditer(namePattern, lines)
for match in matches_2:
    print(match.group())