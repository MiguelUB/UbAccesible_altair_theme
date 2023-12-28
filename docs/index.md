# Getting Started

## Overview

This library is all about giving resources for vega-altair aiming to create
better and more accessible graphs, the library was built investigating both vega-altair and vega-lite API.

It offers resources for programmers such as tools to create new vega-altair themes, built-in accessible themes,
description generators(Powered by BrailleR).

For the user offers limited customization of the graph like select the color scheme, change text size, change graph size

The idea behind the library is that like in vega-altair most of the configurations and details to create the graph are
handle by the library, giving you more time to spend in the data.
The library itself doesn't alter any concept, function or API of vega-altair just add more tools for you to use.

This documentation serve for reference of the resources given after the installation and to help understand more about
what makes a graph accessible.

## Installation

The library and its dependencies can be easy installed, using:

```
pip install accessible-theme
```

After installation the next built-in themes shoud be ready to use:

- accessible_theme
- dark_accessible_theme
- protonopia_theme
- tritanopia_theme
- deuteranopia_theme

You can enable them, using:

``` py
import altair as alt

alt.themes.enable("accessible_theme")
```

## Requirements
The library was built for:
- altair==5.* -
- typing-extensions>=4.0, <5
- jinja2==3.* 
- pyRserve==1.0.*

Also in order to use the generate_description() function is imperative to have R running in the background, and make R have the libraries ggplpot and pyRserve running


## Getting Help

You can browse this documentation via the links in the top navigation panel or by viewing the API page. 
In addition to reading this documentation page, it can be helpful to also browse the source code of this project.

The code source is avaible in Github where you can report any bugs or request features.

## Resources

## Project Philosofy
This project has the same approach as the vega-altair library that is a simple user interface 
which focuses most of the resources in a experience ready to use after installation, but with the posibility to still 
be abel to create something more complex and complete.

