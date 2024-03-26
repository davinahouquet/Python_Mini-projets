import random

longpass=int(input("Donner la longueur du mot de passe:"))

s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~'
password="".join(random.sample(s,longpass))
print(password)