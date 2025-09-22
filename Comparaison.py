import math

while True:
    print("I am Anselme, a code's learner")
    print("Welcome! Here you can compare two numbers even with math.sqrt (√)")
    print("For square root, enter math.sqrt(x) or x**0.5")

    a = eval(input("Entrez la valeur de a : "))
    b = eval(input("Entrez la valeur de b : "))

    if a == b:
        print("a est égal à b")
    elif a < b:
        print("a est inférieur à b")
    else:
        print("a est supérieur à b")

    reponse = input("Share my code to your friends. Do you want to continue? (Yes/no) : ").lower()
    if reponse != "yes":
        print("Thanks for using my code!")
        break


