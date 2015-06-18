"""
Controls what the background will be or look like
Everything gets rendered on top of this
"""

import pygame
from pygame.locals import K_ESCAPE
from Base.generics import GenericController, GenericView, GenericModel


class BackgroundController(GenericController):
    def __init__(self, event_manager, infrastructure):
        model = BackgroundModel(event_manager, infrastructure)
        view = BackgroundView(event_manager, infrastructure)
        GenericController.__init__(self, event_manager, infrastructure, model, view)
        self.queue = None

    def pause_extra(self):
        if self.view.video:
            self.view.video.pause()

    def load_video(self, filename, skip=False):
        self.view.load_video(filename)

    def load_bg_color(self, color):
        self.view.load_bg_color(color)

    def run(self):
        if type(self.queue) is str:
            self.load_video(self.queue)
        elif type(self.queue) is tuple:
            self.load_bg_color(self.queue)


class BackgroundModel(GenericModel):
    def __init__(self, event_manager, infrastructure):
        GenericModel.__init__(self, event_manager, infrastructure)


class BackgroundView(GenericView):
    def __init__(self, event_manager, infrastructure):
        GenericView.__init__(self, event_manager, infrastructure)
        self.weight = 0
        self.surface = pygame.Surface(self.infrastructure.view.resolution)
        self.replay = True
        self.video = None

    def rem_from_render(self, weight):
        if self.video:
            GenericView.rem_from_render(self, self.weight)

    def load_video(self, filename):
        self.video = pygame.movie.Movie(filename)
        self.video.set_display(self.surface)
        self.render = self.render_video
        self.add_to_render(self.weight)
        self.video.play()

    def load_bg_color(self, color):
        self.surface.fill(color)
        self.render = self.render_static
        self.add_to_render(self.weight)

    def finish_video(self):
        pass

    def render_video(self, time):
        if not self.video.get_busy():
            if self.replay:
                self.video.rewind()
                self.video.play()
            else:
                self.finish_video()
        self.infrastructure.view.screen.blit(self.surface, (0, 0))

    def render_static(self, time):
        self.infrastructure.view.screen.blit(self.surface, (0, 0))
