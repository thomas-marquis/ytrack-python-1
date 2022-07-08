import os

DOCK_FILE = 'fleets.pickle'


def before_scenario(context, scenario):
    context.dock_file = DOCK_FILE
    if os.path.exists(DOCK_FILE):
        os.remove(DOCK_FILE)
