# Examples

## Enabling a theme

Enabling the themes that comes with this library is as easy to just enabling them with altair, then you can create 
your chart as you want the avaible themes in this library are:
- accessible_theme
- dark_accessible_theme
- protonopia_theme
- tritanopia_theme
- deuteranopia_theme

```py
import altair as alt
import pandas as pd


alt.themes.enable('accessible_theme')

source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)


```

## Customizing a built-in theme

Each theme comes from a Theme Model defined in this library, so you only need to instance the model and call to the
functions defined to make little customizations to the theme, like this where we change the background color:
```python
import altair as alt

# Changing background color of the accessible_theme
accesible_theme= ThemeAccesible()
accesible_theme.change_background_color('#ffca6f')

alt.themes.enable('accessible_theme')

source = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

alt.Chart(source).mark_bar().encode(
    x='a',
    y='b'
)

```

## Creating a new theme
### Vega-altair way of defining a theme
Creating a new theme is a built-in function in vega-altair all that is need it is a funtion that return a dict object 
with the appropriate keys and values defined in vega-lite, then register the theme and finally enabling it

```python
import altair as alt
from vega_datasets import data

# define the theme by returning the dictionary of configurations
def black_marks():
    return {
        'config': {
            'view': {
                'height': 300,
                'width': 300,
            },
            'mark': {
                'color': 'black',
                'fill': 'black'
            }
        }
    }

# register the custom theme under a chosen name
alt.themes.register('black_marks', black_marks)

# enable the newly registered theme
alt.themes.enable('black_marks')

# draw the chart
cars = data.cars.url
alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)
```

### Acceessilbe-theme way of defining a theme

However, in this library we use a more direct and organized method, in this library there are several models defined 
that correspond to what the vega-lite API expects.
A simple example would be like this
```python
import altair as alt
from vega_datasets import data

# Create new dictionary with the configurations for the axis
axis_config = AxisModel(labelColor='#e7212f', titleColor='#e7212f').create_axis()

# Create a new dictionary of configurations
red_text_axis= ConfigModel(axis=axis_config).create_config()

# Define the theme by return the dictionary with the configurations
def red_axis_theme():
    return red_text_axis


# register the custom theme under a chosen name
alt.themes.register('red_axis_theme', red_axis_theme)

# enable the newly registered theme
alt.themes.enable('red_axis_theme')

# draw the chart
cars = data.cars.url
alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)
                 
```
Check the API page for more information about the avaible models

## Creating an accessible chart for the user
The library comes with a function that uses jinja2 and a custom template where is expected the chart to render.
This function will use chart to create a new HTML with options for the user to custom the graph

```python
import altair as alt
from vega_datasets import data

cars = data.cars.url
base = alt.Chart(cars).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q'
)
create_accesible_scheme(base,'nameOfHtml','Textual description of the graph')
```
## Generate description of a graph