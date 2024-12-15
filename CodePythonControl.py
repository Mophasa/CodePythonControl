# 1) Création des fonctions mathématiques de base
def ajouter(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        return "Erreur : Division par zéro"
    return a / b

# 2) Dictionnaire pour stocker les opérations
operations = {
    '+': ajouter,
    '-': soustraire,
    '*': multiplier,
    '/': diviser
}

# 3) Fonction calculatrice
def calculatrice():
    num1 = float(input("Entrez le premier chiffre : "))  # Premier chiffre
    should_continue = True  # Variable pour continuer les calculs

    while should_continue:  # 5) Boucle while pour continuer les calculs
        # 4) Impression des symboles d'opération disponibles
        print("Opérations disponibles :")
        for symbole in operations.keys():
            print(symbole)

        # 6) Sélection du symbole d'opération
        symbole = input("Choisissez une opération : ")

        # 7) Saisie du deuxième numéro
        num2 = float(input("Entrez le deuxième chiffre : "))

        # 8) Récupération de la fonction correspondant au symbole d'opération
        calculation_function = operations.get(symbole)

        if calculation_function:  # Vérification si l'opération est valide
            # 9) Effectuer le calcul
            answer = calculation_function(num1, num2)

            # 10) Impression de l'équation et du résultat
            print(f"{num1} {symbole} {num2} = {answer}")

            # 11) Demande à l'utilisateur s'il souhaite continuer avec le résultat
            continuer = input("Souhaitez-vous utiliser ce résultat comme premier chiffre pour un autre calcul ? (oui/non) : ").strip().lower()
            if continuer == 'oui':
                num1 = answer  # 12) Mise à jour du premier chiffre avec le résultat
            else:
                should_continue = False  # 13) Démarrer un nouveau calcul

        else:
            print("Opération invalide. Veuillez choisir une opération valide.")

# Lancer la calculatrice
calculatrice()
