def print_normal(frequencies):
    for amino, count in frequencies.items():
        print(amino, count)

def print_table(frequencies):
    print("|  Amino  Count  |")
    print("-"*18)
    for amino, count in frequencies.items():
        print("|  ", amino, "\t |", count, "\t |")