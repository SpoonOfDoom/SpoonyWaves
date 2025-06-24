"""Main entry point."""

import sys

from src.wavyfier import my_wave


def main():
    # get input filename from arguments:
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    # output filename is the same as input filename but with .mp4 extension
    output_file = input_file.rsplit(".", 1)[0] + ".mp4"
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    my_wave(input_file, output_file)


if __name__ == "__main__":
    main()
