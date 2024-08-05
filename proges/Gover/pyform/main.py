from .key import keyboard, mouse
from .utils.settings import Settings

import os
import sys
import json
import time
from tkinter import messagebox


sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))


apps = {}


def add(app, name, settings=None):
    """ Adds Program Into Apps """

    global apps

    apps[name] = app()
    app = apps[name]

    if not settings:
        settings = os.path.join(name, 'settings.json')

    with open(os.path.join(os.getcwd(), settings)) as settings_file:
        app.settings = Settings(json.load(settings_file))

    app.name = name
    app.run = False


def remove(name):
    global apps

    del apps[name]


def update():
    last_frame = time.time()
    
    for name, app in apps.items():
        try:
            if app.run:
                if hasattr(app, 'update'):
                    delay = time.time() - last_frame
                    last_frame = time.time()

                    app.update(delay)

                update_form(app.form)
                handle_hotkeys(app)

                time.sleep(1 / app.settings.INTERVAL)

        except:
            if hasattr(app, 'end'):
                app.end()
                app.run = False


def mainloop():
    global apps

    while True in [apps[name].run for name, app in apps.items()]:
        update()


def run(name):
    """ Runs The Program With Selected Name """

    global apps

    app = apps[name]

    app.set_caption(app.settings.TITLE)
    app.set_size(app.settings.SIZE[0], app.settings.SIZE[1])
    app.set_bg(app.settings.BACKGROUND)

    if os.name != 'posix':
        app.set_icon(app.settings.ICON)

    if hasattr(app, 'start'):
        app.start()

    app.run = True


def quit(name):
    """ Quits From Program With Selected Name """

    global apps

    app = apps[name]

    app.run = False

    if hasattr(app, 'end'):
        app.end()

    app.destroy()


def handle_hotkeys(app):
    """ To Handle Whether The User Uses KeyWord """

    keys = keyboard.pressed_keys()

    if hasattr(app, 'keydown'):
        for special_key in keyboard.special.values():
            if special_key in keys and not 'click' in special_key:
                for i in range(len(keys)):
                    app.keydown('-'.join(keys))
                    keys.insert(0, keys.pop(-1))

                return

        if keys and (key := keys[0]):
            app.keydown(key)
            return

    if hasattr(app, 'mousedown') and keys and 'click' in (key := keys[0]):
        app.mousedown(key.replace('click', ''), mouse.cursor_pos())


def update_form(form):
    form.update()
    form.update_idletasks()


def ask(message):
    return messagebox.askyesno(message)
