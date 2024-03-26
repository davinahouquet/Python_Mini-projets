import random
choix=['Pi','P','C']
cpu=random.choice(choix)

while True:
    joueur = str(input('C: Ciseaux, Pi: Pierre ou P: Papier ? ')).capitalize()
    if joueur==cpu:
        print("Egalité !")
    elif joueur=='Pi':
        if cpu=='P':
            print("Vous perdez, le papier couvre la pierre")
        elif cpu=='C':
            print("Vous gagnez, la pierre casse les ciseaux")
    elif joueur=='Papier':
        if cpu=='Pi':
            print('Vous gagnez, le papier couvre la pierre')
        elif cpu=='C':
            print('Vous perdez, les ciseaux coupent le papier')
    elif joueur=='C':
        if cpu=='Pi':
            print('Vous perdez, la pierre casse les ciseaux')
        elif cpu=='C':
            print('Vous gagnez, les ciseaux coupent le papier')
    else:
        print("Je n'ai pas compris, vérifiez l'orthographe")