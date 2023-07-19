p = 31
q = 37

N = p*q
e = 143
d = 287


#we want to send bob a message x, let x be 23. we send 23^3 (mod 55). 





# message = 300
# print("message is: ", message)
# encripted_message = (message**e) % N
# print("encripted message: ", encripted_message)
# decrypted_message = (encripted_message**d) % N
# print("decrypted message: ", decrypted_message)

#hello = 8,5,12,12,15
def encript_message(arr):
    encripted = []
    for num in arr:
        encripted.append((num**e) % N)
    return encripted

def decript_message(arr):
    decripted = []
    for num in arr:
        decripted.append((num**d) % N)
    return decripted

def int_to_string(arr):
    alphebet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w" , "x", "y", "z"]
    my_str = ""
    for num in arr:
        my_str += alphebet[num - 1]
    return my_str

def string_to_int(string):
    arr = []
    conversion = {"a": 1, "b" : 2, "c": 3, "d" : 4, "e": 5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23 , "x":24, "y":25, "z":26}
    for letter in string:
        arr.append(conversion[letter])
    return arr

# encripted_message = encript_message([8,5,12,12,15])
# print(encripted_message)
# print(decript_message(encripted_message))

word = input("enter your word: ")
word_as_number = string_to_int(word)
print("your word as a number is : ", word_as_number)
encripted_message = encript_message(word_as_number)
print("your word after encription: ", encripted_message)
decripted_message = decript_message(encripted_message)
print("your word after decription (in number form): ", decripted_message)
print("your word as a string: ", int_to_string(decripted_message))