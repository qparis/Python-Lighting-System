import os

import wx

class ManualController(wx.App):
    def __init__(self, midiClock, set_current_effect):
        super().__init__()
        self.midiClock = midiClock
        self.set_current_effect = set_current_effect
        self.frame = wx.Frame(None, wx.ID_ANY, "Python Lighting System v0.0.1", style=wx.BORDER_NONE) # A Frame is a top-level window
        self.frame.SetSize((275, 25))
        self.frame.SetWindowStyle(wx.CAPTION)
        self.frame.SetPosition(((wx.DisplaySize()[0] - 275) / 2, 25))
        self.frame.ToggleWindowStyle(wx.STAY_ON_TOP)
        self.frame.Show(True)
        self.combobox = wx.ComboBox(self.frame, 100, "Init", choices = self.fetchAvailableScenes())

        self.draw()
        self.defineEvents()

    def setCurrentScene(self, currentScene):
        self.currentScene = currentScene
        wx.CallAfter(lambda: self.combobox.SetValue(currentScene))
        #wx.CallAfter(lambda: self.combobox.SetItems(self.fetchAvailableScenes()))


    def draw(self):
        #panel = wx.Panel(self.frame, wx.ID_ANY)
        sizer = wx.BoxSizer(wx.HORIZONTAL)

        sizer.Add(self.combobox)

        self.frame.SetSizer(sizer)
        self.frame.Layout()

    def parseCommand(self, command):
        try:
            parsed_command = command.split(" ")

            if parsed_command[0] == "m":
                self.midiClock.set_mutliplier(float(parsed_command[1]))

            if parsed_command[0] == "e":
                effect = parsed_command[1]
                self.set_current_effect(effect)

            if parsed_command[0] == "sync":
                self.midiClock.sync()
        except:
            print("Error!")

    def run(self):

        self.MainLoop()

    def fetchAvailableScenes(self):
        scenes = os.listdir("effects")
        scenes = [scene.replace(".py", "") for scene in scenes if not scene.startswith("_") and ".py" in scene]
        scenes.sort()
        return scenes

    def current_effect_to_value(self, event):
        self.set_current_effect(self.combobox.GetValue())

    def defineEvents(self):
        self.combobox.Bind(wx.EVT_COMBOBOX, self.current_effect_to_value)



