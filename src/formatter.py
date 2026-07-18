from src.counter import amino_lists

def print_normal(frequencies, verbose=False):
    for amino, count in frequencies.items():
        label = amino_lists[amino] if verbose else amino
        print(label, count)

def print_table(frequencies, verbose=False):
    width = max(len(amino_lists[a]) for a in frequencies) if verbose else 5
    print(f"|  Amino{' ' * (width - 5)}  Count  |")
    print("-" * (width + 13))
    for amino, count in frequencies.items():
        label = amino_lists[amino] if verbose else amino
        print("|  ", label.ljust(width), "\t |", count, "\t |")