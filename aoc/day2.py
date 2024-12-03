#!/usr/bin/env python
# Advent of Code day 2

# chief historian's office; comparing reports
from util import read_input

# first, read the raw data
raw = read_input("../aoc_data/day02_test.txt")
print(raw)
# no_space = raw.replace(" ", "")
processed = []
for item in raw:
    processed.append(item.replace(" ", ""))
print(processed)

length = len(processed[0])
print(length)

for list in processed:
    for number in list:

# write 3 functions: if its fluctuatin, if its ascending, if its descending
