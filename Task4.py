import pygame

# Инициализация Pygame
pygame.init()

# Создание окна 800x600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello Pygame")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифт для текста
font = pygame.font.Font(None, 48)

# Текст "Hello, Pygame!" по центру
text = font.render("Hello, Pygame!", True, WHITE)
text_rect = text.get_rect(center=(400, 300))

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка текста (всегда на экране)
    screen.blit(text, text_rect)

    # Обновление экрана
    pygame.display.update()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
