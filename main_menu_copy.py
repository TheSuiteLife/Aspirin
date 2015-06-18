"""
Controller for producing the main menu
"""

import pygame
from Base.generics import GenericController, GenericModel, GenericView, MouseClickActionPoster, GenericButton, \
    GenericTextDrawButton
from Macros.functions import load_image


class MainMenuController_Copy(GenericController):
    def __init__(self, event_manager, infrastructure):
        GenericController.__init__(self, event_manager, infrastructure)
        self.model = MainMenuModel(event_manager, infrastructure)
        self.view = MainMenuView(event_manager, infrastructure)

    def pause_extra(self):
        for button in self.view.buttons:
            button.stop_listen()

    def run_extra(self):
        for button in self.view.buttons:
            button.listen()


class MainMenuModel(GenericModel):
    def __init__(self, event_manager, infrastructure):
        GenericModel.__init__(self, event_manager, infrastructure)

    def notify(self, event):
        pass


class MainMenuView(GenericView):
    def __init__(self, event_manager, infrastructure):
        GenericView.__init__(self, event_manager, infrastructure)
        self.weight = 10
        self.buttons = pygame.sprite.Group()
        start_button_image = load_image("Start_Button.png")
        start_button = StartGameButton(infrastructure, start_button_image, [700, 300])
        self.button = GenericTextDrawButton("left", infrastructure, pygame.Rect(0, 0, 300, 200), [200, 400], (0, 0, 0),
                                            (255, 255, 255), 30)
        self.button.add_text("Hello world!", (0, 0, 0), pygame.font.match_font('bitstreamverasans'), 50)
        self.add_button(start_button)

    def add_button(self, button):
        self.buttons.add(button)

    def rem_button(self, button):
        self.buttons.remove(button)

    def render(self, time):
        self.button.render()
        self.buttons.draw(self.infrastructure.view.screen)


class StartGameButton(GenericButton):
    def __init__(self, infrastructure, image, position):
        GenericButton.__init__(self, "left", infrastructure, image, position)
        self.infrastructure = infrastructure
        self.listen()

    def down_action(self):
        pass

    def post_action(self):
        print 'you hit the copy'
        self.infrastructure.model.load("Main Menu")
