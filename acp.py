import random 
import string 
def randPass(length):
    lowcases = string.ascii_lowercase
    upcases = string.ascii_uppercase
    num = string.digits
    punctu = string.punctuation
    
    password = [random.choice(lowcases), random.choice(upcases), random.choice(num), random.choice(punctu)]
    
    name = lowcases + upcases + num + punctu
    
    password = password + random.choices(name, k = length - len(password))
    
    return "".join(password)
passwordLenghth = random.randint(6, 10)
password = randPass(passwordLenghth)

print(f"Password: {password}")