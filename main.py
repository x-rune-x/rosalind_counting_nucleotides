def nuc_count(s):
    file = open(s, "r")
    dna = file.read()
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0

    for nucleotide in dna:
        if nucleotide.upper() == "A":
            a_count += 1
        elif nucleotide.upper() == "C":
            c_count += 1
        elif nucleotide.upper() == "G":
            g_count += 1
        elif nucleotide.upper() == "T":
            t_count += 1

    file.close()
    counts = f"{a_count} {c_count} {g_count} {t_count}"
    return counts


nucleotide_counts = nuc_count("rosalind_dna.txt")
print(nucleotide_counts)
