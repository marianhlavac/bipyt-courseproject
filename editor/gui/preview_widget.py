import tkinter
import editor.store as store
import editor.event_handler as evh
from PIL import Image, ImageTk

def get_image_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    picture = Image.open('./resources/noimageloaded.png')
    photoimage = ImageTk.PhotoImage(picture)
    store.state['picture'] = photoimage
    canvas = tkinter.Label(widget, image = photoimage, bg = '#eee')
    canvas.pack()

    def update():
        if store.state['picture'] is not None:
            canvas.configure(image = store.state['picture'])

    evh.register(update)

    return widget

def get_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    text = tkinter.Label(widget, text='Preview', fg = '#aaa', bg = '#eee', pady = 10)
    text.pack()

    get_image_widget(widget).pack()

    return widget
