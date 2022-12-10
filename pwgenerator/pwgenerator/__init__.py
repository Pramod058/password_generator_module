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