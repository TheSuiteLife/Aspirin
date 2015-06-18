"""
Executes the infrastructural parts
"""
import pygame
import os
from main_menu import MainMenuController
from main_menu_copy import MainMenuController_Copy
from background import BackgroundController
from loading_animation import LoadingAnimationController
from resources.settings_manager import SettingsManager
from Game.game_keyboard_manager import GameKeyboardManager


from singletons import infrastructure, event_manager, settings

rect = pygame.Rect(0, 0, 500, 500)


pygame.init()
if __name__ == '__main__':
    pygame.display.set_caption("Aspirin")
    loading_animation = LoadingAnimationController(event_manager, infrastructure)
    background = BackgroundController(event_manager, infrastructure)
    game_keyboard = GameKeyboardManager(event_manager, infrastructure, settings)
    main_menu_1 = MainMenuController(event_manager, infrastructure)
    main_menu_2 = MainMenuController_Copy(event_manager, infrastructure)

    settings.reset_settings()
    loading_animation.queue = os.path.join("resources", "Cinematics", "jon.mpg")
    game_keyboard.listen()
    infrastructure.model.load("Main Menu", main_menu_1)
    infrastructure.model.load("Main Menu Copy", main_menu_2)

    infrastructure.model.load_perm("Background", background)
    infrastructure.model.load("Loading", loading_animation)
    background.queue = os.path.join("resources", "Cinematics", "jon.mpg")
    infrastructure.model.pause_all()
    infrastructure.model.load("Loading")
    del loading_animation

    infrastructure.run_main()


"""
Under this part, all the controllers should be loaded and then paused (I guess), remember that each one has a function
to load the next controller etc.

The background controller can also be paused
"""