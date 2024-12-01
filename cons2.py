# cons

#!/usr/bin/env python

from util import read_input

# if we had a FASTA file, how would we get id-sequencde pairs?
fasta = read_input('./rosalind_data/cons_test.txt')

sequences = []
current_id = ""
for line in fasta:
    if line[0] == ">":
        continue
    else:
        sequences.append(line.strip()) # makes a list containing just the sequences from the fasta file
# print(sequences)


# Each nucleotide (A, C, G, T) has a list for counts at each position
n = len(sequences[0])  # Length of each DNA string
profile = {
    'A': [0] * n,
    'C': [0] * n,
    'G': [0] * n,
    'T': [0] * n
}


# Populate the profile matrix by iterating through the sequences
for seq in sequences:
    for i, base in enumerate(seq): # enumerate(seq) provides both the index (i) and the character (base) of each nucleotide in the sequence, 
        profile[base][i] += 1 # like if seq = "ATCCAGCT": (0, 'A'), (1, 'T'), (2, 'C')...

# print(profile)

# Print the profile matrix
for nucleotide, counts in profile.items():
    print(f"{nucleotide}: {' '.join(map(str, counts))}") # map(str, counts) converts each number in the counts list to a string, so it can be joined for printing.

consensus_seq = ""

# Iterate through each column in the profile matrix
seq_length = len(profile['A'])  # Number of positions in the sequences
for i in range(seq_length):
    max_value = 0
    max_base = ""
    for base, counts in profile.items():
        current_value = counts[i]  # Get the count for the current base at position i
        if current_value > max_value:  # Compare with the current max
            max_value = current_value
            max_base = base
    consensus_seq += max_base  # Add the nucleotide with the highest count to the consensus string

# Print the consensus string
print(consensus_seq)