import pygame

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

# snake location in window


clock = pygame.time.Clock()

lose_font_style = pygame.font.SysFont(name='loma', size=50)


def lose_message(msg, color):
    message = lose_font_style.render(msg, True, color)
    dis.blit(message, [display_size[0] / 2, display_size[1] / 2])
    pygame.display.update()


def game_loop():
    game_over = False
    quit_game = False

    x1 = display_size[0] / 2 - snake_size
    y1 = display_size[1] / 2 - snake_size

    v_x1 = 0
    v_y1 = 0

    while not quit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True
            if event.type == pygame.KEYDOWN:
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
            x1 = x1 + v_x1
            y1 = y1 + v_y1

            dis.fill(black)
            pygame.draw.rect(dis, white, [x1, y1, snake_size, snake_size])

            pygame.display.update()

            clock.tick(60)

        # detect if snake hits boundaries
        if x1 >= display_size[0] or x1 < 0 or y1 >= display_size[1] or y1 < 0:
            game_over = True
            lose_message('You Lost', red)

    pygame.quit()
    quit()


game_loop()
