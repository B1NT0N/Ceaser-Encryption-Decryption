import string
import random

with open('<FILENAME>.txt', 'r') as f:
    text = f.read()

def ceaser(text, shift, alphabets):
    def shift_alphabets(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabets, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

times = random.randint(26,50)
sumkey=0
keys = []

for x in range(times):
    key = random.randint(0,9)
    text = ceaser(text, key, [string.ascii_uppercase, string.ascii_lowercase,])
    sumkey = sumkey+key
    keys.append(key)

with open('<FILENAME>-ENCRYPTED.txt','a') as f:
            f.write(text)

with open('KEYS.txt','a') as f:
            f.write(str(keys))

for x in range(len(keys)):
    key = keys[x]
    text = ceaser(text, 26-key, [string.ascii_uppercase, string.ascii_lowercase,])

print(" _            _    \n"+"| |          | |   \n"+"| | ___   ___| | __\n"+"| |/ _ \ / __| |/ /\n"+"| | (_) | (__|   < \n"+"|_|\___/ \___|_|\_\ \n")




