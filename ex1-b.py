phrase = input("Saisissez une phrase : ")
nb_mots = 0
for lettre in phrase:
    if lettre == " ":
        nb_mots += 1
nb_mots += 1

phrase_maj = ""
for lettre in phrase:
    if lettre >= "a" and lettre <= "z":
        lettre = chr(ord(lettre) - 32)
    phrase_maj += lettre

phrase_min = ""
for lettre in phrase:
    if lettre >= "A" and lettre <= "Z":
        lettre = chr(ord(lettre) + 32)
    phrase_min += lettre


print("Nombre de mots :", nb_mots)
print("Phrase en majuscule :", phrase_maj)
print("Phrase en minuscule :", phrase_min)