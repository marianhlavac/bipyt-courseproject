import editor.actions as actions
import editor.store as store

events = [('start', 0)]
updates = []

def handle(event):
    getattr(actions, event[0])(event[1])

def capture(event):
    events.append(event)

def register(update):
    updates.append(update)

def update():
    for update in updates:
        update()
