#!/usr/bin/env python
# grph

from util import read_input
fasta = read_input('./rosalind_data/rosalind_grph.txt')

sequences = {}
current_id = ""
for line in fasta:
    if line[0] == ">":
        # print("This line is a header:")
        header = line
        # print(header)
        # this is a header
        # we only care about this header from now on
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        # print("this is a sequence:")
        sequence = line
        # print("we currently belong to sequence", current_id)
        # print(sequence)
        # it is a sequence
        sequences[current_id] = sequences[current_id] + sequence

print(sequences)

for key1, value1 in sequences.items():
    last = value1[-3:]  # Last 3 characters of the current sequence
    for key2, value2 in sequences.items():
        if key1 != key2:  # Ensure we're not comparing the sequence to itself
            first = value2[:3]  # First 3 characters of the other sequence
            if last == first:  # Compare the last 3 with the first 3
                print(key1, key2)