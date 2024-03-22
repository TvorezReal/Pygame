import pygame
import random
import sys
pygame.init()

white = (255, 255, 255)
clock = pygame.time.Clock()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # кортеж размеров экрана

pygame.display.set_caption("Игра Тир")  # заголовок окна
icon = pygame.image.load('image/i.jpg')
pygame.display.set_icon(icon)  # иконка в окне

target_image = pygame.image.load('image/target.png')
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 3  # скорость движения
target_speed_y = 3

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0  # счет
running = True
while running:
    screen.fill(color)  # цвет экрана
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # координаты мыши
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    target_x += target_speed_x  # двигаем цель
    target_y += target_speed_y
    if target_x > SCREEN_WIDTH - target_width or target_x < 0:
        target_speed_x = -target_speed_x
    if target_y > SCREEN_HEIGHT - target_height or target_y < 0:
        target_speed_y = -target_speed_y
    screen.blit(target_image, (target_x, target_y))  # рисуем цель

    font = pygame.font.SysFont(None, 55)  # создаем объект шрифта
    text = font.render(f"Счет: {score}", True, white)  # создаем текст
    screen.blit(text, (10, 10))  # рисуем счет
    pygame.display.update()  # обновляем экран

    clock.tick(60)  # 60 кадров в секунду

pygame.quit()
sys.exit()