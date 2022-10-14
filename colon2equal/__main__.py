# tools to transfer colon to equal

import argparse
from colon2equal.transfer import colon2equal


def main():
    parser = argparse.ArgumentParser(description="quick transfer code.")
    parser.add_argument("strings", help="input string")
    args = parser.parse_args()
    print(colon2equal(args.strings))


if __name__ == "__main__":
    main()
