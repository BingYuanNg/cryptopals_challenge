import base64
import binascii
from itertools import cycle

def xor(a,b):
	return a^b

def xor_bytes(a,b):
	return [xor(x,y) for (x,y) in list(zip(a,cycle(b))) ]

def hex_to_bytes(input):
	return bytearray.fromhex(input)

def hex_to_base64(input):
	return base64.b64encode(hex_to_bytes(input))
	
def byte_to_hex(input):
	return binascii.hexlify(input)