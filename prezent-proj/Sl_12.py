import random
import math

# Funkcja z lokalnym i globalnym maksimum
def func(x):
    return math.sin(5 * x) * (1 - x) + 1  # lokalne max ok. x=0.2, globalne max ok. x=0.8

# Hill climbing (lokalne przeszukiwanie)
def hill_climb():
    x = random.uniform(0, 1)
    for _ in range(50):
        new_x = x + random.uniform(-0.05, 0.05)
        if 0 <= new_x <= 1 and func(new_x) > func(x):
            x = new_x
    return x, func(x)

# Genetyczny – losowa populacja i selekcja najlepszego
def genetic_search():
    population = [random.uniform(0, 1) for _ in range(20)]
    for _ in range(20):
        population.sort(key=func, reverse=True)
        parent1, parent2 = population[0], population[1]
        child = (parent1 + parent2) / 2
        if random.random() < 0.3:
            child += random.uniform(-0.1, 0.1)
        child = max(0, min(1, child))
        population[-1] = child
    best = max(population, key=func)
    return best, func(best)

# Wyniki porównania
hc_result = hill_climb()
ga_result = genetic_search()

print(f"Hill Climb: x = {hc_result[0]:.3f}, wynik = {hc_result[1]:.3f}")
print(f"Genetyczny: x = {ga_result[0]:.3f}, wynik = {ga_result[1]:.3f}")
