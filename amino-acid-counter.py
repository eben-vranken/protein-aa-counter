from argparse import ArgumentParser

from src import counter
from src import parser
from src import formatter

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-s", "--sequence", help="The protein sequence to be counted.")
    parser.add_argument("-f", "--file", help="File path to FASTA protein file.")

    # Formatting args
    parser.add_argument("-t", "--table", action="store_true", help="Print the frequencies as a table.")

    args = parser.parse_args()
    
    if not args.file and not args.sequence:
        print("Either file or sequence flag is required.")
        exit(1)
    
    if args.file and args.sequence:
        print("Using both flag and sequence flags in one command is not allowed.")
        exit(1)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if args.file:
        sequence = parser.parse_fasta(args.file)
    else:
        sequence = args.sequence

    # These two functions could definitely be combined into 1.
    # That would make this counter be O(2N) instead of O(N)
    # but hey, separation of concerns.
    counter.validate_sequence(sequence)
    frequencies = counter.count_aminos(sequence)

    if args.table:
        formatter.print_table(frequencies)
    else:
        formatter.print_normal(frequencies)