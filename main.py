import pygame

def main():
    pygame.init()

    screen_info = pygame.display.Info()  
    width = screen_info.current_w # Contains information about the width of screen
    height = screen_info.current_h # Contains information about the height of screen

    window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PolyLaser")

    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        window.fill((211, 211, 211))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()





