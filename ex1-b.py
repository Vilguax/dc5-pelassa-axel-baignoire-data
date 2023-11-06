phrase = input("Saisissez une phrase : ")
nb_mots = 0

precedent_alphanum = False
for lettre in phrase:
    if ('a' <= lettre <= 'z') or ('A' <= lettre <= 'Z') or ('0' <= lettre <= '9'):
        if not precedent_alphanum:
            nb_mots += 1
        precedent_alphanum = True
    else:
        if lettre == " ":
            precedent_alphanum = False
        else:
            if not precedent_alphanum:
                nb_mots += 1 
            precedent_alphanum = False

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