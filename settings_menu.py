"""
Omnipresent settings menu that can change settings
"""

from GameFramework.Base.generics import GenericController, GenericModel, GenericView


class SettingsMenuController(GenericController):
    def __init__(self, event_manager, infrastructure):
        GenericController.__init__(self, event_manager, infrastructure)


class SettingsMenuModel(GenericModel):
    def __init__(self, event_manager, infrastructure, settings_manager):
        GenericModel.__init__(self, event_manager, infrastructure)
        self.settings_manager = settings_manager


class SettingsMenuView(GenericView):
    def __init__(self, event_manager, infrastructure):
        GenericView.__init__(self, event_manager, infrastructure)