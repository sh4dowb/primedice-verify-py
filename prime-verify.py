import hmac
import hashlib
import base64

def roll(key, text):
	hash = hmac.new(key, text, hashlib.sha512).hexdigest()

	index = 0
	lucky = int(hash[index * 5:index * 5 + 5], 16)

	print(lucky)

	while lucky >= 10**6:
		index += 1
		lucky = int(hash[index * 5:index * 5 + 5], 16)
		if index * 5 + 5 > 128:
			lucky = 99.99;
			break

	lucky %= 10**4.0
	lucky /= 10**2.0
	return lucky

print(roll(raw_input("Server hash: "), raw_input("Client hash-nonce: ")))
