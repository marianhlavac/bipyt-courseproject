import tkinter
from . import control_widget, preview_widget

def get_window_geometry(window_dim, screen_dim):
    x = (screen_dim[0] - window_dim[0])/2
    y = (screen_dim[1] - window_dim[1])/2
    return '%dx%d+%d+%d' % (window_dim[0], window_dim[1], x, y)

def display():

    top = tkinter.Tk()
    top.title('Image editor')

    window_dimensions = (960, 480)
    screen_dimensions = (top.winfo_screenwidth(), top.winfo_screenheight())
    top.geometry(get_window_geometry(window_dimensions, screen_dimensions))

    top = attach_widgets(top)

    return top

def attach_widgets(tk):
    control_widget.get_widget(tk).pack(
        side = tkinter.RIGHT, fill = tkinter.Y, ipadx = 10, ipady = 10)

    preview_widget.get_widget(tk).pack(
        side = tkinter.LEFT, fill = tkinter.BOTH, ipadx = 10, ipady = 10,
        expand = True)

    return tk
