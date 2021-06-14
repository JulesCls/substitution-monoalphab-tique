import sys

#Saisie et traitement de la chaîne de caractères
print("Saisir une chaîne à décrypter")
lines = [] 
while True: 
	line = input() 
	if line == '': 
		break 
	else: 
		lines.append(line) 
text = '\n'.join(lines)
text = text.replace("\n", " ") 
words=text.split()

#alphabet pour la comparaisons
alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z"
l=alphabet.split()

#décryptage du texte
newtext = []
for word in words:
    newords =[]
    for j in range(0,26):
        neword = ""
        for letter in word:
            if l.count(letter) != 0:
                k = letter.replace(letter, l[l.index(letter)-j])
                neword+=k
        newords.append(neword)
        print(str(j)+"\t"+newords[j])
    print("Saisir numéro du bon mot:")
    n = int(input())
    newtext.append(newords[n])

#affichage du texte final
print("Le message décodé est :")
for word in newtext:
    print(word+" ", end='')

        
