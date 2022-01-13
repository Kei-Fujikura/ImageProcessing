import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np

import dash_drawing

img_blank = np.zeros((300,300),np.uint8)*255

config = {
    "modeBarButtonsToAdd": [
        """
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
        """
    ]
}

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1(id="head-title"),
        dcc.Textarea(id="my-text-state",value="init"),
        html.Button(id="my-button", n_clicks=0, children="submit"),
        html.H3("Drag and draw annotations"),
        dcc.Graph(id="pic",figure=px.imshow(img_blank), config=config),
    ]
)

@app.callback(
    Output("head-title","children"),
    Output("pic","figure"),
    Input("my-button","n_clicks"),
    State("my-text-state","value")
)
def update_title(n_clicks, txt_value):
    num = 100 + int(n_clicks)

    fig = dash_drawing.DrawImage()
    if n_clicks == 1:
        dash_drawing.addRectangle(rect=[10,10,300,200])

    return ("%s : %d"%(txt_value, num), fig)


if __name__ == "__main__":
    app.run_server(debug=True)