def count(filepath, search):
    counts = {word: 0 for word in search}
    
    with open(filepath, 'r') as file:
        text = file.read()
        
    word = ''
    alpha = False
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
            word += char
            alpha = True
        else:
            if alpha:
                if word in counts:
                    counts[word] += 1
                word = ''
            alpha = False
            
    if word and word in counts:
        counts[word] += 1

    return counts

filepath = 'mots.txt'
search = ['Homme', 'homme', 'hommes', 'Hommes', 'femme', 'femmes', 'Femme', 'Femmes']
result = count(filepath, search)
print(result)