phrase = input("Saisissez une phrase : ")
nb_mots = 0
precedent_alphanum = False
precedent_ponctuation = False

for lettre in phrase:
    if ('a' <= lettre <= 'z') or ('A' <= lettre <= 'Z') or ('0' <= lettre <= '9') or lettre in "àâäéèêëïîôöùûüç":
        if not precedent_alphanum:
            nb_mots += 1
        precedent_alphanum = True
        precedent_ponctuation = False 
    else:
        if lettre in "'-!.?,":
            if not precedent_ponctuation:
                nb_mots += 1
            precedent_ponctuation = True
        else:
            precedent_ponctuation = False
        precedent_alphanum = False

phrase_maj = ""
for lettre in phrase:
    if 'a' <= lettre <= 'z':
        phrase_maj += chr(ord(lettre) - 32)
    else:
        phrase_maj += lettre

phrase_min = ""
for lettre in phrase:
    if 'A' <= lettre <= 'Z':
        phrase_min += chr(ord(lettre) + 32)
    else:
        phrase_min += lettre

print("Nombre de mots :", nb_mots)
print("Phrase en majuscule :", phrase_maj)
print("Phrase en minuscule :", phrase_min)