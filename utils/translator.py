import configparser
import os

lng_path = os.path.join(os.getcwd(), "lng")

def translate(language_name, string):
    config = configparser.ConfigParser()
    config.read(os.path.join(lng_path, f"{language_name}.lang"))
    try:
        return config.get("Strings", string)
    except (configparser.NoOptionError, configparser.NoSectionError):
        if string:
            return string
        else:
            raise Exception("language engine error: This translation is corrupt!")
            return 0
