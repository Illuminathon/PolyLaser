import pygame
from src.laser import draw_laser
from src.scene import Scene
from src.text import Text

def main():
    pygame.init()
    pygame.font.init()

    screen_info = pygame.display.Info()  
    width = screen_info.current_w # Contains information about the width of screen
    height = screen_info.current_h # Contains information about the height of screen

    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PolyLaser")

    current_level = Scene(decoration=[Text("PolyLaser", (width // 2, height // 2), 100, (0, 0, 0))])

    run = True
    while run:
        pygame.time.delay(1000 / 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # TODO: przydalyby sie dwie ogolne funckje update/draw no i clear przed draw

        window.fill((211, 211, 211))

        current_level.draw(window, height, width)
        current_level.update()

        draw_laser(window)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()





