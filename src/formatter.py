from src.counter import amino_lists

def print_normal(frequencies, verbose=False):
    for amino, count in frequencies.items():
        label = amino_lists[amino] if verbose else amino
        print(label, count)

def print_table(frequencies, verbose=False):
    label_width = max(len(amino_lists[a]) for a in frequencies) if verbose else 5
    count_width = max(len(str(c)) for c in frequencies.values())
    count_width = max(count_width, 5)
 
    header = f"| {'Amino'.ljust(label_width)} | {'Count'.ljust(count_width)} |"
    print(header)
    print("-" * len(header))
    for amino, count in frequencies.items():
        label = amino_lists[amino] if verbose else amino
        print(f"| {label.ljust(label_width)} | {str(count).ljust(count_width)} |")
