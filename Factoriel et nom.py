#Vianney ANANI
#Factoriel avec 2 boucle

nombre=5
####################################################
#Boucle While
fact=1;i=1
while i<=nombre:
  fact*=i
  i += 1
print("Calcul du factoriel de",nombre,"est",fact)

####################################################
#Boucle for
fact=1
for i in range(1, nombre + 1):
  fact*=i
print("Calcul du factoriel de",nombre,"est",fact)

###################################################
nom = "ANANI"
prenom = "Vianney"

for i in range(1, 51):
    if (i % 3 == 0 and i % 5 == 0):
        print(i,"Nom:",nom,"Prenom:",prenom)

    elif (i % 3 == 0):
        print(i,"Nom:",nom)

    elif (i % 5 == 0):
        print(i,"Prenom:",prenom)

    else:
        print(i,"Aucun")
