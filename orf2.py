from prot import translate, code
from rosalind_revc import reverse_complement

seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

# find all start codons:
def orf_start_positions(rna):
    start_positions = []
    for i in range(len(rna)-2):
        if rna[i:i+3] == "AUG":
            start_positions.append(i)
    return start_positions

# find the open reading frame:
def find_orfs(rna, start_positions):
    orfs = []
    for start in start_positions:
        orf = ""
        for i in range(start, len(rna), 3):
            codon = rna[i:i+3] # find the tripplet in the sequence
            orf += codon # adds the tripplet to orf
            if len(codon) < 3:
                    break
            if code[codon] == "Stop":
                orfs.append(orf)
    return orfs

# make a forward RNA strand:
forward_rna_s = ""
for base in seq:
    if base == "T":
        base = "U"
        forward_rna_s += base
    else:
        forward_rna_s += base

# print(f"This is forward RNA strand {forward_rna_s}")

# make a backwards RNA strand:
backward_dna = reverse_complement(seq)
back_rna = backward_dna.replace("T", "U")
# print(f"test for backwards RNA {back_rna}")

# find start codons in forward and backwards rna strand:
f_starts = orf_start_positions(forward_rna_s)
b_starts = orf_start_positions(back_rna)

# find open reading frames in both:
f_orfs = find_orfs(forward_rna_s, f_starts)
b_orfs = find_orfs(back_rna, b_starts)

orfs = f_orfs + b_orfs # combines the two lists into one list (not string) 
proteins = list()
for orf in orfs:
    protein = translate(orf)
    if protein not in proteins:
        proteins.append(protein)
        print(protein)
