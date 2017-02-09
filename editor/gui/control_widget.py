import tkinter
import editor.event_handler as evh
import editor.store as store
import editor.utils as utils

widget_y_padding = 5
widget_x_padding = 10

def handle_load(ev): evh.capture('load', 0)
def handle_revert(ev): evh.capture('revert', 0)
def handle_inverse(ev): evh.capture('inverse', 0)
def handle_grayscale(ev): evh.capture('grayscale', 0)
def handle_edges(ev): evh.capture('edges', 0)

def get_widget(master):
    widget = tkinter.Frame(master)

    open_file_frame = tkinter.Frame(widget, padx = widget_x_padding,
                        pady = widget_y_padding)
    open_file_frame.pack(fill = tkinter.X)
    open_file_btn = tkinter.Button(open_file_frame, text = 'Open file...')
    open_file_btn.pack(fill = tkinter.X)
    open_file_btn.bind("<Button-1>", handle_load)

    get_title_widget(widget, 'FILE').pack(fill = tkinter.X, padx = widget_x_padding)
    get_fileinfo_widget(widget, ('thisisfilename')).pack(fill = tkinter.X)

    get_title_widget(widget, 'CONVERT').pack(fill = tkinter.X, padx = widget_x_padding)
    get_convert_widget(widget).pack(fill = tkinter.X, padx = widget_x_padding)

    get_title_widget(widget, 'ADJUST BRIGHTNESS').pack(fill = tkinter.X, padx = widget_x_padding)
    get_adjust_widget(widget).pack(fill = tkinter.X, padx = widget_x_padding)

    get_title_widget(widget, 'EXPORT').pack(fill = tkinter.X, padx = widget_x_padding)
    get_export_widget(widget).pack(fill = tkinter.X, padx = widget_x_padding)

    return widget

def get_space_widget(master, height):
    widget = tkinter.Frame(master, height = height)
    return widget

def get_title_widget(master, label):
    widget = tkinter.Frame(master)

    get_space_widget(widget, widget_y_padding*2).pack()

    label = tkinter.Label(widget, text = label,
                fg = '#888', font = 'TkDefaultFont 10 bold')
    label.pack(side = tkinter.LEFT)

    return widget

def get_fileinfo_widget(master, data):
    widget = tkinter.Frame(master, pady = widget_y_padding,
                padx = widget_x_padding)

    filename_var = tkinter.StringVar()
    filename = tkinter.Label(widget, textvariable = filename_var, justify = tkinter.LEFT,
                    font = 'TkDefaultFont 12 bold')
    filename.pack(anchor = tkinter.W)
    evh.register(lambda: filename_var.set(store.state['filename']))

    fileinfo = tkinter.StringVar()
    text = tkinter.Label(widget, justify = tkinter.LEFT, textvariable=fileinfo)
    text.pack(anchor = tkinter.W)
    evh.register(lambda: fileinfo.set(
        'Filesize: %.2f MB\nDimesions: %s' % (store.state['filesize'], store.state['filedim'])))

    return widget

def get_convert_widget(master):
    widget = tkinter.Frame(master, pady = widget_y_padding)

    invert_btn = tkinter.Button(widget, text = 'Invert colors')
    invert_btn.pack(fill = tkinter.X)
    invert_btn.bind("<Button-1>", handle_inverse)

    gs_btn = tkinter.Button(widget, text = 'Convert to grayscale')
    gs_btn.pack(fill = tkinter.X)
    gs_btn.bind("<Button-1>", handle_grayscale)

    edge_btn = tkinter.Button(widget, text = 'Detect edges')
    edge_btn.pack(fill = tkinter.X)
    edge_btn.bind("<Button-1>", handle_edges)

    return widget

def get_adjust_widget(master):
    widget = tkinter.Frame(master, pady = widget_y_padding)

    brightness = tkinter.Scale(widget, from_ = -100, to = 100, orient = tkinter.HORIZONTAL)
    brightness.pack(fill = tkinter.X)

    return widget

def get_export_widget(master):
    widget = tkinter.Frame(master, pady = widget_y_padding)

    revert_btn = tkinter.Button(widget, text = 'Revert changes')
    revert_btn.pack(fill = tkinter.X)
    revert_btn.bind("<Button-1>", handle_revert)

    export_btn = tkinter.Button(widget, text = 'Export to file...')
    export_btn.pack(fill = tkinter.X)

    return widget
