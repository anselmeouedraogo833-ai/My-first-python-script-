import math  # pour utiliser sqrt (racine carrée)

while True:
    print("Welcome! Here you can compare two numbers y compris les racines carrées ")

    a = eval(input("Entrez la valeur de a : "))
    b = eval(input("Entrez la valeur de b : "))

    if a == b:
        print("a est égal à b")
    elif a < b:
        print("a est inférieur à b")
    else:
        print("a est supérieur à b")

    reponse = input("Veux-tu recommencer ? (oui/non) : ").lower()
    if reponse != "oui":
        print("Merci d'avoir utilisé mon programme !")
        break
      
