from argparse import ArgumentParser
from src import counter

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", help="The protein sequence to be counted.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    sequence = args.sequence

    counter.validate_sequence(sequence)