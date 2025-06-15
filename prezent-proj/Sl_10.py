import random

# Losowa funkcja dopasowania (tylko do pokazania losowości)
def fitness():
    return random.randint(50, 100)

# Symulacja różnych wyników przy każdym uruchomieniu
for i in range(5):
    print(f"Próba {i+1}: wynik = {fitness()}")
