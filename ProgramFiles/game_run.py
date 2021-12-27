from ProgramFiles.consts import *
from ProgramFiles.units_sprites import *


def terminate():
    pygame.quit()
    exit(0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    running = True

    player = Player()
    enemy = EnemyLevelOne()
    dx = dy = 0
    count = 1

    first_bg = FirstBg()
    second_bg = SecondBg()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy += -1
                if event.key == pygame.K_DOWN:
                    dy += 1
                if event.key == pygame.K_LEFT:
                    dx += -1
                if event.key == pygame.K_RIGHT:
                    dx += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    dy += 1
                if event.key == pygame.K_DOWN:
                    dy += -1
                if event.key == pygame.K_LEFT:
                    dx += 1
                if event.key == pygame.K_RIGHT:
                    dx += -1

        if count % 15 == 0:
            # ВВылет выстрела
            shot = ProjectileLevelOne(player)

        bg_group.draw(screen)
        bg_group.update()
        player_shots_group.update()
        player.change_pos(dx, dy)

        clock.tick(FPS)

        # Отрисовка
        player_group.draw(screen)
        enemy_group.draw(screen)
        player_shots_group.draw(screen)
        pygame.display.flip()
        count += 1

    terminate()
