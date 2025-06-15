import random
import math

# Lista miast (punkty w 2D)
cities = [(0, 0), (1, 5), (5, 2), (6, 6), (8, 3)]

# Oblicz dystans Euklidesowy między dwoma punktami
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Całkowity dystans dla trasy (kolejność miast)
def total_distance(path):
    return sum(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))

# Generuj losową trasę (permutacja miast)
def generate_path():
    path = list(range(len(cities)))
    random.shuffle(path)
    return path

# Krzyżowanie – zamiana losowych miejsc w trasie
def crossover(p1, p2):
    cut = random.randint(1, len(cities) - 2)
    child = p1[:cut] + [city for city in p2 if city not in p1[:cut]]
    return child

# Mutacja – zamiana miejscami dwóch miast
def mutate(path):
    i, j = random.sample(range(len(path)), 2)
    path[i], path[j] = path[j], path[i]

# Algorytm genetyczny
def tsp_ga():
    population = [generate_path() for _ in range(6)]
    for generation in range(20):
        population.sort(key=total_distance)
        print(f"\nPokolenie {generation + 1}, najlepsza trasa: {population[0]}, dystans: {total_distance(population[0]):.2f}")

        parent1, parent2 = population[0], population[1]
        new_population = []

        while len(new_population) < 6:
            child = crossover(parent1, parent2)
            if random.random() < 0.3:
                mutate(child)
            new_population.append(child)

        population = new_population

tsp_ga()
