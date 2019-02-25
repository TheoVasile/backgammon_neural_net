import pygame as pg
from random import randint

pg.init()

w = 750
h = 500

screen = pg.display.set_mode((w,h))
pg.display.set_caption("backgammon")

clock = pg.time.Clock()
fps = 1

def do(q):
    print ("gay")
    print (q.get_id())
    return q.get_id()

class make_piece:
    def __init__(self,position,team,id):
        self.position = position
        self.team = team
        self.direction = [1,-1][self.team - 1]
        self.color = [(0,0,0),(255,255,255)][self.team - 1]
        self.id = id
    def move(self,value):
        print ("id = {}".format(self.id))
        self.ids = []
        for self.p in spots[self.position]:
            self.ids.append(self.p.get_id())
        print (self.ids)
        #print(spots[self.position])
        spots[self.position].remove(self)
        if len(spots[self.position]) < 1:
            spots[self.position] = [False]
        if self.position + (value * self.direction) not in range(1,25):
            print ("out of bounds")
            return False
        self.position += value * self.direction
        spots[self.position].append(self)
        try:
            spots[self.position].remove(False)
        except:
            pass

        return True

    def get_color(self):
        return self.color

    def get_team(self):
        return self.team
    def get_id(self):
        return self.id

class make_die:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.value = randint(0,6)
        self.width  = size
        self.height = size
    def randomize(self):
        self.value = randint(1,6)
        #print (self.value)
    def display(self):
        pg.draw.rect(screen, (255,255,255), (self.x - (self.width / 2), self.y - (self.height / 2), self.width, self.height), 0)

        if self.value == 1:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), 1, 0)
        elif self.value == 2:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
        elif self.value == 3:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
        elif self.value == 4:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
        elif self.value == 5:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 2)), int(self.y + ((self.height / 2) - 2))), 1, 0)
        elif self.value == 6:
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 4)), int(self.y)), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 4)), int(self.y)), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 4)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 4)), int(self.y - ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x - ((self.width / 2) - 4)), int(self.y + ((self.height / 2) - 2))), 1, 0)
            pg.draw.circle(screen, (0, 0, 0), (int(self.x + ((self.width / 2) - 4)), int(self.y + ((self.height / 2) - 2))), 1, 0)

    def get_value(self):
        return self.value

pieces = {1:[],2:[]}
spots = {1:[make_piece(1,1,1),make_piece(1,1,2)],2:[False],3:[False],4:[False],5:[False],6:[make_piece(6,2,3), make_piece(6,2,4), make_piece(6,2,5), make_piece(6,2,6), make_piece(6,2,7)],7:[False],8:[make_piece(8,2,8),make_piece(8,2,9),make_piece(8,2,10)],9:[False],10:[False],11:[False],12:[make_piece(12,1,11),make_piece(12,1,12),make_piece(12,1,13),make_piece(12,1,14),make_piece(12,1,15)],13:[make_piece(13,2,16),make_piece(13,2,17)],14:[False],15:[False],16:[False],17:[False],18:[make_piece(12,1,18),make_piece(12,1,19),make_piece(12,1,20),make_piece(12,1,21),make_piece(12,1,22)],19:[False],20:[make_piece(20,1,23),make_piece(20,1,24),make_piece(20,1,25)],21:[False],22:[False],23:[False],24:[make_piece(24,2,26),make_piece(24,2,27),make_piece(24,2,28),make_piece(24,2,29),make_piece(24,2,30)]}
for position in range(1,25):
    if spots[position][0]:
        for piece_index in range(0,len(spots[position])):
                pieces[spots[position][piece_index].get_team()].append(spots[position][piece_index])

dice = [make_die(w/2,h/2 + 10, 15), make_die(w/2,h/2 - 10, 15)]
teams = [1,2]
current_team = 1

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((215,200,200))

    for x in range(1,7):
        thing = (w / 2)
        pg.draw.polygon(screen, (100, 100, 100), [(((x / 6) * thing) - 45, 0), ((x / 6) * thing - 25, 0), ((x / 6) * thing - 35, h / 2 - 10)], 0)
        pg.draw.polygon(screen, (100, 100, 100), [(((x / 6) * thing) - 45, h), ((x / 6) * thing - 25, h), ((x / 6) * thing - 35, h / 2 + 10)], 0)
        pg.draw.polygon(screen, (100, 100, 100), [(((x / 6) * thing) - 45 + (w / 2), 0), ((x / 6) * thing - 25 + (w / 2), 0), ((x / 6) * thing - 35 + (w / 2), h / 2 - 10)], 0)
        pg.draw.polygon(screen, (100, 100, 100), [(((x / 6) * thing) - 45 + (w / 2), h), ((x / 6) * thing - 25 + (w / 2), h), ((x / 6) * thing - 35 + (w / 2), h / 2 + 10)], 0)

    for position in range(1,7):
        x = int(((position / 6) * (w / 2)) - 35)
        for piece_index in range(0,len(spots[position])):
            if spots[position][0]:
                radius = 10
                y = int(piece_index * (radius*2)) + radius
                pg.draw.circle(screen,spots[position][piece_index].get_color(),(x,y),radius,0)

    for position in range(7,13):
        x = int(((position / 6) * (w / 2)) - 35) #int((position / 6) * (w / 2) - 35 + (w / 2))
        for piece_index in range(0,len(spots[position])):
            if spots[position][0]:
                radius = 10
                y = int(piece_index * (radius*2)) + radius
                pg.draw.circle(screen,spots[position][piece_index].get_color(),(x,y),radius,0)

    for position in range(13,19):
        x = int((((position - 12) / 6) * (w / 2)) - 35) #int((position / 6) * (w / 2) - 25)
        for piece_index in range(0,len(spots[position])):
            if spots[position][0]:
                radius = 10
                y = h - int(piece_index * (radius*2)) - radius
                pg.draw.circle(screen,spots[position][piece_index].get_color(),(x,y),radius,0)

    for position in range(19,25):
        x = int((((position - 12) / 6) * (w / 2)) - 35) #int((position / 6) * (w / 2) - 25)
        for piece_index in range(0,len(spots[position])):
            if spots[position][0]:
                radius = 10
                y = h - int(piece_index * (radius*2)) - radius
                pg.draw.circle(screen,spots[position][piece_index].get_color(),(x,y),radius,0)
    pg.draw.rect(screen, (150, 125, 125), ((w / 2) - 5, 0, 10, h), 0)

    for die in dice:
        die.randomize()
        die.display()
        value = die.get_value()
        while not pieces[current_team][randint(0,len(pieces[current_team])-1)].move(value):
            a = 2+1

    current_team = teams[teams.index(current_team) - 1]

    pg.display.update()
    clock.tick(fps)