def xor_with_13(label):
    # XOR each character with the integer 13 and convert back to a string
    result_string = ''.join(chr(ord(char) ^ 13) for char in label)
    return result_string

# Example usage
label = "label"
result = xor_with_13(label)
print(result)

