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
    try:
        store.state['picture'] = PIL.ImageOps.invert(store.state['picture'])
    except:
        alert(('This image is not supported to be inverted.'))

def grayscale(params):
    try:
        store.state['picture'] = store.state['picture'].convert('L')
    except:
        alert(('This image is not supported to be converted to grayscale.'))

def edges(params):
    try:
        store.state['picture'] = store.state['picture'].filter(ImageFilter.FIND_EDGES)
    except:
        alert(('This image is not supported to apply filters on.'))

def brightness(params):
    #try:
        store.state['picture'] = editor.fileop.brighten(store.state['picture'], params[0][0])
    #except:
    #    alert(('This image is not supported to apply filters on.'))
