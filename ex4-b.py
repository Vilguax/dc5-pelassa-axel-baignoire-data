def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)

print(factoriel(5))
print(factoriel(10))
print(factoriel(100))