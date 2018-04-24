'''Password Generator - Should be random and a combination of Upper and lowercase, special symbol and numbers'''
import string
import random

x=''.join(random.choice(string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
print(x)


#s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#p =  "".join(random.sample(s,10 ))
#print p
