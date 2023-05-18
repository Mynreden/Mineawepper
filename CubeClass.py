

class Cube():
    def __init__(self, number, position):
        super().__init__()
        self.number = number
        self.status = False # False for closed, True for open
        self.flag = False # True for flagged Cubes
        self.rect.topleft = position

