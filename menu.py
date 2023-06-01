import pygame
from sprites import *


class Button:
    def __init__(self, action, image):
        self.action = action
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def get_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Menu:
    def __init__(self, screen, width, height, buttons):
        self.screen = screen
        self.width = width
        self.height = height
        self.buttons = buttons

    def draw(self):
        # Отрисовываем фон меню
        bg_image = pygame.image.load(Sprites.FON)
        bg_image1 = pygame.transform.scale(bg_image, (700, 700))
        bg_rect = bg_image.get_rect()
        self.screen.blit(bg_image1, bg_rect)
        button_top = self.height // 2 - (59 * len(self.buttons))

        # Отрисовываем кнопки
        for index, button in enumerate(self.buttons):
            button.rect = pygame.Rect(self.width // 2 - 73,
                                      button_top + index * 59, 146, 59)
            self.screen.blit(button.image, button.rect),

        pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.get_hovered(mouse_pos):
                            if callable(button.action):
                                button.action()
                            else:
                                print("Clicked button: ", button)

            self.draw()
