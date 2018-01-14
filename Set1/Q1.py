import argparse
import utils

# Convert hex to base64

# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# Should produce:

# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="Hexadecimal input for conversion")
	args = parser.parse_args()
	print("Input : ", args.input)
	print("Output : ", utils.hex_to_bytes(args.input).decode("utf-8"))
	print("Output : ", utils.hex_to_base64(args.input).decode("utf-8"))