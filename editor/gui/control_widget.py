import tkinter

widget_y_padding = 5
widget_x_padding = 10

def get_widget(master):
    widget = tkinter.Frame(master)

    open_file_frame = tkinter.Frame(widget, padx = widget_x_padding,
                        pady = widget_y_padding)
    open_file_frame.pack(fill = tkinter.X)
    open_file_btn = tkinter.Button(open_file_frame, text = 'Open file...')
    open_file_btn.pack(fill = tkinter.X)

    get_title_widget(widget, 'FILE').pack(fill = tkinter.X, padx = widget_x_padding)

    get_fileinfo_widget(widget, ('thisisfilename')).pack(fill = tkinter.X)

    get_title_widget(widget, 'EDIT').pack(fill = tkinter.X, padx = widget_x_padding)

    get_edit_widget(widget).pack()

    get_title_widget(widget, 'EXPORT').pack(fill = tkinter.X, padx = widget_x_padding)

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

    filename = tkinter.Label(widget, text='theimage.png', justify = tkinter.LEFT,
                    font = 'TkDefaultFont 12 bold')
    filename.pack(anchor = tkinter.W)

    text = tkinter.Label(widget, text='Filesize: 1.4 MB\nDimesions: 1280 x 720',
                            justify = tkinter.LEFT)
    text.pack(anchor = tkinter.W)

    return widget

def get_edit_widget(master):
    widget = tkinter.Frame(master, pady = widget_y_padding)

    # resize image controls
    resize = tkinter.Frame(widget)
    resize.pack()

    x_input = tkinter.Entry(resize, width = 7)
    x_input.insert(0, '1280')
    x_input.pack(side = tkinter.LEFT, expand = True, fill = tkinter.X)

    lock_btn = tkinter.Button(resize, text = '<->')
    lock_btn.pack(side = tkinter.LEFT, expand = True)

    y_input = tkinter.Entry(resize, width = 7)
    y_input.insert(0, '720')
    y_input.pack(side = tkinter.LEFT, expand = True, fill = tkinter.X)

    crop_btn = tkinter.Button(widget, text = 'Resize image')
    crop_btn.pack(fill = tkinter.X)

    get_space_widget(widget, widget_y_padding*4).pack()

    # apply filter controls
    selected_filter = tkinter.StringVar(widget)
    selected_filter.set('- select filter -')
    filters = tkinter.OptionMenu(widget, selected_filter,
                'Convert to grayscale', 'Red filter', 'Green filter',
                'Blue filter')
    filters.pack(fill = tkinter.X)

    apply_btn = tkinter.Button(widget, text = 'Apply filter')
    apply_btn.pack(fill = tkinter.X)

    return widget
