#!/usr/bin/env python

# check if a sequence (seq1) contains the four nt of interest by comparing 4 consecutive nt of the long sequence with the sequence of interest (seqf)
# do it in a for loop
# access the nts in seq1 with [i]. the following nt should be [nt+1] and so on
# nts in seqf are accessed in the same way
# add only the first nt [i] to a list (start)
# convert it to a string, remove brackets and replace comma with a space

from util import read_input

line_list = read_input("./rosalind_data/rosalind_subs.txt")
seq1 = line_list[0]
seqf = line_list[1]

# test seq1 = "GATATATGCATATACTT"
# test seqf = "ATAT"

start = []
for i in range(len(seq1)):
    if seq1[i] == seqf[0] and seq1[i+1] == seqf[1] and seq1[i+2] == seqf[2] and seq1[i+3] == seqf[3]:
        # print(i, i+1, i+2, i+3)
        # print(f"In Python notation: [{i}, {i+3}]")
        # print(f"In Rosalind notation: [{i+1}, {i+4}]")
        # print("---")
        # print(i+1)
        start.append(i+1)
print(start)
result=str(start)
result = result.strip("[]") # remove brackets
result = result.replace(",", "") # exchange comma

print(result)