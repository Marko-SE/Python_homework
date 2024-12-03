#!/usr/bin/env python

# chief historian's office; comparing reports
from util import read_input

# first, read the raw data
raw = read_input("../aoc_data/day01_data.txt")
list_a = []
list_b = []
for line in raw:
    tmp = line.split(' ')
    a = int(tmp[0])
    b = int(tmp[-1])
    list_a.append(a)
    list_b.append(b)

# print(list_a)
# print(list_b)

# now we need to sort the lists
list_a.sort()
list_b.sort()
# print(list_a)

# calculate differences!
sum_of_differences = 0
for a, b in zip(list_a, list_b):
    diff = abs(a - b)
    sum_of_differences += diff

print(sum_of_differences)

# for a in list_a:
#     count = 0
#     for b in list_b:
#         if a == b:
#             count +=1
#     print(a, count)

def count_occurences(x, l):
    counter = 0
    for number in l:
        if x == number:
            counter += 1
    return counter

res = 0 
for a in list_a:
    occ_a = count_occurences(a, list_b)
    res += a * occ_a

print(res)
