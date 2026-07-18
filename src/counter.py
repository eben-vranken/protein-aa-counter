amino_lists = {
    "A": "Alanine",
    "R": "Arginine",
    "N": "Asparagine",
    "D": "Aspartic acid",
    "C": "Cysteine",
    "E": "Glutamic acid",
    "Q": "Glutamine",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "L": "Leucine",
    "K": "Lysine",
    "M": "Methionine",
    "F": "Phenylalanine",
    "P": "Proline",
    "S": "Serine",
    "T": "Threonine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
    "V": "Valine"
}

def validate_sequence(sequence):
    for c in sequence:
        if c not in amino_lists:
            print(f"Sequence contained invalid character: %s" % c)
            exit(1)

def count_aminos(sequence):
    amino_counts = {}

    for c in sequence:
        if c in amino_counts:
            amino_counts[c] += 1
        else:
            amino_counts[c] = 1
    
    return amino_counts