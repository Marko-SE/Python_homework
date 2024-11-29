seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
start_seq = "AUG"

code = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}

# make a forward RNA strand:
forward_rna_s = ""

for base in seq:
    if base == "T":
        base = "U"
        forward_rna_s += base
    else:
        forward_rna_s += base

print(f"This is forward RNA strand {forward_rna_s}")

# make a backwards RNA strand:

back_rna = forward_rna_s[::-1]
print(f"test for backwards RNA {back_rna}")

                    # # make a backwards DNA strand:
                    # def complement(x):
                    #     if x == "A":
                    #         return "T"
                    #     elif x == "C":
                    #         return "G"
                    #     elif x == "G":
                    #         return "C"
                    #     elif x == "T":
                    #         return "A"

                    # back_dna_s = ""
                    # for base in seq:
                    #     back_dna_s = back_dna_s + complement(base)

                    # back_strand_dna = back_dna_s[::-1]

                    # # make out of back_strand_dna an RNA strand
                    # back_rna_s = ""

                    # for base in back_strand_dna:
                    #     if base == "T":
                    #         base = "U"
                    #         back_rna_s += base
                    #     else:
                    #         back_rna_s += base

                    # print(f"This is backward RNA strand {back_rna_s}")


start_seq_len = len(start_seq)

start_positions = []

# for forward strand:
for i in range(len(forward_rna_s)-2):
    if forward_rna_s[i:i+start_seq_len] == start_seq:
        start_positions.append(i)
print(start_positions)


for start in start_positions:
    peptide = ""
    orf = ""
    for i in range(start, len(forward_rna_s) -2, 3):
        codon = forward_rna_s[i:i+3] # find the tripplet in the sequence
        if codon in ["UAA", "UAG", "UGA"]:
            break
        orf += codon # adds the tripplet to orf
        aminoacid = code[codon]
        peptide += aminoacid
    print(orf)
    print(peptide)

