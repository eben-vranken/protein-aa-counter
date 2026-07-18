from argparse import ArgumentParser
from src import counter

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", help="The protein sequence to be counted.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    sequence = args.sequence

    # These two functions could definitely be combined into 1.
    # That would make this counter be O(2N) instead of O(N)
    # but hey, separation of concerns.
    counter.validate_sequence(sequence)
    frequences = counter.count_aminos(sequence)

    print(frequences)