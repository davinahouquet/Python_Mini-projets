import random

longpass=int(input("Donner la longueur du mot de passe:"))

s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~'
print(random.sample(s,longpass))