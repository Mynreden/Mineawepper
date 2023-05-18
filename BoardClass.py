square_size = 30

class Board():
    def __init__(self, wight, height, n_bombs):
        self.wight = wight
        self.height = height
        self.board = [[]]
        self.bombs = []
        self.n_bombs = n_bombs
        self.cube_group = pygame.sprite.Group()

    def generate(self): # generate matrix representation of board
        map = [[True for j in range(wight + 2)] for i in range(height + 2)] # True for bombs anf False for empty
        n_bombs = self.n_bombs
        while n_bombs:
            y, x = random.randint(1, self.height - 1), random.randint(1, self.wight - 1)
            if not map[y][x]:
                map[y][x] = True
                n_bombs -= 1

        for i in range(1, self.height - 1):
            list1 = []
            for j in range(1, self.wight - 1):
                bombs_around = 0
                for m in range(i - 1, i + 2):
                    for n in range(j - 1, j + 2):
                        if self.map[m][n]:
                            bombs_around += 1
                cube = Cube(bombs_around, [(i - 1) * square_size, (j - 1) * square_size])
                self.cube_group.add(cube)
                list1.append(cube)
            self.bombs.append(list1)

