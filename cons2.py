# cons

#!/usr/bin/env python

from util import read_input

# if we had a FASTA file, how would we get id-sequencde pairs?
fasta = read_input('./rosalind_data/rosalind_cons.txt')

sequences = []
current_id = ""
current_seq = ''
for line in fasta:
    if line[0] == ">":
        if current_seq != '':
            sequences.append(current_seq)
            current_seq = ''
        continue
    else:
        current_seq += (line.strip()) # makes a string containing just the sequences from the fasta file

sequences.append(current_seq)
# print(len(sequences))

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
    # print(seq)
    for i, base in enumerate(seq): # enumerate(seq) provides both the index (i) and the character (base) of each nucleotide in the sequence, 
        # print(i)
        profile[base][i] += 1 # like if seq = "ATCCAGCT": (0, 'A'), (1, 'T'), (2, 'C')...

# print(profile)


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
# Print the profile matrix
for nucleotide, counts in profile.items():
    print(f"{nucleotide}: {' '.join(map(str, counts))}") # map(str, counts) converts each number in the counts list to a string, so it can be joined for printing.