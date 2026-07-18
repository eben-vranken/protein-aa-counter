from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("sequence", help="The protein sequence to be counted.")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    print(args.sequence)