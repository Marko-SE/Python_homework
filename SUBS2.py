#!/usr/bin/env python

# check if a sequence (seq1) contains the nts of interest (seqf) by slicing seq1 from i to i + the lenght of seqf (sub_len) and comparing it to seqf
# add only the first nt [i] to a list (start)
# convert it to a string, remove brackets and replace comma with a space

from util import read_input

line_list = read_input("./rosalind_data/rosalind_subs.txt")
seq1 = line_list[0]
seqf = line_list[1]



# seq1 = "GATATATGCATATACTT" # test
# seqf = "ATAT" # test

sub_len = len(seqf)

start = []
for i in range(len(seq1)):
    if seq1[i:i+sub_len] == seqf:
        # print(i, i+1, i+2, i+3)
        # print(f"In Python notation: [{i}, {i+3}]")
        # print(f"In Rosalind notation: [{i+1}, {i+4}]")
        # print("---")
        # print(i+1)
        start.append(i+1) # + 1 for Rosalind notation
print(start)
result=str(start)
result = result.strip("[]") # remove brackets
result = result.replace(",", "") # exchange comma

print(result)