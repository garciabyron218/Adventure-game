# Character stats


class character_info:
    def __init__(self, name="coco", level=20):
        self.name = name
        self.level = int(level)

    def add_level(self, levels):
        self.level += levels

player = character_info()

