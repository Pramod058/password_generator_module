import string
import random
def generate(number):
    characters = list(string.ascii_letters + string.digits + string.punctuation)
    try:
        chars = []
        i = 0 
        while i<= number:
            chars.append(random.choice(characters))
            i+= 1
        random.shuffle(chars)
        password = "".join(chars)
        return password
    except:
        return "Something went wrong"

def CountChar(characters):
    count = 0
    final = []
    only_value = []
    for char in characters:
        if char not in only_value:
            only_value.append(char)

    for i in only_value:
        count = 0
        for ch in characters:
            if i == ch:
                count+= 1
        final.append({i : count})
        
    return final