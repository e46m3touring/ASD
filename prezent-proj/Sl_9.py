import random

# Prosty problem: znajdź ciąg 5 jedynek
def fitness(ind):
    return sum(ind)

# Generowanie losowego osobnika
def generate():
    return [random.randint(0, 1) for _ in range(5)]

# Mutacja: zamień losowy bit
def mutate(ind):
    i = random.randint(0, 4)
    ind[i] = 1 - ind[i]
    return ind

# Minimalny algorytm genetyczny
best = generate()
for _ in range(20):
    candidate = mutate(best[:])
    if fitness(candidate) > fitness(best):
        best = candidate

print("Najlepszy osobnik:", best, "Dopasowanie:", fitness(best))
