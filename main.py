import pygame
from src.laser import draw_laser
from src.scene import Scene
from src.text import Text
from src.button import Button

def main():
    pygame.init()
    pygame.font.init()

    screen_info = pygame.display.Info()  
    width = screen_info.current_w # Contains information about the width of screen
    height = screen_info.current_h # Contains information about the height of screen

    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PolyLaser")

<<<<<<< Updated upstream
<<<<<<< Updated upstream
    current_level = Scene([
        Text("PolyLaser", 100, "Arial", (0, 0, 0), (width // 2 - 200, height // 4)),
        Button("", "Start", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2), lambda: print("Button clicked!"), True),
        Button("", "Exit", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2 + 100), lambda: print("Button clicked!"), True),
    ],[],0,0,0)
=======
    current_level = Scene(decoration=[Text("PolyLaser", 100, None, (0, 0, 0), (width // 2, height // 2))])
>>>>>>> Stashed changes
=======
    current_level = Scene(decoration=[Text("PolyLaser", 100, None, (0, 0, 0), (width // 2, height // 2))])
>>>>>>> Stashed changes

    run = True
    while run:
        pygame.time.delay(16)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # TODO: przydalyby sie dwie ogolne funckje update/draw no i clear przed draw

        window.fill((211, 211, 211))

        current_level.draw(window, height, width)
        current_level.update()

        #draw_laser(window)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()





