import tkinter
import editor.store as store
import editor.event_handler as evh
from PIL import Image, ImageTk

def get_image_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    picture = Image.open('./resources/noimageloaded.png')
    photoimage = ImageTk.PhotoImage(picture)
    store.state['picture'] = picture
    canvas = tkinter.Label(widget, image = photoimage, bg = '#eee')
    canvas.image = photoimage
    canvas.pack(fill = tkinter.BOTH)

    def update():
        if store.state['picture'] is not None:
            photoimage = ImageTk.PhotoImage(store.state['picture'])
            canvas.configure(image = photoimage)
            canvas.image = photoimage

    evh.register(update)

    return widget

def get_widget(master):
    widget = tkinter.Frame(master, bg = '#eee')

    text = tkinter.Label(widget, text='Preview', fg = '#aaa', bg = '#eee', pady = 10)
    text.pack()

    get_image_widget(widget).pack()

    return widget
