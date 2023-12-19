"""Altair theme configuration."""
from ub_accesible_theme_altair.models.models_theme import *

accessible = ThemeAccesible()
dark_accessible = DarkThemeAccesible()
deuteranopia = ThemeDaltonismDeuteranopia()
protonopia = ThemeDaltonismProtonopia()
tritanopia = ThemeDaltonismTritanopia()


def deuteranopia_theme():
    return deuteranopia.get_theme()


def protonopia_theme():
    return protonopia.get_theme()


def tritanopia_theme():
    return tritanopia.get_theme()


def accessible_theme():
    return accessible.get_theme()


def dark_accessible_theme():
    return dark_accessible.get_theme()


print(deuteranopia_theme())
