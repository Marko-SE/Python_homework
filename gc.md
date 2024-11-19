~~~ python
s = >Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

# cut somehow (maybe split "\n") and put the DNA sequence together (maybe make a list out of it so that later the Nametag and the percentage can be put together by invoking their number)
# do 2 for loops (or one if we use len): one counts the total amount of nts and another one just the GC
# divide GC number with total and multiply by 100 to get in percent

s="CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

# b is total number of nts
b=0
for _ in s:
    b += 1

print(b)

c = 0
for a in s:
    if a == "G":
        c += 1

c = c * 2
# c is the number of GC in the DNA sequence
print (c)

~~~
