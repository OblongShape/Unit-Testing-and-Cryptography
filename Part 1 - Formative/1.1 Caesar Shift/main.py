# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text = "HELLOWORLD"



def caesar_encode(text, n):
    new_str = ""
    for let in text:
        index = alpha.index(let)
        new_str += alpha[(index) % len(alpha)]
    return new_str


def caesar_decode(text, n):
    return ""


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
