import base64

ciphertext = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Convert hexadecimal string to bytes
hex_bytes = bytes.fromhex(ciphertext)

# Encode the bytes using base64
flag = base64.b64encode(hex_bytes)

print(flag.decode())                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    