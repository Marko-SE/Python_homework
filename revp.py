#!/usr/bin/env python
# Locating Restriction Sites

from util import read_input
from rosalind_revc import reverse_complement

sequence = read_input('./rosalind_data/rosalind_revp.txt')

dna_sequence = ""
current_id = ""
for line in sequence:
    if line[0] == ">":
        continue
    else:
        dna_sequence += line.strip()

print(dna_sequence)

dna_sequence_compl = reverse_complement(dna_sequence)
print(dna_sequence_compl)

# for i, j in zip(dna_sequence, dna_sequence_compl):
#     if dna_sequence[i] == dna_sequence_compl[j+1] and dna_sequence[i+1] == dna_sequence_compl[j-1]:
#         print(dna_sequence[i], dna_sequence_compl[j+1])

# for i in range(len(dna_sequence) - 1):  # Ensure no out-of-bound access
#     if dna_sequence[i] == dna_sequence_compl[i + 1] and dna_sequence[i + 1] == dna_sequence_compl[i - 1]:
#         print(f"Pattern found: {dna_sequence[i]} and {dna_sequence_compl[i + 1]}")

# complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

# # Compare the original DNA sequence with its reverse complement
# length = len(dna_sequence)
# for i in range(length):
#     # Calculate the corresponding index in the reverse complement
#     j = length - i - 1
#     base1 = dna_sequence[i]
#     base2 = dna_sequence_compl[j]
    
#     # Check if they are complementary
#     if complements[base1] == base2:
#         print(f"Complementary match at original index {i} and reverse index {j}: {base1} == {base2}")

# Function to find restriction sites
def find_restriction_sites(dna_sequence):
    results = []
    length = len(dna_sequence)

    # Iterate over all possible substrings of length 4 to 12
    for start in range(length):
        for size in range(4, 13):  # Palindromic sequences are typically 4-12 bases long
            end = start + size
            if end > length:
                break
            
            # Extract the substring
            substring = dna_sequence[start:end]
            
            # Compute the reverse complement of the substring
            reverse_comp = reverse_complement(substring)
            
            # Check if the substring is a palindrome
            if substring == reverse_comp:
                results.append((start + 1, size))  # +1 for 1-based indexing

    return results

# Find and print restriction sites
restriction_sites = find_restriction_sites(dna_sequence)
print(restriction_sites)
for site in restriction_sites:
    print(site[0], site[1])