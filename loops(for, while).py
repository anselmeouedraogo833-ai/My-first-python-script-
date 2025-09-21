U nano 8.6                                                          learning.py
Friends=["Axel","Jackhen","Bazo","Faïco","Andi","Anselme","Auguste","Lacina"]
for Friend in Friends:
   print ( "Hello just wanna say you that you will pass your exam this year"  + Friend + "!")
for i in range(1,5):
   print ("*" * i)
hauteur = 6
for i in range (1,hauteur+ 1):
   espaces = "" *( hauteur-1)
   etoiles = "*" * (2 * i-1)
   print ( espaces + etoiles)
i=0
while i<=4 :
      print ("*");i+=1
for i in range(1,6):
   print ("*" * i)

for i in range ( 1,6):
    print ("*" * (6 - i))
print (" "*5 + "#"*5)
h=5
for i in range (1,h + 1):
    espaces =" " * (h - i)
    etoiles= "*" * i
    print (espaces + etoiles)
h=5
for i in range (1,h):
   espaces=" " * (h - i)
   etoiles="*" * (2 * i - 1)
   print ( espaces + etoiles)
h=5
for i in range(1,h+1):
    espaces=" " * ( h - i)
    etoiles="*" * (2 * i - 1)
    print ( espaces + etoiles)
for i in range(h - 1, 0, - 1):
    espaces=" " * (h -  i)
    etoiles="*" * (2 * i - 1)
    print (espaces + etoiles)
