#!/usr/bin/env python
# Advent of Code day 3

from util import read_input

# first, read the raw data
raw = read_input("../aoc_data/day03_test.txt")
# print(len(raw))
# print(len(raw[0]))
# print(raw)

total_xmas = 0
for line in raw:
    total_xmas += line.count("XMAS")
    total_xmas += line[::-1].count("XMAS")

print(total_xmas)

length = len(raw[0])
print(length)

# raw = raw[::-1]
# for line in raw:
#     print(line)

def diag_down (x,y):
    diagonal = []
    x_c=x
    y_c=y
    for x_c in range(len(raw[0])):
        diagonal.append([x_c, y_c])
        x_c += 1
        y_c += 1
    return diagonal

# print("===================")

matrix = [list(row) for row in raw]

# print(matrix)

# Transpose the matrix
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Perform any specific transformations if needed
# (e.g., modifying certain elements or rows)

# Convert back to strings
transposed_strings = [''.join(row) for row in transposed]

def diag_side (x,y):
    diagonal = []
    x_c=x
    y_c=y
    for x_c in range(len(transposed_strings[0])):
        diagonal.append([x_c, y_c])
        x_c += 1
        y_c += 1
    return diagonal


# Print the transposed grid
print("Transposed Grid:")
for row in transposed_strings:
    print(row)

total_xmas2 = 0
for line in transposed_strings:
    total_xmas2 += line.count("XMAS")
    total_xmas2 += line[::-1].count("XMAS")

print(total_xmas2)

# 
# or
# SAMX