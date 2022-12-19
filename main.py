def encode_cfmail(raw, key):
	return hex(key)[2:] + "".join([hex(ord(i) ^ key)[2:] for i in raw])

def decode_cfmail(encoded):
	key = int(encoded[:2], 16)
	return "".join([chr(int(encoded[i : i + 2], 16) ^ key) for i in range(2, len(encoded), 2)])
