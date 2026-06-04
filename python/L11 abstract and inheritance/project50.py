from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar")

    def make_sound(self):
        return "Strum Strum!"

class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano")

    def make_sound(self):
        return "Plink Plink!"

class Drum(Instrument):
    def __init__(self):
        super().__init__("Drum")

    def make_sound(self):
        return "Boom Boom!"


instruments = [Guitar(), Piano(), Drum()]

print("Music Instrument Sound Show ")
for instrument in instruments:
    print(f"{instrument.name}: {instrument.make_sound()}")