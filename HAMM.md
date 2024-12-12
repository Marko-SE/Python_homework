#!/usr/bin/env python

# slice the file, have lines in 2 rows
# assign first line [0] to string 1 and second line [1] to string 2
# measure length of a line with range(len(strin1))
# compare each nt of one string to the other and if != then add +1 to count= 0
# do this by 3 for loops:


from util import read_input

line_list = read_input("./rosalind_data/HAMM_test.txt")
rna = line_list[0]

count = 0
for i in range(len(string1)):
    for nt1 in string1:
        for nt2 in string2:
            if nt1[i] != nt2[i]:
                count += 1

print(count)
