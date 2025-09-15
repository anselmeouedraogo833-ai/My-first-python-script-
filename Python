import math # Import du module math pour utiliser la fonction sqrt (racine carrée)
a =float(input("Entrez la valeur de a : "))
b =float(input("Entrez la valeur de b : "))
c =float(input("Entrez la valeur de c : "))
if a==0 :
  print(f"ce n'est pas une équation du secon dégré")
else:
     print(f"l'equation est  {a}x² + {b}x + {c}=0",)
     delta = b**2 - 4 * a * c
print (" le discriminant est: ", delta)
if delta > 0:
    # calcule les deux solutions
  x1=(- b - math.sqrt(delta)) / (2 * a)
  x2= (- b +math.sqrt(delta))/(2 * a)
  print(f"deux solutions réelles x1={x1} et x2={x2}")
elif delta==0:
    # calcule l'unique solution
    x=-b/(2 * a)
    print (f"une solution unique réelle  x={x}")
else:
    # affiche qu'il n'y a pas de solution réelle
    print ("pas de solution (ensemble vide)")




