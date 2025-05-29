import pygame, sys, random, time

# Configuración general
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 32
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

# Colores
BG_COLOR = (30, 30, 30)
WALL_COLOR = (50, 50, 50)
GOAL_COLOR = (0, 255, 0)
ENEMY_COLOR = (255, 80, 80)

# Inicializar
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laberinto con Muñeco Animado, Enemigos y cronómetro")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# ------- GENERADOR DE LABERINTO -------
def generate_maze(rows, cols):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    visited = set()

    def visit(r, c):
        if 0 <= r < rows and 0 <= c < cols:
            visited.add((r, c))
            maze[r][c] = 0
            dirs = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(dirs)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    wall_r, wall_c = r + dr // 2, c + dc // 2
                    maze[wall_r][wall_c] = 0
                    visit(nr, nc)

    visit(1, 1)
    maze[1][1] = 0
    maze[rows - 2][cols - 2] = 2  # salida
    return maze

maze = generate_maze(ROWS, COLS)

# ------- JUGADOR -------
player_pos = [1, 1]
player_frame = 0
player_frames = []

def make_player_frames():
    for i in range(1):
        surf = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.rect(surf, (100 + i*30, 200, 255), (6, 6, 20, 24), border_radius=6)
        pygame.draw.circle(surf, (255, 255, 255), (16, 10), 6)
        player_frames.append(surf)

make_player_frames()

# -------- ENEMIGOS -------
class Enemy:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.path = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])

    def move(self):
        nx, ny = self.pos[0] + self.path[0], self.pos[1] + self.path[1]
        if 0 <= nx < COLS and 0 <= ny < ROWS and maze[ny][nx] != 1:
            self.pos = [nx, ny]
        else:
            self.path = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])

    def draw(self):
        x, y = self.pos[0]*TILE_SIZE, self.pos[1]*TILE_SIZE
        pygame.draw.rect(screen, ENEMY_COLOR, (x+4, y+4, TILE_SIZE-8, TILE_SIZE-8), border_radius=5)

enemies = [Enemy(COLS - 3, ROWS - 3), Enemy(3, ROWS - 4)]

# FUNCIONES
def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            tile = maze[y][x]
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if tile == 1:
                pygame.draw.rect(screen, WALL_COLOR, rect)
            elif tile == 2:
                pygame.draw.rect(screen, GOAL_COLOR, rect)

def draw_player():
    global player_frame
    frame = player_frames[player_frame // 8 % len(player_frames)]
    px = player_pos[0]*TILE_SIZE
    py = player_pos[1]*TILE_SIZE
    screen.blit(frame, (px, py))

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if 0 <= new_x < COLS and 0 <= new_y < ROWS:
        if maze[new_y][new_x] != 1:
            player_pos[0] = new_x
            player_pos[1] = new_y

# LOOP PRINCIPAL
def main():
    start_time = time.time()
    win = False
    game_over = False

    while True:
        screen.fill(BG_COLOR)
        draw_maze()
        draw_player()

        for enemy in enemies:
            enemy.draw()

        # Cronómetro
        elapsed = time.time() - start_time
        timer_text = font.render(f"Tiempo: {elapsed:.1f}s", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))

        # Verificar condiciones de victoria o derrota
        if maze[player_pos[1]][player_pos[0]] == 2:
            win = True
            game_over = True
        for e in enemies:
            if e.pos == player_pos:
                game_over = True
                win = False

        if game_over:
            msg = "¡Ganaste!" if win else "¡Perdiste!"
            txt = font.render(msg, True, (255, 255, 0))
            screen.blit(txt, (WIDTH/2 - 60, HEIGHT/2))
            pygame.display.flip()
            pygame.time.wait(2500)
            break

        pygame.display.flip()
        clock.tick(12)

        for e in enemies:
            e.move()

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: move_player(-1, 0)
                if event.key == pygame.K_RIGHT: move_player(1, 0)
                if event.key == pygame.K_UP: move_player(0, -1)
                if event.key == pygame.K_DOWN: move_player(0, 1)

        global player_frame
        player_frame += 1

if __name__ == "__main__":
    main()
