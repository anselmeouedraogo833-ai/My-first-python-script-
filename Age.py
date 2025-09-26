
age = int(input("Quel âge avez-vous ? "))

if age < 18:
    print("Tu es encore trop bébé. Si t'avais plus que ça tu serais plus content !!! Grandis !")

elif age == 18:
    print("Je peux vous vouvoyer maintenant... mais est-ce que tu as go ??")
    reponse = input("Tu as go ??? (yes/no) : ").lower()
    
    if reponse != "yes":
        print("À ton âge là ? Humm ?? Donne ta vie à Jésus frère. Bye !")
    else:
        print("Hein donc tu as go hein... ")

else:
    print("Salut grand frère, pensez à vous marier")
    reponse = input("oubien vous etes deja marié?(yes/no) : ").lower()
    if reponse != "yes":
        print("Vous n'avez pas honte?")
    else:
        print("Que le bonheur pour vous ")


