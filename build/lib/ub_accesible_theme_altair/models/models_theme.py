from ub_accesible_theme_altair.models.models_axis import AxisModel
from ub_accesible_theme_altair.models.models_config import ConfigModel
from ub_accesible_theme_altair.models.models_header import HeaderModel
from ub_accesible_theme_altair.models.models_legend import LegendModel
from ub_accesible_theme_altair.models.models_mark import *
from ub_accesible_theme_altair.models.models_range import RangeModel
from ub_accesible_theme_altair.models.models_title import TitleModel
from ub_accesible_theme_altair.models.models_view import ViewModel
from ub_accesible_theme_altair.tokens import COLORS, FONT, FONT_SIZES, OPACITIES, SPACING, STROKE_WIDTHS, \
    COLOR_PRIMITIVES
from ub_accesible_theme_altair.types_theme import Theme, Legend, View, Colors
import altair as alt


class ThemeDaltonismDeuteranopia():
    """
    This class incorporates colors for the type of color blindness - deuteranopia (Absence of GREEN photoreceptors).
    The class is responsible for creating models according to what the Vega-Altair API expects.
    """
    name_theme = 'deuteranopia_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': COLORS['axis'], 'background': COLORS['background'],
                      'text': COLORS['text'],
                      'mark': COLOR_PRIMITIVES["lavender"]["40"],
                      'grid': COLORS['grid'], }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = AxisModel(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0, gridDash=[1, 2],
                            gridOpacity=0.3, tickSize=spacing['md'], titleColor=colors['text'],
                            titleFontSize=font_size['sm']).create_axis()

    header_config = config = HeaderModel(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                         titleColor=colors['text'],
                                         titleFontSize=font_size['md']).create_header()

    legend_config = LegendModel(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()

    range_config = RangeModel(category=COLORS['schemes']['categorical']['ibm'],
                              diverging='purplegreen',
                              heatmap=COLORS["schemes"]["sequential"]['oranges'],
                              ramp=COLORS["schemes"]["sequential"]["oranges"]).create_range()

    title_config = TitleModel(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                              subtitleFontSize=font_size['md']).create_title()
    view_config = ViewModel(stroke='tan').create_view()

    # Mark config
    arc_config = MarkArkModel(stroke=colors['arc']).create_mark_ark()
    bar_config = MarkBarModel(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = MarkLineModel(stroke=colors['mark']).create_mark_line()
    path_config = MarkPathModel(stroke=colors['mark']).create_mark_path()
    point_config = MarkPointModel(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = MarkRectModel(fill=colors["mark"]).create_mark_rect()
    rule_config = MarkRuleModel(stroke=colors['mark']).create_mark_rule()
    shape_config = MarkShapeModel(stroke=colors['mark']).create_mark_shape()
    text_config = MarkTextModel(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = ConfigModel(background=self.colors['background'],
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

    def increse_font_size(self, number: int):
        self.font_size["sm"] += number
        self.font_size["md"] += number
        self.font_size["lg"] += number
        alt.themes.register(self.name_theme, self.get_theme())

    def decrese_font_size(self, number: int):
        self.font_size["sm"] -= number
        self.font_size["md"] -= number
        self.font_size["lg"] -= number

        if self.font_size['sm'] < 0:
            self.font_size["sm"] = 0
        if self.font_size['md'] < 0:
            self.font_size["md"] = 0
        if self.font_size['lg'] < 0:
            self.font_size["lg"] = 0
        alt.themes.register(self.name_theme, self.get_theme())


class ThemeDaltonismProtonopia():
    """
    This class incorporates colors for the type of color blindness - protonopia (Absence of RED photoreceptors).
    The class is responsible for creating models according to what the Vega-Altair API expects.
    """
    name_theme = 'protonopia_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': COLORS['axis'], 'background': COLORS['background'],
                      'text': COLORS['text'],
                      'mark': COLOR_PRIMITIVES["lavender"]["40"],
                      'grid': COLORS['grid'], }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = AxisModel(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0, gridDash=[1, 2],
                            gridOpacity=0.3, tickSize=spacing['md'], titleColor=colors['text'],
                            titleFontSize=font_size['sm']).create_axis()

    header_config = config = HeaderModel(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                         titleColor=colors['text'],
                                         titleFontSize=font_size['md']).create_header()

    legend_config = LegendModel(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()

    range_config = RangeModel(category=COLORS['schemes']['categorical']['ibm'],
                              diverging=COLORS["schemes"]["categorical"]["wong"],
                              heatmap=COLORS["schemes"]["sequential"]['blues'],
                              ramp=COLORS["schemes"]["sequential"]["blues"]).create_range()

    title_config = TitleModel(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                              subtitleFontSize=font_size['md']).create_title()
    view_config = ViewModel(stroke='tan').create_view()

    # Mark config
    arc_config = MarkArkModel(stroke=colors['arc']).create_mark_ark()
    bar_config = MarkBarModel(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = MarkLineModel(stroke=colors['mark']).create_mark_line()
    path_config = MarkPathModel(stroke=colors['mark']).create_mark_path()
    point_config = MarkPointModel(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = MarkRectModel(fill=colors["mark"]).create_mark_rect()
    rule_config = MarkRuleModel(stroke=colors['mark']).create_mark_rule()
    shape_config = MarkShapeModel(stroke=colors['mark']).create_mark_shape()
    text_config = MarkTextModel(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = ConfigModel(background=self.colors['background'],
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

    def increse_font_size(self, number: int):
        self.font_size["sm"] += number
        self.font_size["md"] += number
        self.font_size["lg"] += number
        alt.themes.register(self.name_theme, self.get_theme())

    def decrese_font_size(self, number: int):
        self.font_size["sm"] -= number
        self.font_size["md"] -= number
        self.font_size["lg"] -= number

        if self.font_size['sm'] < 0:
            self.font_size["sm"] = 0
        if self.font_size['md'] < 0:
            self.font_size["md"] = 0
        if self.font_size['lg'] < 0:
            self.font_size["lg"] = 0
        alt.themes.register(self.name_theme, self.get_theme())


class ThemeDaltonismTritanopia():
    """
    This class incorporates colors for the type of color blindness - tritanopia (Absence of BLUE photoreceptors).
    The class is responsible for creating models according to what the Vega-Altair API expects.
    """
    name_theme = 'tritanopia_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': COLORS['axis'], 'background': COLORS['background'],
                      'text': COLORS['text'],
                      'mark': COLOR_PRIMITIVES["teal"]["40"], 'grid': COLORS['grid'], }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = AxisModel(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0, gridDash=[1, 2],
                            gridOpacity=0.3, tickSize=spacing['md'], titleColor=colors['text'],
                            titleFontSize=font_size['sm']).create_axis()

    header_config = config = HeaderModel(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                         titleColor=colors['text'],
                                         titleFontSize=font_size['md']).create_header()

    legend_config = LegendModel(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()

    range_config = RangeModel(category=COLORS['schemes']['categorical']['ibm'],
                              diverging=COLORS["schemes"]["categorical"]["tol"],
                              heatmap=COLORS["schemes"]["sequential"]['reds'],
                              ramp=COLORS["schemes"]["sequential"]["reds"]).create_range()

    title_config = TitleModel(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                              subtitleFontSize=font_size['md']).create_title()
    view_config = ViewModel(stroke='tan').create_view()

    # Mark config
    arc_config = MarkArkModel(stroke=colors['arc']).create_mark_ark()
    bar_config = MarkBarModel(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = MarkLineModel(stroke=colors['mark']).create_mark_line()
    path_config = MarkPathModel(stroke=colors['mark']).create_mark_path()
    point_config = MarkPointModel(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = MarkRectModel(fill=colors["mark"]).create_mark_rect()
    rule_config = MarkRuleModel(stroke=colors['mark']).create_mark_rule()
    shape_config = MarkShapeModel(stroke=colors['mark']).create_mark_shape()
    text_config = MarkTextModel(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = ConfigModel(background=self.colors['background'],
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

    def increse_font_size(self, number: int):
        self.font_size["sm"] += number
        self.font_size["md"] += number
        self.font_size["lg"] += number
        alt.themes.register(self.name_theme, self.get_theme())

    def decrese_font_size(self, number: int):
        self.font_size["sm"] -= number
        self.font_size["md"] -= number
        self.font_size["lg"] -= number

        if self.font_size['sm'] < 0:
            self.font_size["sm"] = 0
        if self.font_size['md'] < 0:
            self.font_size["md"] = 0
        if self.font_size['lg'] < 0:
            self.font_size["lg"] = 0
        alt.themes.register(self.name_theme, self.get_theme())


class ThemeAccesible():
    """
    This class incorporates colors trying to be accesible to most of the colour blindness, and other sight conditions
    The class is responsible for creating models according to what the Vega-Altair API expects.
    """
    name_theme = 'accesible_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': COLORS['axis'], 'background': COLORS['background'],
                      'text': COLORS['text'],
                      'mark': COLORS['mark'], 'grid': COLORS['grid'], }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = AxisModel(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0, gridDash=[1, 2],
                            gridOpacity=0.3, tickSize=spacing['md'], titleColor=colors['text'],
                            titleFontSize=font_size['sm']).create_axis()

    header_config = config = HeaderModel(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                         titleColor=colors['text'],
                                         titleFontSize=font_size['md']).create_header()

    legend_config = LegendModel(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()

    range_config = RangeModel(category=COLORS['schemes']['categorical']['qualitative'],
                              diverging=COLORS["schemes"]["categorical"]["tol"],
                              heatmap=COLORS["schemes"]["sequential"]['blues'],
                              ramp=COLORS["schemes"]["sequential"]["blues"]).create_range()

    title_config = TitleModel(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                              subtitleFontSize=font_size['md']).create_title()
    view_config = ViewModel(stroke='tan').create_view()

    # Mark config
    arc_config = MarkArkModel(stroke=colors['arc']).create_mark_ark()
    bar_config = MarkBarModel(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = MarkLineModel(stroke=colors['mark']).create_mark_line()
    path_config = MarkPathModel(stroke=colors['mark']).create_mark_path()
    point_config = MarkPointModel(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = MarkRectModel(fill=colors["mark"]).create_mark_rect()
    rule_config = MarkRuleModel(stroke=colors['mark']).create_mark_rule()
    shape_config = MarkShapeModel(stroke=colors['mark']).create_mark_shape()
    text_config = MarkTextModel(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = ConfigModel(background=self.colors['background'],
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

    def increse_font_size(self, number: int):
        self.font_size["sm"] += number
        self.font_size["md"] += number
        self.font_size["lg"] += number
        alt.themes.register(self.name_theme, self.get_theme())

    def decrese_font_size(self, number: int):
        self.font_size["sm"] -= number
        self.font_size["md"] -= number
        self.font_size["lg"] -= number

        if self.font_size['sm'] < 0:
            self.font_size["sm"] = 0
        if self.font_size['md'] < 0:
            self.font_size["md"] = 0
        if self.font_size['lg'] < 0:
            self.font_size["lg"] = 0
        alt.themes.register(self.name_theme, self.get_theme())


class DarkThemeAccesible():
    """
    This class incorporates colors trying to be accesible to most of the colour blindness, and other sight conditions in a dark mode
    The class is responsible for creating models according to what the Vega-Altair API expects.
    """
    name_theme = 'accesible_theme'
    colors: Colors = {'arc': '#FFFFFF', 'axis': "#000000", 'background': "#333333",
                      'text': "#000000",
                      'mark': COLOR_PRIMITIVES["blue"]["30"], 'grid': "#000000", }
    font_size: FONT_SIZES = {'sm': FONT_SIZES['sm'], 'md': FONT_SIZES['md'], 'lg': FONT_SIZES['lg']}
    spacing: SPACING = {'sm': SPACING['sm'], 'md': SPACING['md'], 'xl': SPACING['xl']}

    # Variables a cambiar independientes
    axis_config = AxisModel(gridColor=colors['axis'], labelColor=colors['axis'], tickOpacity=1.0, gridDash=[1, 2],
                            gridOpacity=0.4, tickSize=spacing['md'], titleColor=colors['text'],
                            titleFontSize=font_size['sm']).create_axis()

    header_config = config = HeaderModel(labelColor=colors['text'], labelFontSize=font_size['sm'],
                                         titleColor=colors['text'],
                                         titleFontSize=font_size['md']).create_header()

    legend_config = LegendModel(labelColor=colors['axis'], labelFontSize=font_size['sm'], titleColor=colors['text'],
                                titleFontSize=font_size['sm'], titlePadding=spacing['md']).create_legend()

    range_config = RangeModel(category=COLORS['schemes']['categorical']['qualitative'],
                              diverging=COLORS["schemes"]["categorical"]["tol"],
                              heatmap=COLORS["schemes"]["sequential"]['reds'],
                              ramp=COLORS["schemes"]["sequential"]["reds"]).create_range()

    title_config = TitleModel(color=colors["text"], fontSize=font_size["lg"], subtitleColor=colors['text'],
                              subtitleFontSize=font_size['md']).create_title()
    view_config = ViewModel(stroke='tan').create_view()

    # Mark config
    arc_config = MarkArkModel(stroke=colors['arc']).create_mark_ark()
    bar_config = MarkBarModel(fill=colors['mark'], stroke=colors['arc']).create_mark_bar()
    line_config = MarkLineModel(stroke=colors['mark']).create_mark_line()
    path_config = MarkPathModel(stroke=colors['mark']).create_mark_path()
    point_config = MarkPointModel(fill=colors["mark"], filled=True).create_mark_point()
    rect_config = MarkRectModel(fill=colors["mark"]).create_mark_rect()
    rule_config = MarkRuleModel(stroke=colors['mark']).create_mark_rule()
    shape_config = MarkShapeModel(stroke=colors['mark']).create_mark_shape()
    text_config = MarkTextModel(color=colors["text"], fontSize=font_size['sm']).create_mark_text()

    def __init__(self):
        self.config = ConfigModel(background=self.colors['background'],
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

    def increse_font_size(self, number: int):
        self.font_size["sm"] += number
        self.font_size["md"] += number
        self.font_size["lg"] += number
        alt.themes.register(self.name_theme, self.get_theme())

    def decrese_font_size(self, number: int):
        self.font_size["sm"] -= number
        self.font_size["md"] -= number
        self.font_size["lg"] -= number

        if self.font_size['sm'] < 0:
            self.font_size["sm"] = 0
        if self.font_size['md'] < 0:
            self.font_size["md"] = 0
        if self.font_size['lg'] < 0:
            self.font_size["lg"] = 0
        alt.themes.register(self.name_theme, self.get_theme())
