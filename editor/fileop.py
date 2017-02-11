from PIL import Image
from . import event_handler as evh
import tkinter.filedialog

def ask_for_file():
    return tkinter.filedialog.askopenfilename(
        filetypes = [('png files', '.png'), ('jpg files', '.jpg'), ('gif files', '.gif')]
    )

def ask_for_save():
    return tkinter.filedialog.asksaveasfilename(
        defaultextension = '.png',
        filetypes = [('png files', '.png'), ('jpg files', '.jpg'), ('gif files', '.gif')]
    )

def load(filename):
    file = Image.open(filename)
    return file.convert('RGB')

# http://stackoverflow.com/a/31363374
def brighten(image, brightness):
    src = image.convert('RGB').split()
    constant = (100 - brightness) / 100

    r, g, b = src

    if constant != 0:
        r = src[0].point(lambda i: i / constant)
        g = src[1].point(lambda i: i / constant)
        b = src[2].point(lambda i: i / constant)

    return Image.merge('RGB', (r, g, b)).convert(image.mode)
