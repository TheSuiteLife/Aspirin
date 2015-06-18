"""
Global variables that will probably be passed around everywhere and need to be instantiated
"""
from Infrastructure.infrastructure import Infrastructure
from resources.settings_manager import SettingsManager


infrastructure = Infrastructure([1280, 720], 30)
event_manager = infrastructure.get_event_manager()
settings = SettingsManager()
