import json
import os

from altair import Chart

from jinja2 import Template
import pandas as pd
import altair as alt
from vega_datasets import data

accesible_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vega-Altair Graphic</title>
    <!-- Incluye Vega y Vega-Lite desde CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
    <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            <style>
    /* Apply background to the selector */
    option.default {
      background: linear-gradient(to right, red, blue);
      padding: 5px;
      color: white;
    }
  </style>

</head>
</head>
<body>
<div class="container mt-5">
    <!-- Selectors for Graph-->

    <div class="row ">
        <div class="col-md-6">
            <!-- Color Scheme Selector -->
            <div class="form-group my-1">
                <label for="selector">Scheme selector:</label>
                <select class="form-control" id="selector" aria-labelledby="selectorLabel">
                    <option  value="option1">Default
                    </option>
                    <option value="option2">category20b</option>
                    <option value="option3">viridis</option>
                </select>
            </div>
            <div >
                <!-- Height and Width -->
                <label for="heightGraphInput">Height:</label>
                <input type="range" id="heightGraphInput" min="0" max="1000" value="300" step="50">
                <label for="widthGraphInput">Width:</label>
                <input type="range" id="widthGraphInput" min="0" max="1000" value="300" step="50">
            </div>
                <!-- Change Text Size -->
            <div class="btn-group my-1" role="group" aria-label="Change text size">
                <button id="decreaseSizeText" class="btn btn-primary">Decrease</button>
                <button id="increaseSizeText" class="btn btn-primary">Increase</button>
            </div>
        </div>
    </div>
    <!-- Accessible Graph -->
    <div class="row my-2">
        <div class="col-md-6">
            <div id="chart"></div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <p>Layered charts does not support color schemes changes</p>
                <p>Changing size in layeres, concat, repeated, facet chart may vary the effect</p>
            </div>
        </div>
    </div>
    <!-- Basic variables -->
    <script>
        const el = document.getElementById('chart');
        let fontSizes = {"sm": 12, "md": 14, "lg": 18}
        var $heightGraphInput = $("#heightGraphInput");
        var $widthGraphInput = $("#widthGraphInput");
        var $buttonIncrease = $("#increaseSizeText");
        var $buttonDecrease = $("#decreaseSizeText");
        let spec = {{ chart | tojson }};
        let description = "{{ description }}"
        let embedOpt = {"mode": "vega-lite"};
        let defaultScheme = null
        if (spec.encoding.hasOwnProperty('color')) {
            if (spec.encoding.color.hasOwnProperty('scale')) {
                defaultScheme = spec.encoding.color.scale
            } else {
                spec.encoding.color["scale"] = {"scheme": "blues"}
                defaultScheme = spec.encoding.color["scale"] = {"scheme": "blues"}
            }
        }
        if(!spec.hasOwnProperty("description")){
            spec.description=description
        }

    </script>

    <!--  Auxiliar functions-->
    <script>
        function showError(el, error) {
            el.innerHTML = ('<div style="color:red;">'
                + '<p>JavaScript Error: ' + error.message + '</p>'
                + "<p>This usually means there's a typo in your chart specification. "
                + "See the javascript console for the full traceback.</p>"
                + '</div>');
            throw error;
        }

        function changeHeight() {
            let newHeight = $heightGraphInput.val();
            spec["height"] = newHeight

            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
        }

        function changeWidth() {
            let newWidth = $widthGraphInput.val();
            spec["width"] = newWidth

            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
        }

        function biggerFontSize() {
            fontSizes.sm += 2
            fontSizes.md += 2
            fontSizes.lg += 2
            // change axis size
            spec.config['axis'] = {...spec.config.axis, 'labelFontSize': fontSizes.sm, 'titleFontSize': fontSizes.md}
            // change title size
            spec.config['title'] = {...spec.config.title, 'fontSize': fontSizes.lg}
            // change legend size
            spec.config['legend'] = {
                ...spec.config.legend,
                'labelFontSize': fontSizes.sm,
                'titleFontSize': fontSizes.md
            }
            // change text mark size
            spec.config['text'] = {...spec.config.text, 'fontSize': fontSizes.sm}
            // change header size
            spec.config['header'] = {
                ...spec.config.header,
                'labelFontSize': fontSizes.sm,
                'titleFontSize': fontSizes.md
            }


            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));

        }

        function smallerFontSize() {
            fontSizes.sm -= 2
            fontSizes.md -= 2
            fontSizes.lg -= 2
            // change axis size
            spec.config['axis'] = {...spec.config.axis, 'labelFontSize': fontSizes.sm, 'titleFontSize': fontSizes.md}
            // change title size
            spec.config['title'] = {...spec.config.title, 'fontSize': fontSizes.lg}
            // change legend size
            spec.config['legend'] = {
                ...spec.config.legend,
                'labelFontSize': fontSizes.sm,
                'titleFontSize': fontSizes.md
            }
            // change text mark size
            spec.config['text'] = {...spec.config.text, 'fontSize': fontSizes.sm}
            // change header size
            spec.config['header'] = {
                ...spec.config.header,
                'labelFontSize': fontSizes.sm,
                'titleFontSize': fontSizes.md
            }
            
            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));

        }
    </script>
    
    <!-- Main sript -->
    <script>
        // Color scheme selector
        $(document).ready(function () {
            if (defaultScheme != null) {
                $('#selector').change(function () {
                    var opcionSeleccionada = $(this).val();
                    switch (opcionSeleccionada) {
                        case 'option1':
                            spec.encoding.color.scale = defaultScheme
                            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                            break;
                        case 'option2':

                            spec.encoding.color.scale = {"scheme": "category20b"}
                            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                            break;
                        case 'option3':
                            spec.encoding.color.scale = {"scheme": "viridis"}
                            vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                            break;
                        default:
                            console.log("The selected option does not correspond any color scheme")
                            break;

                    }

                });
            }
        });
        
        vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
        $heightGraphInput.on("input", changeHeight);
        $widthGraphInput.on("input", changeWidth);
        $buttonIncrease.on("click", biggerFontSize);
        $buttonDecrease.on("click", smallerFontSize);

    </script>
</body>
</html>


"""


def create_accesible_scheme(chart: Chart, filename='test', description='Esta es una simple descripcion'):
    """
    This function will create a HTML file in the root of the project, this HTML file will contain the vega lite style
    graphic using the information from the vega-altair Chart passed.
    The new HTML file contains some option for the user to  change the color scheme in order to be more accessible

    :param chart:Chart This is a vega-altair Chart object
    :param filename:str Name of the new HTML file
    :param description:str A description to instep in the attribute aria-label for the screen readers
    """
    chart_json = json.loads(chart.to_json())
    root_file = os.path.abspath(os.path.dirname(__file__))
    html_path = filename + ".html"
    template = Template(accesible_template)
    template_html = template.render(chart=chart_json, description=description)

    with open(html_path, "w") as file:
        file.write(template_html)
    print("Thew HTLM file has been created in", html_path)


