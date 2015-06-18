"""
Controller for producing the main menu
"""

import pygame
from Base.generics import GenericController, GenericModel, GenericView, MouseClickActionPoster, GenericButton
from Macros.functions import load_image


class MainMenuController(GenericController):
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

    def run(self):
        GenericController.run(self)
        self.effects_renderer.force_fade_exponential(self.infrastructure, self.fade_time, 'in')
        print self.effects_renderer.rendering_functions


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
        start_button = StartGameButton(infrastructure, infrastructure.controller, start_button_image, [300, 300])
        self.add_button(start_button)

    def add_button(self, button):
        self.buttons.add(button)

    def rem_button(self, button):
        self.buttons.remove(button)

    def render(self, time):
        self.buttons.draw(self.infrastructure.view.screen)


class StartGameButton(GenericButton):
    def __init__(self, infrastructure, input_controller, image, position):
        GenericButton.__init__(self, "left", input_controller, image, position)
        self.infrastructure = infrastructure
        self.listen()

    def down_action(self):
        pass

    def post_action(self):
        print 'you hit the main menu'
        self.infrastructure.model.load("Main Menu Copy")
