import pygame
import random

display_size = (800, 800)
snake_size = 20
snake_speed = 10  # in pixel

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


def show_score(score):
    score_msg = lose_font_style.render('score: {}'.format(score), True, white)
    dis.blit(score_msg, [0, 0])


def lose_message(msg, color):
    message = lose_font_style.render(msg, True, color)
    dis.blit(message, [display_size[0] / 2, display_size[1] / 2])
    pygame.display.update()


def update_display(pos_list, score):
    dis.fill(black)

    # draw
    for item in pos_list:
        pygame.draw.rect(dis, white, [item[0], item[1], snake_size, snake_size])

    show_score(score)
    pygame.display.update()


def generate_food():
    food_pos = [round(random.randrange(1, display_size[0])), round(random.randrange(1, display_size[1]))]
    pygame.draw.rect(dis, blue, [food_pos[0], food_pos[1], snake_size, snake_size])
    pygame.display.update()


def game_loop():
    player_score = 0

    game_over = False
    quit_game = False

    snake_pos_list = []

    x1 = int(display_size[0] / 2 - snake_size)
    y1 = int(display_size[1] / 2 - snake_size)
    snake_pos_list.append([x1, y1])
    v_x1 = 0
    v_y1 = 0

    while not quit_game:
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # code to extend length
                    snake_pos_list.append(
                        [snake_pos_list[0][0], snake_pos_list[0][1]])
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
            # extend snake length
            snake_pos_list[0][0] += v_x1
            snake_pos_list[0][1] += v_y1

            snake_pos_list.append([snake_pos_list[0][0], snake_pos_list[0][1]])
            update_display(snake_pos_list, player_score)
            if len(snake_pos_list) > player_score:
                snake_pos_list.pop(1)

            clock.tick(60)

        # detect if snake hits boundaries
        if snake_pos_list[0][0] >= display_size[0] or snake_pos_list[0][0] < 0 or snake_pos_list[0][1] >= display_size[1] or snake_pos_list[0][1] < 0:
            game_over = True
            lose_message('Game Over', red)
        # detect if snake hits itself
        # for item in snake_pos_list[1:]:
        #     if snake_pos_list[0][0] == item[0] and snake_pos_list[0][1] == item[1]:
        #         game_over = True
        #         lose_message('Game Over', red)

    pygame.quit()
    quit()


game_loop()
