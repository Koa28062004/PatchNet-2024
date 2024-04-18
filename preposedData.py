import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help='Input file')
    parser.add_argument('--output', type=str, required=True, help='Output file')
    return parser.parse_args()

def main():
    args = arg_parser()

if __name__ == '__main__':
    main()