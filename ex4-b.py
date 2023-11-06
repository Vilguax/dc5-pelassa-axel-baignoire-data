def factoriel(n):
    facto = 1
    i = 1

    if n < 0:
        print("La factorielle n'est pas définie pour les nombres négatifs.")
    else:
        while i <= n:
            facto *= i
            i += 1
        return facto


print(factoriel(5))
print(factoriel(10))
print(factoriel(100))