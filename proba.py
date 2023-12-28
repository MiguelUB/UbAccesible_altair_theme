import altair as alt
from vega_datasets import data

from ub_accesible_theme_altair.models.models_theme import DarkAccessibleTheme, PrintFriendlyTheme
from ub_accesible_theme_altair.utils import create_accesible_scheme

tema = PrintFriendlyTheme()


def getTheme():
    return tema.get_theme()


alt.themes.register('dd', getTheme)
alt.themes.enable('dd')
source = data.barley()

chart = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='sum(yield):Q',
    color='year:N',
    column='site:N'
)

# Mostrar el gráfico
chart.save('proba.html')
create_accesible_scheme(chart,'test')
