KEY1 = int('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313', 16)
KEY2_xor_KEY1 = int('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e', 16)
KEY2_xor_KEY3 = int('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1', 16)
FLAG_xor_KEYS = int('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf', 16)

# Cancel out common terms using commutative and associative properties
FLAG_xor_KEYS ^= KEY2_xor_KEY1  # Cancelling KEY2
FLAG_xor_KEYS ^= KEY2_xor_KEY3  # Cancelling KEY2

# Cancelling terms that are XOR'd with themselves
#FLAG_xor_KEYS ^= KEY1
#FLAG_xor_KEYS ^= KEY1
#FLAG_xor_KEYS ^= KEY3
#FLAG_xor_KEYS ^= KEY3

# The remaining value is the FLAG
FLAG = FLAG_xor_KEYS
print(FLAG.decode)