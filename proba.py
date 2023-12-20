import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data

from ub_accesible_theme_altair.utils import create_accesible_scheme

import pandas as pd
import altair as alt
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

base = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)

create_accesible_scheme(base, "test")



