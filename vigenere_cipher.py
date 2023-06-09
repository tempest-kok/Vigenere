initial_text = "hello world"  #-> "catca tcatc" -> "jeeno pqref"
key = "cat"
initial_text = list(initial_text)
key = list(key)
key_len = len(key)
count = 0
key_text = []
for i in range(len(initial_text)):
    if not 97 <= ord(initial_text[i]) <= 122:
        key_text.append(initial_text[i])
        count += 1
    else:
        key_text.append(key[(i - count) % key_len])
vigenere = ""
for i in range(len(initial_text)):
    if not 97 <= ord(initial_text[i]) <= 122:
        char = initial_text[i]
    else:
        char = chr(97 + (ord(initial_text[i]) + ord(key_text[i]) - 97 - 97) % 26)
    vigenere += char
print(vigenere)