import pandas as pd

from EffectController import EffectController
from EffectFactory import EffectFactory
from ManualController import ManualController
from dmx import OpenDmxUsb
from midi.DJMController import DJMController
from midi.DenonHC4500VirtualLCD import DenonHC4500VirtualLCD
from midi.MidiClock import MidiClock
from midi.MidiController import MidiController


class PartyController:
    def __init__(self):
        self.dmxUsb = OpenDmxUsb()
        self.dmxUsb.start()
        self.effectFactory = EffectFactory(self.dmxUsb)
        self.midiClock = MidiClock()
        self.manualController = ManualController(self.midiClock, self.set_current_effect)
        self.djmController = DJMController()
        self.djmController.set_update_control_callback(self.update_control_callback)
        self.denonHc4500Controller = DenonHC4500VirtualLCD()
        self.midiController = MidiController(self.midiClock, self.denonHc4500Controller, True, self.djmController)
        self.set_current_effect("AlternateColor")
        self.playing_states = {
            0: {
                "playing": False,
                "position_in_seconds": 0
            },
            1: {
                "playing": False,
                "position_in_seconds": 0
            }
        }
        self.effect_controller = EffectController(self.set_current_effect, self.midiController)

    def process_song(self, deck, line, song):
        if line == 1 or line == 2:
            return

        if self.playing_states[deck]["playing"] is False:
            print("Deck not playing. Ignoring song: '%s'" % song)
            return

        print("Looking for <%s> (%s)" % (song, line))
        rules = list(pd.read_csv("songs.csv", sep=';').T.to_dict().values())

        matching_rules = []
        for rule in rules:
            if rule["Song"][:11].strip() in song:
                try:
                    print("Found effect: %s (song %s)" % (rule["Effect"], song))
                    matching_rules += [rule]
                except:
                    print("Error")

        self.effect_controller.set_rules(deck, matching_rules)

    def process_position(self, position, deck):
        time_in_seconds = 60 * position["minutes"] + position["seconds"] + (position["frame"] / 100)
        self.playing_states[deck]["position_in_seconds"] = time_in_seconds
        self.effect_controller.set_timing(deck, time_in_seconds)

    def start(self):
        # denonHc4500Controller.set_position_callback(lambda p: print(p))
        # denonHc4500Controller.set_screen_callback(lambda x,y: print(y))
        self.midiController.start()
        self.denonHc4500Controller.set_play_callback(self._play_callback)
        self.denonHc4500Controller.set_track_callback(self.process_song)
        self.denonHc4500Controller.set_position_callback(self.process_position)
        self.manualController.run()

    def update_control_callback(self, state):
        if "FADER" in state and state["FADER"] > 64:
            if self.playing_states[1]["selected"] is False:
                self.playing_states[0]["selected"] = False
                self.playing_states[1]["selected"] = True
                self.update_scene_to_current_song()
        else:
            if self.playing_states[0]["selected"] is False:
                self.playing_states[0]["selected"] = True
                self.playing_states[1]["selected"] = False
                self.update_scene_to_current_song()

    def _play_callback(self, decks, event_deck):
        changed1 = False
        changed2 = False

        if "playing" not in self.playing_states[0] or self.playing_states[0]["playing"] != decks[0]["playing"]:
            self.playing_states[0]["playing"] = decks[0]["playing"]
            changed1 = True

        if "track" not in self.playing_states[0] or self.playing_states[0]["track"] != decks[0]["track"]:
            self.playing_states[0]["track"] = decks[0]["track"]
            changed1 = True

        if "playing" not in self.playing_states[1] or self.playing_states[1]["playing"] != decks[1]["playing"]:
            self.playing_states[1]["playing"] = decks[1]["playing"]
            changed2 = True

        if "track" not in self.playing_states[1] or self.playing_states[1]["track"] != decks[1]["track"]:
            self.playing_states[1]["track"] = decks[1]["track"]
            changed2 = True

        if "selected" not in self.playing_states[0]:
            self.playing_states[0]["selected"] = False

        if "selected" not in self.playing_states[1]:
            self.playing_states[1]["selected"] = False

        if (changed1 and self.playing_states[0]["selected"] is True) or (
                changed2 and self.playing_states[1]["selected"] is True):
            self.update_scene_to_current_song()

    def update_scene_to_current_song(self):
        decks = self.playing_states
        if decks[0]["playing"] is False and decks[1]["playing"] is False or \
                decks[0]["selected"] is True and decks[0]["playing"] is False or \
                decks[1]["selected"] is True and decks[1]["playing"] is False :
            self.midiController.set_effect(self.effectFactory.getEffectInstance("Blackout"))
            print(self.playing_states)
        else:
            if decks[0]["selected"] is False and decks[1]["selected"] is True:
                for line in decks[1]["track"]:
                    self.process_song(1, line, decks[1]["track"][line])
            else:
                for line in decks[0]["track"]:
                    self.process_song(0, line, decks[0]["track"][line])

            self.midiController.set_effect(self.effectFactory.getEffectInstance(self.current_effect))

    def set_current_effect(self, effect):
        self.current_effect = effect
        self.manualController.setCurrentScene(effect)
        self.midiController.set_effect(self.effectFactory.getEffectInstance(self.current_effect))


PartyController().start()
