import random
print("1: Lancer le dé, 0: Quitter le programme")
while True:
    x=int(input("Cliquer sur un bouton ")) #x est forcément un entier
    if x==0:
        print('Terminé')
        break
    elif x==1:
        print(random.randint(1,80)) #Génère des entiers entre a et b
    else:
        print("Je n'ai pas compris")