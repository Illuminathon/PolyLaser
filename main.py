import pygame
import sys
from src.laser import draw_laser
from src.scene import Scene
from src.text import Text
from src.button import Button

NONE = Scene([], [], 0, 0, 0)

current_level = NONE

def set_current_level(level: Scene):
    global current_level
    current_level = level

def main():
    global current_level

    pygame.init()
    pygame.font.init()

    screen_info = pygame.display.Info()  
    width = screen_info.current_w
    height = screen_info.current_h

    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PolyLaser")

    MAIN_MENU = Scene([
        Text("PolyLaser", 100, "Arial", (0, 0, 0), (width // 2 - 200, height // 4)),
    ],[
        Button("", "Start", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2), 200, 50, lambda: set_current_level(LEVEL_SELECT), True),
        Button("", "Exit", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2 + 100), 200, 50, lambda: sys.exit(), True)
    ],0,0,0)

    LEVEL_SELECT = Scene([
        Text("Level Select", 100, "Arial", (0, 0, 0), (width // 2 - 200, height // 4)),
    ],[
        Button("", "Level 1", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2), 200, 50, lambda: print("Level 1 clicked!"), True),
        Button("", "Level 2", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2 + 100), 200, 50, lambda: print("Level 2 clicked!"), True),
        Button("", "Back", 50, "Arial", (0, 0, 0), (width // 2 - 100, height // 2 + 200), 200, 50, lambda: set_current_level(MAIN_MENU), True)
    ],0,0,0)

    current_level = MAIN_MENU

    mouse_pos_text = Text("Mouse pos: 0,0", 50, "Arial", (0, 0, 0), (200, 100))

    run = True
    while run:
        pygame.time.delay(16)

        mouse_pos_text.update_text(f"Mouse pos: {pygame.mouse.get_pos()[0]},{pygame.mouse.get_pos()[1]}")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # TODO: przydalyby sie dwie ogolne funckje update/draw no i clear przed draw

        window.fill((211, 211, 211))

        current_level.draw(window, height, width)
        current_level.update()

        mouse_pos_text.draw(window, height, width)

        #draw_laser(window)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()





