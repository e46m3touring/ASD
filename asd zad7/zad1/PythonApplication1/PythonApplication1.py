# 1. Permutacje ciągu znaków
def permute(s, path="", used=None):
    if used is None:
        used = [False] * len(s)
    if len(path) == len(s):
        print(path)
        return
    for i in range(len(s)):
        if not used[i]:
            used[i] = True
            permute(s, path + s[i], used)
            used[i] = False

# 2. Rekurencyjne wypisanie liczby w zapisie binarnym
def print_binary(n):
    if n > 1:
        print_binary(n // 2)
    print(n % 2, end="")

# 3. Rozwiązanie labiryntu (rekurencja DFS)
def solve_maze(maze, start, end, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()

    x, y = start
    if start == end:
        print("Path found:", path)
        return True

    visited.add(start)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # prawo, dół, lewo, góra
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) not in visited:
            if solve_maze(maze, (nx, ny), end, path + [(nx, ny)], visited):
                return True

    return False

# Przykładowe uruchomienie
if __name__ == "__main__":
    print("Permutacje ciągu 'abc':")
    permute("abc")

    print("\nPodaj liczbę całkowitą do wypisania w zapisie binarnym:")
    n = int(input())
    print("Zapis binarny liczby:")
    print_binary(n)

    print("\n\nLabirynt:")
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    if not solve_maze(maze, start, end):
        print("Brak ścieżki.")



