class DenonHC4500VirtualLCD:
    def __init__(self):
        self.state = {}
        self.display_count = 0
        self._position_callback = None
        self._screen_callback = None
        self._play_callback = None
        self._track_callback = None
        self.track_position = {}
        self.playing_state = {
            0: {
                "playing": False,
                "track": {
                    0: "",
                    1: ""
                }
            },
            1: {
                "playing": False,
                "track": {
                    0: "",
                    1: ""
                }
            }
        }

        self.reading_states = {
            0: {
                0: {
                    "last_screen_content": " " * 12,
                    "consecutive_spaces": 0,
                    "is_collecting": False,
                    "last_char_position": 0,
                    "current_read": ""
                },
                1: {
                    "last_screen_content": " " * 12,
                    "consecutive_spaces": 0,
                    "is_collecting": False,
                    "last_char_position": 0,
                    "current_read": ""
                }
            },
            1: {
                0: {
                    "last_screen_content": " " * 12,
                    "consecutive_spaces": 0,
                    "is_collecting": False,
                    "last_char_position": 0,
                    "current_read": ""
                },
                1: {
                    "last_screen_content": " " * 12,
                    "consecutive_spaces": 0,
                    "is_collecting": False,
                    "last_char_position": 0,
                    "current_read": ""
                }
            }
        }

    def set_position_callback(self, callback):
        self._position_callback = callback

    def set_screen_callback(self, callback):
        self._screen_callback = callback

    def set_play_callback(self, callback):
        self._play_callback = callback

    def set_track_callback(self, callback):
        self._track_callback = callback

    def process(self, payload, deck):
        command, number, value = payload

        if 0x01 <= number <= 0x39:
            line = self.fetch_line(number)
            bit_number = self.fetch_bit_numbering(number)
            char_position = self.fetch_char_position(number)

            if deck not in self.state:
                self.state[deck] = {}

            if line not in self.state[deck]:
                self.state[deck][line] = {}

            if char_position not in self.state[deck][line]:
                self.state[deck][line][char_position] = {}

            self.state[deck][line][char_position][bit_number] = value
            if bit_number == "MSB":
                self.state[deck][line][char_position]["LSB"] = None

            elif bit_number == "LSB" and "MSB" in self.state[deck][line][char_position]:
                LSB = value
                MSB = self.state[deck][line][char_position]["MSB"]

                current_char = chr(MSB << 4 | LSB)

                self.state[deck][line][char_position]["content"] = current_char

            if char_position == 12 and self._screen_callback is not None:
                self._screen_callback(deck, self.read_screen(deck))

            screen_content = self.read_screen(deck)[line - 1]
            reading_state = self.reading_states[deck][line - 1]

            if reading_state["last_screen_content"] != screen_content:
                if reading_state["last_char_position"] > char_position:
                    # if deck == 1 and line == 1:
                    #    print(reading_state["last_screen_content"], " -> ", char_position)

                    if reading_state["last_screen_content"][0] == " ":
                        reading_state["consecutive_spaces"] += 1
                    else:
                        reading_state["consecutive_spaces"] = 0

                    if reading_state["consecutive_spaces"] == 3:
                        reading_state["current_read"] = reading_state["last_screen_content"].split("   ")[0]

                    read_content = reading_state["current_read"].strip()
                    if read_content != "" and self.playing_state[deck]["track"][line - 1] != read_content:
                        self.playing_state[deck]["track"][line - 1] = read_content
                        if self._track_callback is not None:
                            self._track_callback(deck, line, read_content)

                reading_state["last_screen_content"] = screen_content
                reading_state["last_char_position"] = char_position

        elif number == 0x42:
            self.track_position["minutes"] = value
        elif number == 0x43:
            self.track_position["seconds"] = value
        elif number == 0x44:
            self.track_position["frame"] = value
        elif number == 0x48:
            self.track_position["percent"] = value
            self.update_track_position(deck)
        elif number == 0x4E:
            if deck not in self.playing_state:
                self.playing_state[deck] = {}

            if value == 0x0B:
                self.playing_state[deck]["playing"] = True

            if value == 0x0C:
                self.playing_state[deck]["playing"] = False

            if self._play_callback is not None:
                self._play_callback(self.playing_state, deck)

    def read_screen(self, deck_to_collect):
        result = {}
        for deck in self.state:
            if deck == deck_to_collect:
                for line in self.state[deck]:
                    for character in range(1, 13):
                        if line not in result:
                            result[line] = ""

                        if character in self.state[deck][line] and \
                                "content" in self.state[deck][line][character] and \
                                self.state[deck][line][character]["content"] is not None:

                            result[line] += self.state[deck][line][character]["content"]
                        elif character not in self.state[deck][line]:
                            result[line] += " "
        return list(result.values())

    def fetch_line(self, number):
        if 0x01 <= number <= 0x0D:
            return 1

        if 0x21 <= number <= 0x2D:
            return 1

        if 0x0E <= number <= 0x19:
            return 2

        if 0x2E <= number <= 0x39:
            return 2

    def fetch_bit_numbering(self, number):
        if 0x01 <= number <= 0x0D:
            return "MSB"

        if 0x21 <= number <= 0x2D:
            return "LSB"

        if 0x0E <= number <= 0x19:
            return "MSB"

        if 0x2E <= number <= 0x39:
            return "LSB"

    def fetch_char_position(self, number):
        if 0x01 <= number <= 0x05:
            return number

        if 0x07 <= number <= 0x0D:
            return number - 1

        if 0x21 <= number <= 0x25:
            return number - 0x20

        if 0x27 <= number <= 0x2D:
            return number - 0x21

        if 0x0E <= number <= 0x19:
            return number - 0x0D

        if 0x2E <= number <= 0x39:
            return number - 0x2D

    def empty_buffer(self):
        self.state = {}

    def buffer_full(self):
        for deck in self.state:
            for line in self.state[deck]:
                if len(self.state[deck][line]) != 12:
                    return False
                for character in self.state[deck][line]:
                    if not "content" in self.state[deck][line][character]:
                        return False

        return True

    def update_track_position(self, deck):
        if self._position_callback is not None:
            if "percent" in self.track_position and "minutes" in self.track_position and "seconds" in self.track_position and "frame" in self.track_position:
                track = self.playing_state[deck]["track"]
                if track[0] != "" and track[1] != "":
                    self._position_callback(self.track_position, deck)
