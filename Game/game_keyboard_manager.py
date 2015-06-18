"""
Handles keyboard input
"""

import pygame
from GameFramework.Resources.key_translation import PYGAME_KEYS

class GameKeyboardManager():
    def __init__(self, event_manager, infrastructure, settings_manager):
        self.event_manager = event_manager
        self.infrastructure = infrastructure
        self.input_controller = infrastructure.controller
        self.settings_manager = settings_manager

        # Initialize instance variables
        self.controls = self.update_controls()

        self.key_presses = [0] * 5
        self.direction = 0
        self.listening = False

    def listen(self):
        for key in self.controls:
            self.input_controller.add_key_down(key, self.key_down_listener)
            self.input_controller.add_key_up(key, self.key_up_listener)
        self.listening = True

    def stop_listen(self):
        for key in self.controls:
            self.input_controller.rem_key_down(key, self.key_down_listener)
            self.input_controller.rem_key_up(key, self.key_up_listener)
        self.listening = False


    def update_settings(self):
        if self.listening:
            self.stop_listen()
        self.controls = self.update_controls()
        self.listen()

    def update_controls(self):
        return [PYGAME_KEYS[self.settings_manager.get_str_setting('Controls', 'up')],
                PYGAME_KEYS[self.settings_manager.get_str_setting('Controls', 'right')],
                PYGAME_KEYS[self.settings_manager.get_str_setting('Controls', 'down')],
                PYGAME_KEYS[self.settings_manager.get_str_setting('Controls', 'left')],
                PYGAME_KEYS[self.settings_manager.get_str_setting('Controls', 'focus')]]

    def key_press_order(self, key_presses):
        # Checks which key had most recently been pressed
        return max(key_presses[0],
                   key_presses[1],
                   key_presses[2],
                   key_presses[3])

    def update_key_presses(self, direction):
        # Update the keys that are being pressed
        key = abs(direction)
        if direction < 1:
            # Set to zero if the key had been released
            self.key_presses[key - 1] = 0
        else:
            # Set to next highest value if the key had been pressed
            self.key_presses[key - 1] = self.key_press_order(self.key_presses) + 1
        self.find_direction()

    def find_direction(self):
        # Update the direction based on the key presses
        if self.key_presses[:4] != [0] * 4:
            # Sets the direction to the most recently pressed direction
            if self.key_presses[0] > self.key_presses[2] \
                    and self.key_presses[1] == 0 and self.key_presses[3] == 0:
                self.direction = 0
            elif self.key_presses[0] < self.key_presses[2] \
                    and self.key_presses[1] == 0 and self.key_presses[3] == 0:
                self.direction = 2
            elif self.key_presses[1] > self.key_presses[3] \
                    and self.key_presses[0] == 0 and self.key_presses[2] == 0:
                self.direction = 1
            elif self.key_presses[1] < self.key_presses[3] \
                    and self.key_presses[0] == 0 and self.key_presses[2] == 0:
                self.direction = 3
                # Diagonals
            elif self.key_presses[0] > self.key_presses[2] \
                    and self.key_presses[1] > self.key_presses[3]:
                self.direction = 4
            elif self.key_presses[0] < self.key_presses[2] \
                    and self.key_presses[1] > self.key_presses[3]:
                self.direction = 5
            elif self.key_presses[1] < self.key_presses[3] \
                    and self.key_presses[0] < self.key_presses[2]:
                self.direction = 6
            else:
                self.direction = 7
        else:
            self.direction = -1

    # ---------------------------------------------------------------------- #
    # Event handling

    def key_down_listener(self, key):
        self.update_key_presses(self.controls.index(key) + 1)

    def key_up_listener(self, key):
        self.update_key_presses(-self.controls.index(key) - 1)
