import plotly.graph_objects as go
import plotly.express as px
from skimage import data

fig = None

def deco_fig_check(func):
    print("fig_check")
    def wrapper(*args, **kwargs):
        if fig == None:
            print("fig = None")
        else:
            func(*args, **kwargs)
    return wrapper

@deco_fig_check
def addRectangle(rect : list = [0,0,1,1], col : str = "red"):
    fig.add_shape(
        type="rect",
        x0=rect[0], y0=rect[1], x1=rect[2], y1=rect[3],
        line=dict(color=col))

@deco_fig_check
def addCircle(rect : tuple = [0,0,1,1], col : str = "red"):
    fig.add_shape(
        type="rect",
        x0=rect[0], y0=rect[1], x1=rect[2], y1=rect[3],
        line=dict(color=col))

def DrawImage(im = None):
    global fig
    if im == None:
        im = data.checkerboard()
        fig = px.imshow(im,color_continuous_scale="gray")
    else:
        fig = px.imshow(im)
    return fig
