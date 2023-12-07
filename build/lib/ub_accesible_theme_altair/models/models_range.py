from typing import List


from ub_accesible_theme_altair.tokens import COLORS
from ub_accesible_theme_altair.types_theme import ScaleRange


class range_model():

    def __init__(self, **kwargs):


        # Establecer valores predeterminados
        self.category = kwargs.get('category', COLORS["schemes"]["categorical"]["default"])
        self.diverging = kwargs.get('diverging', COLORS["schemes"]["diverging"]["tealred"])
        self.heatmap = kwargs.get('heatmap', COLORS["schemes"]["sequential"]["blues"])
        self.ramp = kwargs.get('ramp', COLORS["schemes"]["sequential"]["blues"])

        # Actualizar atributos con kwargs
        self.__dict__.update(kwargs)

    def create_range(self):
        new_range = ScaleRange(
            category=self.category,
            diverging=self.diverging,
            heatmap=self.heatmap,
            ramp=self.ramp
        )
        return new_range
