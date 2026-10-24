import pygame
import os

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        
        self.title_font = pygame.font.Font(None, 80)
        self.button_font = pygame.font.Font(None, 40)
        
        bg_path = os.path.join("src", "menu_bg.png")
        try:
            self.bg_image = pygame.image.load(bg_path).convert()
            self.bg_image = pygame.transform.scale(self.bg_image, (screen_width, screen_height))
        except (pygame.error, FileNotFoundError):
            self.bg_image = None

        button_width, button_height = 220, 60
        self.play_button = pygame.Rect(
            (screen_width - button_width) // 2, 
            (screen_height - button_height) // 2 + 50, 
            button_width, 
            button_height
        )

    def draw(self, surface):
        if self.bg_image:
            surface.blit(self.bg_image, (0, 0))
        else:
            surface.fill((15, 15, 20))

        title_text = "POLYLASER"
        
        shadow_surf = self.title_font.render(title_text, True, (0, 0, 0))
        surface.blit(shadow_surf, (self.width // 2 - shadow_surf.get_width() // 2 + 3, 153))
        
        title_surf = self.title_font.render(title_text, True, (0, 255, 255))
        surface.blit(title_surf, (self.width // 2 - title_surf.get_width() // 2, 150))

        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.play_button.collidepoint(mouse_pos)
        
        button_color = (0, 180, 180) if is_hovered else (0, 120, 120)
        border_color = (0, 255, 255) if is_hovered else (0, 180, 180)

        pygame.draw.rect(surface, button_color, self.play_button, border_radius=8)
        pygame.draw.rect(surface, border_color, self.play_button, width=2, border_radius=8)

        btn_text_surf = self.button_font.render("GRAJ", True, (255, 255, 255))
        surface.blit(
            btn_text_surf, 
            (
                self.play_button.centerx - btn_text_surf.get_width() // 2, 
                self.play_button.centery - btn_text_surf.get_height() // 2
            )
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.play_button.collidepoint(event.pos):
                    return "PLAY"
        return None

