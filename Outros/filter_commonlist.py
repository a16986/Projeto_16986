#!/usr/bin/env python3

import re
import sys

def remove_accents(a):
    a = re.sub(u"[àáâãäå]", 'a', a)
    a = re.sub(u"[èéêë]", 'e', a)
    a = re.sub(u"[ìíîï]", 'i', a)
    a = re.sub(u"[òóôõö]", 'o', a)
    a = re.sub(u"[ùúûü]", 'u', a)
    a = re.sub(u"[ýÿ]", 'y', a)
    a = re.sub(u"[ß]", 'ss', a)
    a = re.sub(u"[ñ]", 'n', a)
    return a


with open(sys.argv[1], "r") as outfile:
	old_content = outfile.readlines()

new_contents = []

pattern = r" {0,6}[0-9]{1,8}	"

for line in old_content:
    new_contents.append(re.sub(pattern, "", line))

for line in new_contents:
    line = remove_accents(line)


new_contents = set(new_contents)

with open("filtered_words.txt", "w") as f:
	for line in new_contents:
		f.write(line)
		