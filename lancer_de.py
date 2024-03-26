import random
while True:
    x=int(input("Cliquer sur un bouton ")) #x est forcément un entier
    if x==0:
        print('Terminé')
        break
    elif x==1:
        print(random.randint(1,6)) #Génère des entiers entre a et b
