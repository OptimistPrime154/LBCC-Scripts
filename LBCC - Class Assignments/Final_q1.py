
#Answer: XMAS{guido_has_been_good_this_year_https://en.wikipedia.org/wiki/Guido_van_Rossum}

#opening file to start conversion
with open('q1_input.txt', 'r') as file:
    codes = file.readlines()
#TESTING OUTPUT
#print(codes)

characters_list = [] #creating empty list to hold characters
#iterating over lines
for code in codes:
    #stripping newlines (\n)
    unicode = int(code.strip())
    #TESTING
    #print(unicode)
    #CONVERTING NUMBERS TO CHARACTERS
    characters = chr(unicode)
    #TESTING OUTPUT
    #print(characters) letters print in new lines and are in reverse
    characters_list.append(characters)
#TESTING OUTPUT
#print(characters_list)

#NEED TO REVERSE AND REMOVE QUOTES('')
#print(''.join(reversed(characters_list)))    

flag = ''.join(reversed(characters_list))

print ("Answer: " + flag)

