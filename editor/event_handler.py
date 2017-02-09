import editor.actions as actions
import editor.store as store

events = [('start', [])]
updates = []

def handle(event, *params):
    getattr(actions, event)(params)

def capture(event, *params):
    print(event)
    print(params)
    events.append((event, params))

def register(update):
    updates.append(update)

def update():
    for update in updates:
        update()
