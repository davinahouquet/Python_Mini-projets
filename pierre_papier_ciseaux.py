import random
choix=['Pi','P','C']
score_cpu=0
score_joueur=0

while True:
    cpu = random.choice(choix)
    joueur = str(input('C: Ciseaux, Pi: Pierre ou P: Papier ? Pour terminer tapez Fin ')).capitalize()
    if joueur==cpu:
        print("Egalité !")
    elif joueur=='Pi':
        if cpu=='P':
            print("Vous perdez, le papier couvre la pierre")
            score_cpu+=1
        elif cpu=='C':
            print("Vous gagnez, la pierre casse les ciseaux")
            score_joueur+=1
    elif joueur=='P':
        if cpu=='Pi':
            print('Vous gagnez, le papier couvre la pierre')
            score_joueur += 1
        elif cpu=='C':
            print('Vous perdez, les ciseaux coupent le papier')
            score_cpu += 1
    elif joueur=='C':
        if cpu=='Pi':
            print('Vous perdez, la pierre casse les ciseaux')
            score_cpu += 1
        elif cpu=='P':
            print('Vous gagnez, les ciseaux coupent le papier')
            score_joueur += 1
    elif joueur=='Fin':
        print('Résultat : ')
        print(f"CPU : {score_cpu}")
        print(f"joueur : {score_joueur}")
        break
    else:
        print("Je n'ai pas compris, vérifiez l'orthographe")