#!/bin/env python3

import os
import sys
import re
from collections import Counter

if not len(sys.argv) > 1:
	print("Usage : " + sys.argv[0] + " filename.txt [min_length]\nmin_length is optional ; default = 2")
	sys.exit()

if not os.path.isfile(sys.argv[1]):
	print("Error while opening file " + sys.argv[1])
	sys.exit()

file = open(sys.argv[1], 'r')

content, lines = [], file.read().split()
if len(sys.argv) == 3 and int(sys.argv[2]) > 0:	min_length = int(sys.argv[2])
else:	min_length = 2

for key, value in enumerate(lines):
	if value=='':
		del lines[key] # if empty line, delete it
	else:
		array = re.sub('[^\w-]', ' ', "".join(lines[key].split()).lower()).split() # filter on any non-alphanumerical char
		
		for i in array:
			if re.match("^.{0," + str(min_length-1) + "}$", i) is None and re.match("^[0-9]+$", i) is None:
				content.append(i)

dic = Counter(content)

print("Words found : " + str(len(dic)))

ctr=1
for key,value in dic.most_common():
	print("#" + str(ctr) + " " + key + " (" + str(value) + ")")
	ctr += 1
