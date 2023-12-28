# About

## Roadmap

### First approach

When starting this project, the first idea that crossed our minds was to create a completely separate branch of
vega-altair where we could configure the internal files of the library. While this may seem like the logical thing to
do, it is a monumental and unrealistic job for a small team.

The second and more realistic idea was to be able to create a theme that had accessible parameters to be able to
visualize and improve the graphics rendered by vega, however this was limited to returning a dictionary type
object in a function.

### Understanding limitations

The two most important limitations that we imposed on ourselves was to be able to have a library that did not alter the
workflow of altair or projects built with altair, the second was to be able to provide tools so that programmers can
expand the available tools to work with altair.

One big limitation is that the usual way to save charts in HTML in altair is using the canvas tag, although this tag has
nothing wrong with it, it is more limited than the svg tag since the latter is used for example by HighCharts to be able
to give more customization to your graphs by providing fill patterns, custom javascript, description for each element in
the graph, etc. All this only because unlike canvas tag the svg tag has childs for every element while the canvas is
only one tag.

Another limitation we found is that because we try not to touch anything from the vega-altair source code and since we
cannot touch the vega-lite source code either, our library must adapt to both and use the tools that both provide.
With this in mind, ideas such as using fill patterns, giving graphics sounds, among others were also discarded.

### The final approach

So with that in mind we make one step further, taking inspiration from the Feedzai theme and also applying more
organization
when creating a theme.

The next step then focused on creating models to store values that the Vega API expects, tokens like color values,
font sizes and others and finally typing files to ensure that what the models return to us is what was
expected by the API.

With all these new ideas is that we created a simple and organized system of models that use correctly can create a
simple and robust theme, and with these very same models we create 4 accessible themes that attempt to create graphics
more accessible

### Graphs for everyone and beyond

The last thing we thought is that since each person is different and may have different needs or tastes, it was to give
them simple options so that they can customize the graph in their own way. From this idea came the
create_accesible_scheme() function which It is the same as altair.chart.save('test.hml'), since both create an HTML
where the chart is rendered but our function adds options to improve its visualization

## Style, design and inspiration

### Color Schemes

Our biggest inspiration for the color schemes is the color brewer project, vega color schemes and the web Coloring for
Colorblindness

### Vega API, Vega-Altair API

All our models are a direct reference to the Vega API although we only took the parameters that we thought were most
relevant, but that does not prevent us from adding any other attribute that we have not defined but is present in the
Vega API.

### Inspirations

Our first inspiration for creating this theme was the feedzai-altair-theme their project had many hint and guidelines
to use when creating a new theme we like their more refined approach, so we decided to use it as a template for this
project

### Testing

The testing part was only made with plugins of the chrome store to check the efficiency of the graph when it comes down
to visualization, the plugins we use are:

- Web disability simulator
- Funkify
- Daltonimos Amigavel

## FAQS

### Does this library support layered, repeated, concat and facet charts?

While the theme set will have no problems with these kind of charts, the function create_accesible_scheme() does not
support this kind of chart specially the options to change the graph size or color scheme



