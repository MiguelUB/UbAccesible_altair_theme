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
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
   </head>
   </head>
   <body >
      <div class="container mt-5">
         <div class="row">
            <div class="col-md-6">
               <!-- Primer div: Selector -->
               <div class="form-group">
                  <label for="selector">Scheme selector:</label>
                  <select class="form-control" id="selector" aria-labelledby="selectorLabel">
                     <option value="option1">Default</option>
                     <option value="option2">category20b</option>
                     <option value="option3">viridis</option>
                  </select>
               </div>
            </div>
         </div>
         <div class="row">
            <div class="col-md-6">
               <div id="chart"></div>
            </div>
         </div>
      </div>
      <!-- Div para mostrar el gráfico -->
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
      <script>
         // Especifica tu especificación de Vega-Lite
         var spec = {{ spec|tojson }};
         var defaultScheme = spec.encoding.color.hasOwnProperty('scale') ? spec.encoding.color.scale:
         spec.description = "{{description}}"
         var embedOpt = {"mode": "vega-lite"};
         function showError(el, error){
             el.innerHTML = ('<div style="color:red;">'
                                   + '<p>JavaScript Error: ' + error.message + '</p>'
                                   + "<p>This usually means there's a typo in your chart specification. "
                                   + "See the javascript console for the full traceback.</p>"
                                   + '</div>');
                   throw error;
               }
         const el = document.getElementById('chart');
         
         $(document).ready(function () {
                 // Manejar el cambio en el selector
                 $('#selector').change(function () {
                     // Obtener el valor seleccionado
                     var opcionSeleccionada = $(this).val();
                     console.log(opcionSeleccionada)
         
                     // Realizar acciones según el valor seleccionado
                     switch (opcionSeleccionada) {
                         case 'option1':
                             // Acciones para la opción 1
                             spec.encoding.color.scale=defaultScheme
                             vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                             break;
                         case 'option2':
                             // Acciones para la opción 2
                             spec.encoding.color.scale={"scheme":"category20b"}
                             vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                             break;
                         case 'option3':
                             // Acciones para la opción 3
                             console.log("Hola3")
                             spec.encoding.color.scale={"scheme":"viridis"}
                             vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
                             break;
                         default:
                             // Acciones por defecto
                             $('#graficoContainer').html('<p>Contenido por defecto</p>');
                             break;
                     }
                 });
             });
         vegaEmbed("#chart", spec, embedOpt).catch(error => showError(el, error));
         
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
    html_path = os.path.join(root_file, filename + ".html")
    template = Template(accesible_template)
    template_html = template.render(spec=chart_json, description=description)

    with open(html_path, "w") as file:
        file.write(template_html)
    print("Thew HTLM file has been created in", html_path)

