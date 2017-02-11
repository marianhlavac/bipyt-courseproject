import editor.fileop
import editor.store as store
import os, os.path
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
import PIL.ImageOps

def start(params):
    print('Ready.')

def load(params):
    filename = editor.fileop.ask_for_file()

    if not os.path.isfile(filename):
        alert(('Selected file does not exist.'))
    else:
        picture = editor.fileop.load(filename)
        store.state['picture'] = picture
        store.state['original_picture'] = picture
        store.state['filename'] = filename.split('/')[-1]
        store.state['filesize'] = os.stat(filename).st_size / 1048576
        store.state['filedim'] = '{0}x{1}'.format(picture.size[0], picture.size[1])

def alert(params):
    print('Alert: {0}'.format(params))
    tkinter.messagebox.showinfo('Alert', params)

def revert(params):
    store.state['picture'] = store.state['original_picture']

def inverse(params):
    store.state['picture'] = PIL.ImageOps.invert(store.state['picture'])

def grayscale(params):
    try:
        store.state['picture'] = store.state['picture'].convert('L')
    except:
        alert(('This image is not supported to be converted to grayscale.'))

def edges(params):
    store.state['picture'] = store.state['picture'].filter(ImageFilter.FIND_EDGES)

def brightness(params):
    store.state['picture'] = editor.fileop.brighten(store.state['picture'], params[0][0])

def export(params):
    filename = editor.fileop.ask_for_save()
    extension = filename.split('.')[-1]

    if extension == 'png':
        store.state['picture'].save(filename, 'PNG')
    elif extension == 'jpg':
        store.state['picture'].save(filename, 'JPEG')
    elif extension == 'gif':
        store.state['picture'].save(filename, 'GIF')
    else:
        raise NotImplementedError('This file type is not supported to be exported.')

    print(extension)
