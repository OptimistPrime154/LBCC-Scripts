

ciphertext = "389522349995436715844193537714605131724625287193646686754528880"

flag = bytes.fromhex(ciphertext).decode()

print(flag)


#learn .encode and .decode