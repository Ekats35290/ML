import random
import string

def generate_id():
    used = set()
    while True:
        if len(used) == 5:
            break
        used.add(random.randint(0, 9))
    return "".join([str(x) for x in used])

def generate_login():
    letters = string.ascii_lowercase
    consonants = 'bcdfghjklmnpqrstvwxz'
    return ''.join(random.choice(letters) for i in range(5)) + random.choice(consonants)

def generate_password():
    symb = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
    password = ""
    for i in range(10):
        c = random.choice(symb)
        while c in password:
            c = random.choice(symb)
        else:
            password += c
    return password

def generate(n):
    
    ans = []
    for i in range(n):
        ans.append((generate_id(), generate_login(), generate_password()))
    return ans

print(*generate(10), sep="\n")
