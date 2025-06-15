import random

# Parametry algorytmu
POPULATION_SIZE = 6     # liczba osobników
GENE_LENGTH = 5         # długość genotypu (ilość genów 0/1)
GENERATIONS = 10        # liczba pokoleń

# Tworzenie losowego osobnika (ciąg 0 i 1)
def generate_individual():
    return [random.randint(0, 1) for _ in range(GENE_LENGTH)]

# Funkcja dopasowania: liczba jedynek = jakość rozwiązania
def fitness(individual):
    return sum(individual)

# Wybór dwóch najlepszych osobników z populacji
def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

# Krzyżowanie jednopunktowe: mieszanie "genów" dwóch rodziców
def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    return parent1[:point] + parent2[point:]

# Mutacja: zmiana losowego genu (0 -> 1 lub 1 -> 0)
def mutate(individual):
    index = random.randint(0, GENE_LENGTH - 1)
    individual[index] = 1 - individual[index]

# Główna pętla algorytmu genetycznego
def genetic_algorithm():
    # 1. Start – losowa inicjalizacja populacji
    population = [generate_individual() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        print(f"\nPokolenie {generation + 1}")

        # 2. Ocena – obliczenie dopasowania każdego osobnika
        for ind in population:
            print(f"Osobnik: {ind}, dopasowanie: {fitness(ind)}")

        # 3. Selekcja – wybór najlepszych osobników
        parent1, parent2 = selection(population)

        # 4-5-6. Krzyżowanie, mutacja i tworzenie nowej populacji
        new_population = []
        while len(new_population) < POPULATION_SIZE:
            child = crossover(parent1, parent2)
            if random.random() < 0.3:  # 30% szansy na mutację
                mutate(child)
            new_population.append(child)

        # 7. Nowa populacja zastępuje starą
        population = new_population

# Uruchomienie algorytmu
genetic_algorithm()
