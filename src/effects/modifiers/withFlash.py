from scenes.White import White


def withFlash(effect, flashScene = White().scene()):
    wait = [{
        "type": "wait",
        "duration": 0.05
    }]

    return flashScene + wait + effect