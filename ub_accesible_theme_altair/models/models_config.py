from ub_accesible_theme_altair.models.models_axis import axis_model
from ub_accesible_theme_altair.models.models_header import header_model
from ub_accesible_theme_altair.models.models_legend import legend_model
from ub_accesible_theme_altair.models.models_range import range_model
from ub_accesible_theme_altair.models.models_title import title_model
from ub_accesible_theme_altair.models.models_view import view_model
from ub_accesible_theme_altair.types_theme import Config, Axis, Legend, ScaleRange, Header, Title, View


class config_model():

    def __init__(self, **kwargs):
        self._required_params = {
            'axis': Axis,
            'legend': Legend,
            'range': ScaleRange,
            'background': str,
            'header': Header,
            'title': Title,
            'view': View
        }

        # Establecer valores predeterminados
        self.axis = kwargs.get('axis', axis_model().create_axis())
        self.legend = kwargs.get('legend', legend_model().create_legend())
        self.range = kwargs.get('range', range_model().create_range())
        self.background = kwargs.get('background', '#FFFFFF')
        self.header = kwargs.get('header', header_model().create_header())
        self.title = kwargs.get('title', title_model().create_title())
        self.view = kwargs.get('view', view_model().create_view())

        # Actualizar atributos con kwargs
        self.__dict__.update(kwargs)

        '''# Verificar tipos de datos para los parámetros obligatorios
        for param, expected_type in self._required_params.items():
            if param in kwargs and not isinstance(getattr(self, param), expected_type):
                raise TypeError(f"Se esperaba '{param}' como tipo {expected_type}.")
        '''
        # Verificar que los parámetros obligatorios tengan valores
        missing_params = [param for param, expected_type in self._required_params.items() if
                          getattr(self, param, None) is None]
        if missing_params:
            raise ValueError(
                f"Los siguientes parámetros son obligatorios y no fueron proporcionados: {missing_params}")

    def create_config(self):
        new_config = {'config': Config(
            axis=self.axis,
            legend=self.legend,
            range=self.range,
            background=self.background,
            header=self.header,
            title=self.title,
            view=self.view
        )}
        return new_config

    def create_full_config(self):
        """
        This configuration return all parameters inserted when the class was created, make sure the parameters entered,
        are the same as described in vega-altair altair.Config
        :return (dict): A dictioanry with all the configuration ready to register and enable
        """
        result_dict = self.__dict__.copy()
        result_dict.pop('_required_params', None)
        return {"config":result_dict}

    def __str__(self):
        return str(self.create_full_config())
