"""Altair theme configuration."""
from ub_accesible_theme_altair.models.models_mark import mark_path_model
from ub_accesible_theme_altair.tokens import COLORS, FONT, FONT_SIZES, OPACITIES, SPACING, STROKE_WIDTHS, \
    COLOR_PRIMITIVES
from ub_accesible_theme_altair.types_theme import Theme, Legend, View, Colors
from ub_accesible_theme_altair.models import *
import altair as alt


class tema_daltonimo_deuteranopia():
    name_theme = 'black_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': COLORS['axis'], 'background': COLORS['background'],
                      'text': COLORS['text'],
                      'mark': COLORS['mark'], 'grid': COLORS['grid'], }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = axis_model(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0,
                             tickSize=spacing['md'], titleColor=colors['text'], titleFontSize=font_size['sm']).create_axis()
    header_config = config = header_model(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                          titleColor=colors['text'],
                                          titleFontSize=font_size['md']).create_header()
    legend_config = legend_model(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                 titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()
    range_config = range_model(category=COLORS['schemes']['categorical']['ibm'],
                               diverging=COLORS["schemes"]["categorical"]["tol"],
                               heatmap=COLORS["schemes"]["sequential"]['oranges'],
                               ramp=COLORS["schemes"]["sequential"]["blues"]).create_range()
    title_config = title_model(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                               subtitleFontSize=font_size['md']).create_title()
    view_config = view_model(stroke='tan').create_view()

    # Mark config
    arc_config = mark_ark_model(stroke=colors['arc']).create_mark_ark()
    bar_config = mark_bar_model(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = mark_line_model(stroke=colors['mark']).create_mark_line()
    path_config = mark_path_model(stroke=colors['mark']).create_mark_path()
    point_config = mark_point_model(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = mark_rect_model(fill=colors["mark"]).create_mark_rect()
    rule_config = mark_rule_model(stroke=colors['mark']).create_mark_rule()
    shape_config = mark_shape_model(stroke=colors['mark']).create_mark_shape()
    text_config = mark_text_model(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = config_model(background=self.colors['background'],
                                   axis=self.axis_config, header=self.header_config,
                                   legend=self.legend_config, range=self.range_config,
                                   title=self.title_config, view=self.view_config,
                                   arc=self.arc_config, bar=self.bar_config,
                                   line=self.line_config, path=self.path_config,
                                   point=self.point_config, rect=self.rect_config,
                                   rule=self.rule_config, shape=self.shape_config,
                                   text=self.text_config)

    def get_theme(self):
        return self.config.create_full_config()

    def change_background_color(self, new_color):
        self.colors['background'] = new_color
        alt.themes.register(self.name_theme, self.get_theme())

    def change_mark_color(self, new_color):
        self.colors['mark'] = new_color
        alt.themes.register(self.name_theme, self.get_theme())

    def change_text_color(self, new_color):
        self.colors['text'] = new_color
        alt.themes.register(self.name_theme, self.get_theme())

    """def re_register(self):
        pass

    def accept_json(self):
        pass

    def __str__(self):
        pass"""


def my_theme():
    return {
        'config': {
            'view': {
                'height': 300,
                'width': 400,
            },
            'mark': {
                'color': 'black',
                'fill': '#000000',
            },
            'axisLeft': {
                'labelFontSize': 30,
            },
        }
    }


def accesible_theme() -> Theme:
    """Feedzai theme (light theme)."""
    return {
        "config": {
            # Guides
            "axis": {
                "domain": True,
                "domainColor": COLORS["axis"],
                "grid": False,
                "gridCap": "round",
                "gridColor": COLORS["grid"],
                "gridDash": [2, 4],
                "gridWidth": STROKE_WIDTHS["sm"],
                "labelColor": COLORS["axis"],
                "labelFont": FONT,
                "labelPadding": SPACING["sm"],
                "tickColor": COLORS["axis"],
                "tickOpacity": OPACITIES["md"],
                "tickSize": SPACING["md"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
            },
            "axisBand": {"domain": True, "labelPadding": SPACING["md"], "ticks": False},
            "axisY": {
                "domain": False,
                "titleAlign": "left",
                "titleAngle": 0,
                "titleX": -20,
                "titleY": -10,
            },
            "legend": {
                "labelColor": COLORS["axis"],
                "labelFont": FONT,
                "labelFontSize": FONT_SIZES["sm"],
                "symbolSize": 40,
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
                "titlePadding": SPACING["md"],
            },
            # Marks
            "arc": {"stroke": COLORS["arc"], "strokeWidth": STROKE_WIDTHS["md"]},
            "bar": {"fill": COLORS["mark"], "stroke": None},
            "line": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["lg"]},
            "path": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["sm"]},
            "point": {"fill": COLORS["mark"], "shape": "circle", "filled": True},
            "rect": {"fill": COLORS["mark"]},
            "rule": {"stroke": COLORS["axis"]},
            "shape": {"stroke": COLORS["mark"]},
            "text": {
                "color": COLORS["text"],
                "font": FONT,
                "fontSize": FONT_SIZES["sm"],
            },
            # Color scales
            "range": {
                "category": COLORS["schemes"]["categorical"]["default"],
                "diverging": COLORS["schemes"]["diverging"]["tealred"],
                "heatmap": COLORS["schemes"]["sequential"]["blues"],
                "ramp": COLORS["schemes"]["sequential"]["blues"],
            },
            # Chart
            "background": COLORS["background"],
            "header": {
                "labelColor": COLORS["text"],
                "labelFont": FONT,
                "labelFontSize": FONT_SIZES["sm"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["md"],
            },
            "title": {
                "anchor": "start",
                "color": COLORS["text"],
                "font": FONT,
                "fontSize": FONT_SIZES["lg"],
                "fontWeight": "bold",
                "offset": SPACING["xl"],
                "subtitleColor": COLORS["text"],
                "subtitleFontSize": FONT_SIZES["md"],
            },
            "view": {
                "continuousHeight": 300,
                "continuousWidth": 400,
                "stroke": "transparent",
            },
        }
    }


gg = tema_daltonimo_deuteranopia()


def black_theme():
    return gg.get_theme()


print(black_theme())
