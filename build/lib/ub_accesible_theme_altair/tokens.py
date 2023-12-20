"""Design tokens for the theme and standalone use.
https://vega.github.io/vega/docs/schemes/

https://colorbrewer2.org/#type=sequential&scheme=YlGn&n=3

https://github.com/ajrgodfrey/BrailleR
"""

from typing import Dict

from ub_accesible_theme_altair.types_theme import Color, Colors

FONT: str = "Roboto, Arial, sans-serif"

FONT_SIZES: Dict[str, int] = {"sm": 14, "md": 18, "lg": 22}

OPACITIES: Dict[str, float] = {"md": 0.5}

SYMBOL_SIZE: int = 40

STROKE_WIDTHS: Dict[str, float] = {"sm": 0.5, "md": 1, "lg": 2}

SPACING: Dict[str, int] = {"xs": 1, "sm": 2, "md": 4, "lg": 8, "xl": 20}

COLOR_PRIMITIVES: Dict[str, Color] = {
    "blue": {
        "00": "#E9F1FD",
        "10": "#A6C4F7",
        "20": "#82ACF3",
        "30": "#4C88EE",
        "40": "#2770EB",
        "50": "#1B4EA5",
        "60": "#18448F",
    },
    "red": {
        "00": "#FBEAEA",
        "10": "#EDAAAA",
        "20": "#E58686",
        "30": "#DA5252",
        "40": "#D32F2F",
        "50": "#942121",
        "60": "#811D1D",
    },
    "green": {
        "00": "#E8F3EB",
        "10": "#9FCDAD",
        "20": "#77B98A",
        "30": "#3C9B58",
        "40": "#148636",
        "50": "#0E5E26",
        "60": "#0C5221",
    },
    "yellow": {
        "00": "#FFF9E6",
        "10": "#FFE796",
        "20": "#FFDD6B",
        "30": "#FFCE2B",
        "40": "#FFC400",
        "50": "#B38900",
        "60": "#7F6202",
    },
    "lavender": {
        "00": "#F5EFFD",
        "10": "#D4BDF5",
        "20": "#C2A2F1",
        "30": "#A87AEA",
        "40": "#965FE6",
        "50": "#6943A1",
        "60": "#5C3A8C",
    },
    "teal": {
        "00": "#E6F6F5",
        "10": "#96D9D7",
        "20": "#6BCAC7",
        "30": "#2BB3AE",
        "40": "#00A39E",
        "50": "#00726F",
        "60": "#006360",
    },
    "pink": {
        "00": "#f7cbe0",
        "10": "#ee94c0",
        "20": "#e55d9f",
        "30": "#dc267f",
        "40": "#a71b60",
        "50": "#701240",
        "60": "#390921",
    },
    "orange": {
        "00": "#ffd7be",
        "10": "#ffb07f",
        "20": "#ff883f",
        "30": "#fe6100",
        "40": "#be4900",
        "50": "#7f3000",
        "60": "#3f1800",
    },
    "neutral": {
        "00": "#F0F1F6",
        "10": "#E1E2E7",
        "20": "#B3B7C4",
        "30": "#666F89",
        "40": "#4D5776",
        "50": "#19274E",
        "60": "#000F3A",
    },
}

COLORS: Colors = {
    "arc": "#FFFFFF",
    "axis": COLOR_PRIMITIVES["neutral"]["60"],
    "background": "#E9E8E8",
    "grid": COLOR_PRIMITIVES["neutral"]["60"],
    "mark": COLOR_PRIMITIVES["blue"]["40"],
    "text": COLOR_PRIMITIVES["neutral"]["50"],
    "schemes": {
        "categorical": {
            "default": [
                COLOR_PRIMITIVES["blue"]["40"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["red"]["40"],
                COLOR_PRIMITIVES["yellow"]["40"],
                COLOR_PRIMITIVES["lavender"]["40"],
                COLOR_PRIMITIVES["teal"]["40"],
                COLOR_PRIMITIVES["neutral"]["40"],
            ],
            "qualitative": [
                COLOR_PRIMITIVES["blue"]["20"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["green"]["20"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["red"]["20"],
            ],
            "ibm": [
                COLOR_PRIMITIVES["blue"]["20"],
                COLOR_PRIMITIVES["lavender"]["40"],
                COLOR_PRIMITIVES["pink"]["30"],
                COLOR_PRIMITIVES["orange"]["30"],
                COLOR_PRIMITIVES["yellow"]["40"]
            ],
            'wong': [
                COLOR_PRIMITIVES["neutral"]["60"],
                COLOR_PRIMITIVES["orange"]["20"],
                COLOR_PRIMITIVES["blue"]["20"],
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["yellow"]["20"],
                COLOR_PRIMITIVES["blue"]["50"],
                COLOR_PRIMITIVES["orange"]["40"],
                COLOR_PRIMITIVES["pink"]["20"],
            ],
            'tol': [
                COLOR_PRIMITIVES["lavender"]["60"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["teal"]["40"],
                COLOR_PRIMITIVES["teal"]["20"],
                COLOR_PRIMITIVES["yellow"]["10"],
                COLOR_PRIMITIVES["red"]["20"],
                COLOR_PRIMITIVES["pink"]["30"],
                COLOR_PRIMITIVES["pink"]["50"],
            ]
        },
        "diverging": {
            "bluered": [
                COLOR_PRIMITIVES["blue"]["60"],
                COLOR_PRIMITIVES["blue"]["30"],
                COLOR_PRIMITIVES["blue"]["10"],
                "#FFFFFF",
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["60"],
            ],
            "tealred": [
                COLOR_PRIMITIVES["teal"]["60"],
                COLOR_PRIMITIVES["teal"]["30"],
                COLOR_PRIMITIVES["teal"]["10"],
                "#FFFFFF",
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["60"],
            ],
            "greenlavender": [
                COLOR_PRIMITIVES["green"]["60"],
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["green"]["10"],
                "#FFFFFF",
                COLOR_PRIMITIVES["lavender"]["10"],
                COLOR_PRIMITIVES["lavender"]["30"],
                COLOR_PRIMITIVES["lavender"]["60"],
            ],
        },
        "sequential": {
            "blues": [
                COLOR_PRIMITIVES["blue"]["60"],
                COLOR_PRIMITIVES["blue"]["50"],
                COLOR_PRIMITIVES["blue"]["40"],
                COLOR_PRIMITIVES["blue"]["30"],
                COLOR_PRIMITIVES["blue"]["20"],
                COLOR_PRIMITIVES["blue"]["10"],
                COLOR_PRIMITIVES["blue"]["00"],
            ],
            "greens": [
                COLOR_PRIMITIVES["green"]["60"],
                COLOR_PRIMITIVES["green"]["50"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["green"]["20"],
                COLOR_PRIMITIVES["green"]["10"],
                COLOR_PRIMITIVES["green"]["00"],
            ],
            "reds": [
                COLOR_PRIMITIVES["red"]["60"],
                COLOR_PRIMITIVES["red"]["50"],
                COLOR_PRIMITIVES["red"]["40"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["20"],
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["00"],
            ],
            "yellows": [
                COLOR_PRIMITIVES["yellow"]["60"],
                COLOR_PRIMITIVES["yellow"]["50"],
                COLOR_PRIMITIVES["yellow"]["40"],
                COLOR_PRIMITIVES["yellow"]["30"],
                COLOR_PRIMITIVES["yellow"]["20"],
                COLOR_PRIMITIVES["yellow"]["10"],
                COLOR_PRIMITIVES["yellow"]["00"],
            ],
            "teals": [
                COLOR_PRIMITIVES["teal"]["60"],
                COLOR_PRIMITIVES["teal"]["50"],
                COLOR_PRIMITIVES["teal"]["40"],
                COLOR_PRIMITIVES["teal"]["30"],
                COLOR_PRIMITIVES["teal"]["20"],
                COLOR_PRIMITIVES["teal"]["10"],
                COLOR_PRIMITIVES["teal"]["00"],
            ],
            "lavenders": [
                COLOR_PRIMITIVES["lavender"]["60"],
                COLOR_PRIMITIVES["lavender"]["50"],
                COLOR_PRIMITIVES["lavender"]["40"],
                COLOR_PRIMITIVES["lavender"]["30"],
                COLOR_PRIMITIVES["lavender"]["20"],
                COLOR_PRIMITIVES["lavender"]["10"],
                COLOR_PRIMITIVES["lavender"]["00"],
            ],
            "grays": [
                COLOR_PRIMITIVES["neutral"]["60"],
                COLOR_PRIMITIVES["neutral"]["50"],
                COLOR_PRIMITIVES["neutral"]["40"],
                COLOR_PRIMITIVES["neutral"]["30"],
                COLOR_PRIMITIVES["neutral"]["20"],
                COLOR_PRIMITIVES["neutral"]["10"],
                COLOR_PRIMITIVES["neutral"]["00"],
            ],
            "oranges": [
                COLOR_PRIMITIVES["orange"]["60"],
                COLOR_PRIMITIVES["orange"]["50"],
                COLOR_PRIMITIVES["orange"]["40"],
                COLOR_PRIMITIVES["orange"]["30"],
                COLOR_PRIMITIVES["orange"]["20"],
                COLOR_PRIMITIVES["orange"]["10"],
                COLOR_PRIMITIVES["orange"]["00"],
            ],
            "pinks": [
                COLOR_PRIMITIVES["pink"]["60"],
                COLOR_PRIMITIVES["pink"]["50"],
                COLOR_PRIMITIVES["pink"]["40"],
                COLOR_PRIMITIVES["pink"]["30"],
                COLOR_PRIMITIVES["pink"]["20"],
                COLOR_PRIMITIVES["pink"]["10"],
                COLOR_PRIMITIVES["pink"]["00"],
            ]
        },
    },
}
