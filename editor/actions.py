import editor.fileop
import editor.store as store
import os
import tkinter.filedialog
from PIL import Image, ImageTk

def start(params):
    print('Ready.')

def load(params):
    filename = tkinter.filedialog.askopenfilename()

    picture = Image.open(filename)
    photoimage = ImageTk.PhotoImage(picture)
    store.state['picture'] = photoimage
    store.state['filename'] = filename.split('/')[-1]

def inverse(params):
    print('Inverse button pressed.')
