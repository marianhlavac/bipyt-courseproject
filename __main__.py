import editor.gui
import editor.event_handler as evh
import editor.store as store

gui = editor.gui.display()

def events():
    if len(evh.events) > 0:
        while len(evh.events) > 0:
            evh.handle(evh.events.pop())
        evh.update()
    gui.after(50, events)

gui.after(50, events)
gui.mainloop()
