from effects.modifiers.between import between
from scenes.Blackout import Blackout


def withColoredFlash(effect, level = 0.75):
    wait = [{
        "type": "wait",
        "duration": 0.05
    }]

    return effect + wait + between(Blackout().scene(), effect, level)
