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
<svg height="0" width="0" xmlns="http://www.w3.org/2000/svg" version="1.1">
<defs>

<!-- From SVG stripe generator 
https://www.coffee-break-designs.com/labs/svg_stripe_generator/ -->

<pattern id="pattern_1" patternUnits="userSpaceOnUse" width="3" height="3" patternTransform="rotate(45)">
<line x1="0" y="0" x2="0" y2="3" stroke="#000000" stroke-width="4" />
</pattern>

<!-- From Pattern Fills by Irene Ros 
http://iros.github.io/patternfills/sample_svg.html 
http://iros.github.io/patternfills/ -->

<pattern id="pattern_2" patternUnits="userSpaceOnUse" width="8" height="8"> <image xlink:href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPSc4JyBoZWlnaHQ9JzgnPgogIDxyZWN0IHdpZHRoPSc4JyBoZWlnaHQ9JzgnIGZpbGw9JyNmZmYnLz4KICA8cGF0aCBkPSdNMCAwTDggOFpNOCAwTDAgOFonIHN0cm9rZS13aWR0aD0nMC41JyBzdHJva2U9JyNhYWEnLz4KPC9zdmc+Cg==" x="0" y="0" width="8" height="8"> </image> </pattern> 

<pattern id="pattern_3" patternUnits="userSpaceOnUse" width="10" height="10"> <image xlink:href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxMCcgaGVpZ2h0PScxMCc+CiAgPHJlY3Qgd2lkdGg9JzEwJyBoZWlnaHQ9JzEwJyBmaWxsPScjNTU5NGU3Jy8+CiAgPHBhdGggZD0nTS0xLDEgbDIsLTIKICAgICAgICAgICBNMCwxMCBsMTAsLTEwCiAgICAgICAgICAgTTksMTEgbDIsLTInIHN0cm9rZT0nd2hpdGUnIHN0cm9rZS13aWR0aD0nMScvPgo8L3N2Zz4=" x="0" y="0" width="10" height="10"> </image> </pattern>

<pattern id="houndstooth" patternUnits="userSpaceOnUse" width="10" height="10"> <image xlink:href="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0nMTAnIGhlaWdodD0nMTAnIHhtbG5zPSdodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2Zyc+CiAgPHBhdGggZD0nTTAgMEw0IDQnIHN0cm9rZT0nI2FhYScgZmlsbD0nI2FhYScgc3Ryb2tlLXdpZHRoPScxJy8+CiAgPHBhdGggZD0nTTIuNSAwTDUgMi41TDUgNUw5IDlMNSA1TDEwIDVMMTAgMCcgc3Ryb2tlPScjYWFhJyBmaWxsPScjYWFhJyBzdHJva2Utd2lkdGg9JzEnLz4KICA8cGF0aCBkPSdNNSAxMEw1IDcuNUw3LjUgMTAnIHN0cm9rZT0nI2FhYScgZmlsbD0nI2FhYScgc3Ryb2tlLXdpZHRoPScxJy8+Cjwvc3ZnPgo=" x="0" y="0" width="10" height="10"> </image> </pattern>

</defs>
</svg>
<svg id='sadsa' width='0%' height='0%' xmlns='http://www.w3.org/2000/svg'><defs><pattern id='gg' patternUnits='userSpaceOnUse' width='30' height='40' patternTransform='scale(3) rotate(95)'><rect x='0' y='0' width='100%' height='100%' fill='hsla(17,50%,57.6%,1)'/><path d='M1.624 19.09l6.597-1.595a.503.503 0 11.238.98L2.145 20l6.314 1.526a.504.504 0 01-.238.98l-6.597-1.595 3.426 3.426a3.813 3.813 0 005.386 0l1.1-1.1a4.584 4.584 0 000-6.475l-1.1-1.099a3.814 3.814 0 00-5.386 0zM-.911 18.377l-1.595-6.597a.504.504 0 11.98-.237L0 17.856l1.526-6.313a.503.503 0 11.98.237L.911 18.377l3.426-3.426a3.813 3.813 0 000-5.386l-1.1-1.099A4.548 4.548 0 000 7.125a4.547 4.547 0 00-3.238 1.341l-1.099 1.099a3.813 3.813 0 000 5.386zM-11.535 16.763a4.584 4.584 0 000 6.476l1.1 1.099a3.813 3.813 0 005.385 0l3.426-3.426-6.597 1.595a.501.501 0 01-.609-.371.504.504 0 01.372-.609l6.313-1.526-6.313-1.526a.504.504 0 11.237-.98l6.597 1.595-3.426-3.426a3.796 3.796 0 00-2.693-1.113c-.975 0-1.95.37-2.693 1.113zM.911 21.625l1.595 6.597a.504.504 0 11-.98.237L0 22.146l-1.526 6.313a.505.505 0 01-.98-.237l1.595-6.597-3.426 3.426a3.813 3.813 0 000 5.386l1.1 1.099a4.584 4.584 0 006.475 0l1.099-1.099a3.813 3.813 0 000-5.386zM31.624 19.09l6.597-1.595a.503.503 0 11.238.98L32.145 20l6.314 1.526a.504.504 0 01-.238.98l-6.597-1.595 3.426 3.426a3.813 3.813 0 005.386 0l1.1-1.1a4.584 4.584 0 000-6.475l-1.1-1.099a3.814 3.814 0 00-5.386 0zM29.089 18.377l-1.595-6.597a.504.504 0 11.98-.237L30 17.856l1.526-6.313a.503.503 0 11.98.237l-1.595 6.597 3.426-3.426a3.813 3.813 0 000-5.386l-1.1-1.099A4.548 4.548 0 0030 7.125a4.547 4.547 0 00-3.238 1.341l-1.099 1.099a3.813 3.813 0 000 5.386zM18.465 16.763a4.584 4.584 0 000 6.476l1.1 1.099a3.813 3.813 0 005.385 0l3.426-3.426-6.597 1.595a.501.501 0 01-.609-.371.504.504 0 01.372-.609l6.313-1.526-6.313-1.526a.504.504 0 11.237-.98l6.597 1.595-3.426-3.426a3.796 3.796 0 00-2.693-1.113c-.975 0-1.95.37-2.693 1.113zM30.911 21.625l1.595 6.597a.504.504 0 11-.98.237L30 22.146l-1.526 6.313a.505.505 0 01-.98-.237l1.595-6.597-3.426 3.426a3.813 3.813 0 000 5.386l1.1 1.099a4.584 4.584 0 006.475 0l1.099-1.099a3.813 3.813 0 000-5.386zM16.624 39.09l6.597-1.595a.503.503 0 11.238.98L17.145 40l6.314 1.526a.504.504 0 01-.238.98l-6.597-1.595 3.426 3.426a3.813 3.813 0 005.386 0l1.1-1.1a4.584 4.584 0 000-6.475l-1.1-1.099a3.814 3.814 0 00-5.386 0zM14.089 38.377l-1.595-6.597a.504.504 0 11.98-.237L15 37.856l1.526-6.313a.503.503 0 11.98.237l-1.595 6.597 3.426-3.426a3.813 3.813 0 000-5.386l-1.1-1.099A4.548 4.548 0 0015 27.125a4.547 4.547 0 00-3.238 1.341l-1.099 1.099a3.813 3.813 0 000 5.386zM3.465 36.763a4.584 4.584 0 000 6.476l1.1 1.099a3.813 3.813 0 005.385 0l3.426-3.426-6.597 1.595a.501.501 0 01-.609-.371.504.504 0 01.372-.609l6.313-1.526-6.313-1.526a.504.504 0 11.237-.98l6.597 1.595-3.426-3.426a3.796 3.796 0 00-2.693-1.113c-.975 0-1.95.37-2.693 1.113zM15.911 41.625l1.595 6.597a.504.504 0 11-.98.237L15 42.146l-1.526 6.313a.505.505 0 01-.98-.237l1.595-6.597-3.426 3.426a3.813 3.813 0 000 5.386l1.1 1.1a4.584 4.584 0 006.475 0l1.099-1.1a3.813 3.813 0 000-5.386zM16.624-.91l6.597-1.595a.503.503 0 11.238.98L17.145 0l6.314 1.526a.504.504 0 01-.238.98L16.624.912l3.426 3.426a3.813 3.813 0 005.386 0l1.1-1.1a4.584 4.584 0 000-6.475l-1.1-1.099a3.814 3.814 0 00-5.386 0zM14.089-1.623L12.494-8.22a.504.504 0 11.98-.237L15-2.144l1.526-6.313a.503.503 0 11.98.237l-1.595 6.597 3.426-3.426a3.813 3.813 0 000-5.386l-1.1-1.099A4.548 4.548 0 0015-12.875a4.547 4.547 0 00-3.238 1.341l-1.099 1.099a3.813 3.813 0 000 5.386zM3.465-3.237a4.584 4.584 0 000 6.476l1.1 1.099a3.813 3.813 0 005.385 0L13.376.912 6.779 2.507a.501.501 0 01-.609-.371.504.504 0 01.372-.609L12.855.001 6.542-1.525a.504.504 0 11.237-.98L13.376-.91 9.95-4.336a3.796 3.796 0 00-2.693-1.113c-.975 0-1.95.37-2.693 1.113zM15.911 1.625l1.595 6.597a.504.504 0 11-.98.237L15 2.146 13.474 8.46a.505.505 0 01-.98-.237l1.595-6.597-3.426 3.426a3.813 3.813 0 000 5.386l1.1 1.099a4.584 4.584 0 006.475 0l1.099-1.099a3.813 3.813 0 000-5.386z'  stroke-width='1' stroke='none' fill='hsla(12,30.6%,90.4%,1)'/></pattern></defs><rect width='800%' height='800%' transform='translate(0,0)' fill='url(#a)'/></svg>
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

            vegaEmbed("#chart", spec, { "renderer": "svg" });
        }

        function changeWidth() {
            let newWidth = $widthGraphInput.val();
            spec["width"] = newWidth

            vegaEmbed("#chart", spec, { "renderer": "svg" });
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


            vegaEmbed("#chart", spec, { "renderer": "svg" });

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
            
            vegaEmbed("#chart", spec, { "renderer": "svg" });

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
                            vegaEmbed("#chart", spec, { "renderer": "svg" });
                            break;
                        case 'option2':

                            spec.encoding.color.scale = {"scheme": "category20b"}
                            vegaEmbed("#chart", spec, { "renderer": "svg" });
                            break;
                        case 'option3':
                            spec.encoding.color.scale = {"scheme": "viridis"}
                           vegaEmbed("#chart", spec, { "renderer": "svg" });
                            break;
                        default:
                            console.log("The selected option does not correspond any color scheme")
                            break;

                    }

                });
            }
        });
        
        vegaEmbed("#chart", spec, { "renderer": "svg" });
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
