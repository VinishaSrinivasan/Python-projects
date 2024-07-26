# RANDOM PASSWORD GENERATOR #

import random

print("Welcome to random password generater ! ")
randchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#@$*"
nopwdnd = int(input("Please enter the number of passwords to be generated: "))
pwdlen = int(input("Please enter the length of the password: "))

print("Here are your random passwords: ")

for v in range(nopwdnd):
    pwd=""
    for j in range(pwdlen):
        pwd=pwd+random.choice(randchar)
    print(pwd) 