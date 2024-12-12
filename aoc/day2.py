#!/usr/bin/env python
# Advent of Code day 2

# chief historian's office; comparing reports
from util import read_input

# first, read the raw data
raw = read_input("../aoc_data/day02_data.txt")
# print(raw)
# no_space = raw.replace(" ", "")

processed = [list(map(int, item.split())) for item in raw] #splits each row into list of integers
print(f"Processed data: {processed}")

def ascending(row):
    return all(row[i] < row[i+1] for i in range(len(row) - 1)) # check whether all adjacent elements in the list row satisfy a certain condition

def descending(row):
    return all(row[i] > row[i+1] for i in range(len(row) - 1))

def is_monotonic(row):
    return ascending(row) or descending(row)

# def is_safe(row):
#     # Check the differences between adjacent elements
#     for i in range(len(row) - 1):
#         diff = abs(row[i] - row[i+1])
#         if diff < 1 or diff > 3:
#             return False
        
    # Check if the row is monotonic
    # return is_monotonic(row)

def is_safe(row):
    # Check the differences between adjacent elements
    for i in range(len(row) - 1):
        diff = abs(row[i] - row[i+1])
        if diff < 1 or diff > 3:
            return False
    # Check monotonicity
    return is_monotonic(row)

def can_become_safe(row):
    for i in range(len(row)):
        # Create a copy of the row with one element removed
        modified_row = row[:i] + row[i+1:]
        if is_safe(modified_row):
            return True
    return False

# Count and print safe rows
safe_count = 0
for row in processed:
    if is_safe(row):
        safe_count += 1
        print(f"Safe: {row}")
    elif can_become_safe(row):
        safe_count += 1
        print(f"Safe (after dampener): {row}")
    else:
        print(f"Unsafe: {row}")

print(f"Number of safe rows: {safe_count}")

# for row in processed:
#     if is_safe(row):
#         continue
#     else:


# def not_fluctiating(num, list):
#     for i in num:
#         for lis in list:
#             if abs(lis[i] - lis[i+1]) == 1 or abs(lis[i] - lis[i+1]) == 2 or abs(lis[i] - lis[i+1]) == 3:
#                 return "still safe"

#write 3 functions: if its fluctuatin, if its ascending, if its descending