def compter_mots(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
            
        nb_mots = 0
        precedent_alphanum = False

        for lettre in contenu:
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

        return nb_mots

nombre_de_mots = compter_mots('mots.txt')
if nombre_de_mots is not None:
    print(f"Le nombre total de mots dans le fichier est : {nombre_de_mots}")
