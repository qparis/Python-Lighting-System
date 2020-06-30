class EffectFactory:
    def __init__(self, dmxUsb):
        self.dmxUsb = dmxUsb

    def getEffectInstance(self, effect_name):
        effectFile = __import__("effects.%s" % effect_name)
        effectModule = getattr(effectFile, effect_name)
        effectClass = getattr(effectModule, effect_name)
        return effectClass(self.dmxUsb)