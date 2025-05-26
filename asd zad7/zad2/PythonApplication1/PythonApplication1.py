from collections import deque

# 1. Flood Fill - Rekurencyjny DFS (głębokie przeszukiwanie)
def flood_fill_dfs(image, x, y, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[x][y]

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            image[r][c] != original_color or image[r][c] == new_color):
            return

        image[r][c] = new_color

        # 4-kierunkowe sąsiedztwo
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    dfs(x, y)

# 2. Flood Fill - Iteracyjny BFS (szerokie przeszukiwanie)
def flood_fill_bfs(image, x, y, new_color):
    rows, cols = len(image), len(image[0])
    original_color = image[x][y]

    if original_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        r, c = queue.popleft()
        if (r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color):
            continue

        image[r][c] = new_color

        # 4-kierunkowe sąsiedztwo
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            queue.append((r + dr, c + dc))

# Przykładowe użycie
if __name__ == "__main__":
    image = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    print("Obraz przed DFS:")
    for row in image:
        print(row)

    flood_fill_dfs(image, 0, 0, 2)

    print("\nObraz po DFS:")
    for row in image:
        print(row)

    image = [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]
    ]

    print("\nObraz przed BFS:")
    for row in image:
        print(row)

    flood_fill_bfs(image, 2, 2, 3)

    print("\nObraz po BFS:")
    for row in image:
        print(row)

