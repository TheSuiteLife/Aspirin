"""
Class used for loading
"""

import sys
import pygame
from pygame.locals import K_ESCAPE
from background import BackgroundController, BackgroundView


class LoadingAnimationController(BackgroundController):
    def __init__(self, event_manager, infrastructure):
        BackgroundController.__init__(self, event_manager, infrastructure)
        print self.queue
        print self.view.render
        self.view.render = self.render_with_dim
        print self.view.render
        self.next_controller = "Main Menu"
        self.next_perm_controller = "Background"
        self.view.replay = False
        self.skippable = False
        self.view.finish_video = self.post_action
        self.dim_time = 0
        self.timer = 0


        self.ticker = pygame.time.Clock()
        # self.view.render(10)


    def listen_skip(self):
        self.skippable = True
        self.infrastructure.controller.add_ml_down(self.skip)
        self.infrastructure.controller.add_key_down(K_ESCAPE, self.skip)

    def stop_listen_skip(self):
        if self.skippable:
            self.skippable = False
            self.infrastructure.controller.rem_ml_down(self.skip)
            self.infrastructure.controller.rem_key_down(K_ESCAPE, self.skip)

    def load_video(self, filename, skip=True):
        self.loading_fade()
        self.view.render = self.render_with_dim
        self.view.load_video(filename)
        self.dim_time = self.view.video.get_length() - self.fade_time / 1000.0
        print self.fade_time
        print self.dim_time
        if skip:
            self.listen_skip()

    def load_bg_color(self, color):
        self.view.load_bg_color(color)

    def loading_fade(self):
        self.effects_renderer.force_fade_exponential(self.infrastructure, self.fade_time, 'in')

    def ending_fade(self):
        self.effects_renderer.force_fade_linear(self.infrastructure, self.fade_time, 'out')

    def skip(self, filler):
        self.effects_renderer.stop_effects(self.infrastructure)
        self.post_action()

    def render_with_dim(self, time):
        self.timer += self.ticker.tick()
        print self.timer, 'hello world'
        if not self.view.video.get_busy():
            if self.view.replay:
                self.view.video.rewind()
                self.view.video.play()
            else:
                self.view.finish_video()
        self.infrastructure.view.screen.blit(self.view.surface, (0, 0))

    def post_action(self):
        self.stop_listen_skip()
        self.pause()
        self.ending_fade()
        self.infrastructure.model.load_perm(self.next_perm_controller)
        self.infrastructure.model.load(self.next_controller, None, True)
        self.view.video.stop()
        self.remove()


