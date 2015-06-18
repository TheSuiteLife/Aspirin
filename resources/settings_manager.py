"""
Gets resources from Game/resources
"""


import ConfigParser
from default_settings import PROPERTIES_FILE,   \
    DEFAULT_CONTROLS,                   \
    DEFAULT_CHARACTER,                  \
    DEFAULT_MISSILE,                    \
    DEFAULT_HOMING_MISSILE,            \
    HEADER

class SettingsManager():

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.config.read(PROPERTIES_FILE)
        self.cfgfile = None

    def reset_settings(self):
        self.cfgfile = open(PROPERTIES_FILE, 'w+')
        self.set_settings(DEFAULT_CONTROLS)
        self.set_settings(DEFAULT_CHARACTER)
        self.set_settings(DEFAULT_MISSILE)
        self.set_settings(DEFAULT_HOMING_MISSILE)
        self.config.write(self.cfgfile)
        self.cfgfile.close()

    def refresh(self):
        self.config.read(PROPERTIES_FILE)

    def set_settings(self, settings):
        """
        Assumes the config file is already open
        """
        header = settings.pop(HEADER)
        if header not in self.config.sections():
            self.config.add_section(header)
        for key in settings.keys():
            self.config.set(header, key, settings[key])

    def get_str_setting(self, section, property):
        self.refresh()
        return self.config.get(section, property)

    def get_int_setting(self, section, property):
        self.refresh()
        return self.config.getint(section, property)

    def get_bool_setting(self, section, property):
        self.refresh()
        return self.config.getboolean(section, property)

    def get_float_setting(self, section, property):
        self.refresh()
        return self.config.getfloat(section, property)

