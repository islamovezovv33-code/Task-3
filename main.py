import pygame

# Инициализация Pygame
pygame.init()

# Создание окна 600x400
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Двигающийся прямоугольник")

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Создание прямоугольника 40x40 с помощью pygame.Rect
rect = pygame.Rect(280, 180, 40, 40)  # Центр экрана
speed = 5

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение нажатых клавиш (постоянное движение при удержании)
    keys = pygame.key.get_pressed()

    # Движение прямоугольника
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование прямоугольника
    pygame.draw.rect(screen, RED, rect)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
