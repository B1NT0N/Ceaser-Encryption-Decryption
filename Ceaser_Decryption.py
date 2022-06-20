import string
import random

def ceaser(text, shift, alphabets):
    def shift_alphabets(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabets, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

with open('<FILENAME>-ENCRYPTED.txt','r') as f:
            text=f.read()

keys=[]

with open('KEYS.txt','r') as f:
            lista=f.read()

for index,a in enumerate(lista):
	if (a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9'):
		keys.append(int(a))

for x in range(len(keys)):
    text = ceaser(text, 26-keys[x], [string.ascii_uppercase, string.ascii_lowercase,])

with open('<FILENAME>-DECRYPTED.txt','a') as f:
            f.write(text)

print("DECRYPTED1!!")