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

def complement_sequence(seq):
    comp = ""
    for base in seq:
        comp = comp + complement(base)
    return comp

def reverse_complement(seq):
    return complement_sequence(seq[::-1])

print(reverse_complement(s))