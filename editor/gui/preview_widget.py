import tkinter

def get_nofile_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    label = tkinter.Label(widget, text = 'No image file loaded, load ' +
                'some using\nthe Load image button...', fg = '#666', bg = '#eee', height = 999)
    label.pack(fill = tkinter.BOTH)

    return widget

def get_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    text = tkinter.Label(widget, text='Preview', fg = '#aaa', bg = '#eee', pady = 10)
    text.pack()

    get_nofile_widget(widget).pack(fill = tkinter.BOTH, expand = True)

    return widget
