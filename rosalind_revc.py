s = "AAAACCCGGT"

def complement(x):
    if x == "A":
        return "T"
    elif x == "C":
        return "G"
    elif x == "G":
        return "C"
    elif x == "T":
        return "A"

comp = ""
for base in s:
    comp = comp + complement(base)

print(comp)

new_comp = comp[::-1]
print(new_comp)