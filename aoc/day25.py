#!/usr/bin/env python
# day 25 aoc

from util import read_input
input_data = read_input('../aoc_data/day25.txt')

input_data_str = "\n".join(input_data) #convert it into string

# Function to calculate the vertical sum of `#` in a block
def vertical_sum(block, skip_first=False, skip_last=False):
    lines = block.split("\n")
    
    # Skip the first or last row if needed
    if skip_first:
        lines = lines[1:]  # Exclude the first row
    if skip_last:
        lines = lines[:-1]  # Exclude the last row
#Lines After Splitting:
# lines = [".####", ".####", ".#.#.", ".#...", "....."]
    # Transpose the grid and count `#` in each column
    sums = [sum(1 for row in lines if row[i] == "#") for i in range(len(lines[0]))]
    return sums
#in the example above (lines) it would sum to 4. if row is "#" then
#it counts it as 1. it goes over all "" which are called rows and
# checks for "#"

# Function to compare locks and keys and count valid lock-key pairs
def compare_locks_keys_all_columns(lock_sums, key_sums):
    valid_pair_count = 0  # Counter for valid lock-key pairs

    # Compare each lock with each key
    for lock in lock_sums:
        for key in key_sums:
            # Check if all columns in the lock and key comparison satisfy the condition
            if all(lock[i] + key[i] < 6 for i in range(len(lock))):
                valid_pair_count += 1  # Increment count if all columns are valid

    return valid_pair_count

# Step 1: Split input into blocks based on empty lines
blocks = input_data_str.strip().split("\n\n")
# it looks like this now:
# [
#     "#####\n.####\n.####\n.####\n.#.#.\n.#...\n.....",
#     "#####\n##.##\n.#.##\n...##\n...#.\n...#.\n.....",
#     ".....\n#....\n#....\n#...#\n#.#.#\n#.###\n#####",
#     ".....\n.....\n#.#..\n###..\n###.#\n###.#\n#####",
#     ".....\n.....\n.....\n#....\n#.#..\n#.#.#\n#####"
# ]

# Step 2: Classify each block as a lock or key
locks = []
keys = []

for block in blocks:
    lines = block.split("\n")  # Split block into lines
    if lines[0] == "#####":  # This is a lock
        locks.append(block)
    if lines[-1] == "#####":  # This is a key
        keys.append(block)

# Output the results
# print("Locks:")
# for lock in locks:
#     print(lock)
#     print("---")

# print("Keys:")
# for key in keys:
#     print(key)
#     print("---")

# Compute vertical sums for locks and keys
lock_sums = [vertical_sum(lock, skip_first=True) for lock in locks]
key_sums = [vertical_sum(key, skip_last=True) for key in keys]
# print(lock_sums)
# print(key_sums)

valid_pairs = compare_locks_keys_all_columns(lock_sums, key_sums)

# Output results
print("Lock Sums:")
for idx, sums in enumerate(lock_sums, start=1):
    print(f"Lock {idx}: {sums}")

print("\nKey Sums:")
for idx, sums in enumerate(key_sums, start=1):
    print(f"Key {idx}: {sums}")

print(f"\nTotal valid lock-key pairs where all columns satisfy lock[i] + key[i] < 6: {valid_pairs}")