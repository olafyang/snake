import pygame
import time

display_size = (800, 800)
snake_size = 20
snake_speed = 5  # in pixel

pygame.init()

dis = pygame.display.set_mode(display_size)
pygame.display.set_caption('snake')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

lose_font_style = pygame.font.SysFont(name='loma', size=50)
score_font_style = pygame.font.SysFont(name='loma', size=10)


# def append_to_snake():


def show_score(score):
    score_msg = lose_font_style.render('score: {}'.format(score), True, white)
    dis.blit(score_msg, [0, 0])


def lose_message(msg, color):
    message = lose_font_style.render(msg, True, color)
    dis.blit(message, [display_size[0] / 2, display_size[1] / 2])
    pygame.display.update()


def game_loop():
    player_score = 0

    game_over = False
    quit_game = False

    snake_list = []

    x1 = int(display_size[0] / 2 - snake_size)
    y1 = int(display_size[1] / 2 - snake_size)
    snake_list.append([x1, y1])

    v_x1 = 0
    v_y1 = 0

    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    snake_list.append([snake_list[len(snake_list) - 1][0] + v_x1, snake_list[len(snake_list) - 1][1] + v_y1])
                    player_score += 1
                    continue
                v_x1 = 0
                v_y1 = 0
                if event.key == pygame.K_LEFT:
                    v_x1 = -snake_speed
                elif event.key == pygame.K_UP:
                    v_y1 = -snake_speed
                elif event.key == pygame.K_RIGHT:
                    v_x1 = snake_speed
                elif event.key == pygame.K_DOWN:
                    v_y1 = snake_speed
        if not game_over:
            snake_list[0][0] += v_x1
            snake_list[0][1] += v_y1
            for i, item in enumerate(snake_list):
                if i == 0:
                    continue
                else:
                    snake_list[i][0] = snake_list[i - 1][0] - v_x1
                    snake_list[i][1] = snake_list[i - 1][1] - v_y1

            dis.fill(black)
            for item in snake_list:
                pygame.draw.rect(dis, white, [item[0], item[1], snake_size, snake_size])
            # pygame.draw.rect(dis, white, [snake_list[0][0], snake_list[0][1], snake_size, snake_size])

            show_score(player_score)

            pygame.display.update()

            clock.tick(60)

        # detect if snake hits boundaries
        if snake_list[0][0] >= display_size[0] or snake_list[0][0] < 0 or snake_list[0][1] >= display_size[1] or snake_list[0][1] < 0:
            game_over = True
            lose_message('Game Over', red)

    pygame.quit()
    quit()


game_loop()
