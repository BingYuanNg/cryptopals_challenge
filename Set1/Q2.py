import argparse
import utils


# Fixed XOR

# Write a function that takes two equal-length buffers and produces their XOR combination.

# If your function works properly, then when you feed it the string:

# 1c0111001f010100061a024b53535009181c

# ... after hex decoding, and when XOR'd against:

# 686974207468652062756c6c277320657965

# ... should produce:

# 746865206b696420646f6e277420706c6179

if __name__=="__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("a",help="Input 1")
	parser.add_argument("b",help="Input 2")

	args = parser.parse_args()

	a = utils.hex_to_bytes(args.a)
	b = utils.hex_to_bytes(args.b)

	result = bytearray(utils.xor_bytes(a,b))

	result = utils.byte_to_hex(result)
	print("Input 1 : ",args.a)
	print("Input 2 : ",args.b)
	print("Output  : ",result.decode('utf-8'))

