i = 0
list = []

val = input("Nom de la valeur recherchée: ")
moy_val = float(input("Entrer la moyenne de la valeur rechercher: "))

moy = input(" Entrer les moyennes qui vont permettre de calculer l'incertitude: ").split(",")
print(moy)
incer = input("Entrer leurs incertitudes ").split(",")
print(incer)
coeff = input("Entrer leurs puissance ").split(",")
print(coeff)

for loop in range(len(moy)):
  list.append((float(incer[i])*float(coeff[i]))/float(moy[i]))
  i+=1

# = sum(list)
q = 0
p = 0
for j in range(len(list)) :
    q +=float(list[p])
    p+=1
num = moy_val * q
print(f"L'incertitude de {val} est :{num}")
