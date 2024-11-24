#!/usr/bin/env python

# slice the file, have lines in 2 rows
# assign first line [0] to line1 and second line [1] to line2
# measure length of a line with range(len(strin1))
# compare each nt of one string to the other and if != then add +1 to count= 0


from util import read_input

line_list = read_input("./rosalind_data/rosalind_hamm.txt")
line1 = line_list[0]
line2 = line_list[1]
# print(line1)
# print(line2)

count = 0
for i in range(len(line1)):
    if line1[i] != line2[i]:
        count += 1

print(count)
