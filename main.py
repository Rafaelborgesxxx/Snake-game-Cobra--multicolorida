import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Constantes do jogo
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
LIME = (50, 205, 50)
GOLD = (255, 215, 0)

# Direções
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Obstacle:
    def __init__(self, position):
        self.position = position
    
    def get_position(self):
        return self.position

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.colors = [RED]  # Começa com vermelho
        self.direction = RIGHT
        self.grow = False
        self.score = 0
        self.level = 1
        
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        # Verificar colisão com as bordas
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
            
        # Verificar colisão com o próprio corpo
        if new_head in self.body:
            return False
            
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
            # Manter as cores - só remove a cor do segmento removido
            if len(self.colors) > 1:
                self.colors.pop()
        else:
            self.grow = False
            self.score += 10 * self.level  # Pontos baseados no nível
            
        return True
    
    def change_direction(self, new_direction):
        # Impedir movimento na direção oposta
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction
    
    def grow_snake(self, food_color):
        self.grow = True
        # Adiciona a cor da comida ao final da lista de cores
        # Esta cor será mantida permanentemente no segmento
        self.colors.append(food_color)
    
    def get_segment_color(self, index):
        """Retorna a cor para um segmento específico"""
        rainbow_colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK, GOLD, LIME]
        
        # Se temos uma cor específica para este segmento, use-a
        if index < len(self.colors):
            return self.colors[index]
        else:
            # Sistema progressivo de cores
            body_length = len(self.body)
            
            if body_length <= 10:
                # Até 10 segmentos: 1 quadrado por cor
                return rainbow_colors[index % len(rainbow_colors)]
            elif body_length <= 20:
                # 11-20 segmentos: 2 quadrados por cor
                color_index = (index // 2) % len(rainbow_colors)
                return rainbow_colors[color_index]
            elif body_length <= 30:
                # 21-30 segmentos: 3 quadrados por cor
                color_index = (index // 3) % len(rainbow_colors)
                return rainbow_colors[color_index]
            elif body_length <= 40:
                # 31-40 segmentos: 4 quadrados por cor
                color_index = (index // 4) % len(rainbow_colors)
                return rainbow_colors[color_index]
            else:
                # 41+ segmentos: 5 quadrados por cor
                color_index = (index // 5) % len(rainbow_colors)
                return rainbow_colors[color_index]
    
    def get_head_position(self):
        return self.body[0]
    
    def get_body(self):
        return self.body
    
    def get_colors(self):
        return self.colors
    
    def get_score(self):
        return self.score
    
    def get_level(self):
        return self.level
    
    def set_level(self, level):
        self.level = level

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.type = "normal"  # normal, bonus, speed
    
    def generate_position(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        return (x, y)
    
    def respawn(self, snake_body, obstacles):
        while True:
            new_position = self.generate_position()
            if new_position not in snake_body and new_position not in [obs.get_position() for obs in obstacles]:
                self.position = new_position
                # 15% chance de comida especial
                if random.random() < 0.15:
                    self.type = random.choice(["bonus", "speed", "rainbow"])
                else:
                    self.type = "normal"
                break
    
    def get_position(self):
        return self.position
    
    def get_type(self):
        return self.type
    
    def get_color(self):
        if self.type == "bonus":
            return YELLOW
        elif self.type == "speed":
            return PURPLE
        elif self.type == "rainbow":
            # Cores do arco-íris para variedade
            rainbow_colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK, GOLD, LIME]
            return random.choice(rainbow_colors)
        else:
            return RED

class Level:
    def __init__(self, level_num):
        self.level = level_num
        self.obstacles = []
        self.generate_obstacles()
    
    def generate_obstacles(self):
        self.obstacles = []
        num_obstacles = min(self.level * 2, 15)  # Máximo 15 obstáculos
        
        for _ in range(num_obstacles):
            while True:
                x = random.randint(2, GRID_WIDTH - 3)
                y = random.randint(2, GRID_HEIGHT - 3)
                pos = (x, y)
                
                # Evitar posição inicial da cobra
                if pos not in [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]:
                    self.obstacles.append(Obstacle(pos))
                    break
    
    def get_obstacles(self):
        return self.obstacles
    
    def get_level(self):
        return self.level

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game - Cobra Multicolorida')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.reset_game()
    
    def reset_game(self):
        self.snake = Snake()
        self.food = Food()
        self.level_obj = Level(1)
        self.game_over = False
        self.paused = False
        self.speed_boost = False
        self.speed_boost_timer = 0
        self.base_speed = 5  # Velocidade inicial mais lenta
        self.current_speed = self.base_speed
    
    def get_current_speed(self):
        # Velocidade base + aumento gradativo por nível + boost temporário
        body_length = len(self.snake.get_body())
        
        # Velocidade base
        speed = self.base_speed
        
        # Aumento gradativo baseado no tamanho da cobra
        if body_length <= 5:
            speed += 0  # Muito lento no início
        elif body_length <= 10:
            speed += 1  # Um pouco mais rápido
        elif body_length <= 15:
            speed += 2  # Velocidade média
        elif body_length <= 20:
            speed += 3  # Mais rápido
        elif body_length <= 25:
            speed += 4  # Rápido
        elif body_length <= 30:
            speed += 5  # Muito rápido
        else:
            speed += 6  # Máximo de velocidade
        
        # Aumento por nível (fase)
        speed += (self.snake.get_level() - 1) * 1
        
        # Boost temporário
        if self.speed_boost:
            speed += 3
        
        return speed
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                elif not self.paused and not self.game_over:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
        return True
    
    def update(self):
        if self.paused or self.game_over:
            return
        
        # Atualizar boost de velocidade
        if self.speed_boost:
            self.speed_boost_timer -= 1
            if self.speed_boost_timer <= 0:
                self.speed_boost = False
        
        # Mover a cobra
        if not self.snake.move():
            self.game_over = True
            return
        
        # Verificar colisão com obstáculos
        head_pos = self.snake.get_head_position()
        for obstacle in self.level_obj.get_obstacles():
            if head_pos == obstacle.get_position():
                self.game_over = True
                return
        
        # Verificar colisão com a comida
        if self.snake.get_head_position() == self.food.get_position():
            food_color = self.food.get_color()
            self.snake.grow_snake(food_color)
            
            # Efeitos especiais baseados no tipo de comida
            if self.food.get_type() == "bonus":
                self.snake.score += 50  # Bônus extra
            elif self.food.get_type() == "speed":
                self.speed_boost = True
                self.speed_boost_timer = 50  # 5 segundos de boost
            elif self.food.get_type() == "rainbow":
                self.snake.score += 30  # Bônus para comida rainbow
            
            self.food.respawn(self.snake.get_body(), self.level_obj.get_obstacles())
            
            # Subir de nível a cada 5 comidas
            if self.snake.get_score() % (50 * self.snake.get_level()) == 0:
                self.snake.set_level(self.snake.get_level() + 1)
                self.level_obj = Level(self.snake.get_level())
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Removida a grade do dashboard - agora é mais limpo!
        
        # Desenhar obstáculos
        for obstacle in self.level_obj.get_obstacles():
            x, y = obstacle.get_position()
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, GRAY, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Desenhar cobra multicolorida - ARCO-ÍRIS PERMANENTE
        body = self.snake.get_body()
        
        for i, segment in enumerate(body):
            # Cada segmento tem sua própria cor do arco-íris
            color = self.snake.get_segment_color(i)
            
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Desenhar comida
        food_x, food_y = self.food.get_position()
        food_rect = pygame.Rect(food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        food_color = self.food.get_color()
        pygame.draw.rect(self.screen, food_color, food_rect)
        pygame.draw.rect(self.screen, WHITE, food_rect, 1)
        
        # Desenhar informações do jogo
        score_text = self.font.render(f'Pontuação: {self.snake.get_score()}', True, WHITE)
        level_text = self.font.render(f'Fase: {self.snake.get_level()}', True, WHITE)
        speed_text = self.small_font.render(f'Velocidade: {self.get_current_speed()}', True, WHITE)
        colors_text = self.small_font.render(f'Cores: {len(self.snake.get_colors())}', True, WHITE)
        
        # Mostrar velocidade baseada no tamanho
        body_length = len(self.snake.get_body())
        if body_length <= 5:
            speed_info = "Muito Lento"
        elif body_length <= 10:
            speed_info = "Lento"
        elif body_length <= 15:
            speed_info = "Médio"
        elif body_length <= 20:
            speed_info = "Rápido"
        elif body_length <= 25:
            speed_info = "Muito Rápido"
        elif body_length <= 30:
            speed_info = "Ultra Rápido"
        else:
            speed_info = "Máximo"
        
        speed_level_text = self.small_font.render(f'Nível: {speed_info}', True, WHITE)
        
        # Mostrar padrão de cores atual
        body_length = len(self.snake.get_body())
        if body_length <= 10:
            pattern_text = self.small_font.render(f'Padrão: 1 quadrado/cor', True, WHITE)
        elif body_length <= 20:
            pattern_text = self.small_font.render(f'Padrão: 2 quadrados/cor', True, WHITE)
        elif body_length <= 30:
            pattern_text = self.small_font.render(f'Padrão: 3 quadrados/cor', True, WHITE)
        elif body_length <= 40:
            pattern_text = self.small_font.render(f'Padrão: 4 quadrados/cor', True, WHITE)
        else:
            pattern_text = self.small_font.render(f'Padrão: 5 quadrados/cor', True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 50))
        self.screen.blit(speed_text, (10, 90))
        self.screen.blit(speed_level_text, (10, 110))
        self.screen.blit(colors_text, (10, 150))
        self.screen.blit(pattern_text, (10, 190))
        
        # Mostrar boost de velocidade
        if self.speed_boost:
            boost_text = self.small_font.render(f'BOOST DE VELOCIDADE! ({self.speed_boost_timer//10}s)', True, ORANGE)
            self.screen.blit(boost_text, (WINDOW_WIDTH - 300, 10))
        
        # Desenhar mensagens de estado
        if self.paused:
            pause_text = self.font.render('PAUSADO - Pressione ESPAÇO', True, WHITE)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(pause_text, text_rect)
        
        if self.game_over:
            game_over_text = self.font.render('GAME OVER!', True, RED)
            restart_text = self.font.render('Pressione R para reiniciar', True, WHITE)
            final_score_text = self.small_font.render(f'Pontuação Final: {self.snake.get_score()}', True, WHITE)
            final_level_text = self.small_font.render(f'Fase Alcançada: {self.snake.get_level()}', True, WHITE)
            final_colors_text = self.small_font.render(f'Cores Coletadas: {len(self.snake.get_colors())}', True, WHITE)
            
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
            final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            final_level_rect = final_level_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30))
            final_colors_rect = final_colors_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(final_score_text, final_score_rect)
            self.screen.blit(final_level_text, final_level_rect)
            self.screen.blit(final_colors_text, final_colors_rect)
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.get_current_speed())
        
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
