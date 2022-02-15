import math


class EffectController():
    def __init__(self, set_current_effect, midiController):
        self.set_current_effect = set_current_effect
        self.midiController = midiController
        self.current_deck = 0
        self.current_rules = []
        self.timings = {
            0: 0,
            1: 0
        }
        self.current_effect = None
        self.default_effect = None

    def set_rules(self, deck, rules):
        self.current_deck = deck
        self.current_rules = rules

        print("Current rules: ", self.current_rules)
        for rule in rules:
            if not "MinimumTime" in rule or rule["MinimumTime"] == 0 or rule["MinimumTime"] is None or math.isnan(
                    rule["MinimumTime"]):
                rule["MinimumTime"] = 0


    def set_timing(self, deck, time_in_seconds):
        self.timings[deck] = time_in_seconds

        if len(self.current_rules) > 0 and deck == self.current_deck:
            best_rule = None
            for rule in self.current_rules:
                if "MinimumTime" in rule and rule["MinimumTime"] <= time_in_seconds:
                    if best_rule is None or rule["MinimumTime"] > best_rule["MinimumTime"]:
                        best_rule = rule

            if best_rule is not None and best_rule["Effect"] != self.current_effect:
                self.set_current_effect(best_rule["Effect"])
                self.current_effect = best_rule["Effect"]
        else:
            if "AlternateColor" != self.current_effect and deck == self.current_deck :
                self.set_current_effect("AlternateColor")
                self.current_effect = "AlternateColor"
