def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result




def caesar_encrypt(text, key):
    import collections
    # alphabetical base list in correct order
    alpha_base_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # create a transposed alphabetical list by shifting to the right by the key value
    transpose = collections.deque(alpha_base_list)
    transpose.rotate(key)
    transposed_list = list(transpose)

    # take the input text to be encrypted and split it into a list
    def split(word):
        return list(word)
    text_list = split(text)
    # print("The message to be encrypted is: ", text_list)

    # iterate over the text list to be encrypted and find its index in the transposed key-shifted list
    encrypted_index = []
    for char in text_list:
        if char in transposed_list:
            index = transposed_list.index(char)
            encrypted_index.append(index)
    # print("The index values in alpha_base_list to match to are: ", encrypted_index)

    # take the values of the encrypted_index and find the index-matching letters of alpha_base_list
    encrypted_list = []
    for value in encrypted_index:
        encrypted_list.append(alpha_base_list[value])
    # print("The encrypted message is: ", encrypted_list)

    # convert the encrypted_list message back to a string
    def convert(s):
        string = ""
        return string.join(s)
    encrypted_string = (convert(encrypted_list))
    print("The homemade version of this cipher is: ", encrypted_string)



text = "pizza time"
key = 19

print("Text  : " + text)
print("Key : " + str(key))
print("Cipher: " + encrypt(text, key))
caesar_encrypt(text, key)