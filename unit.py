#Represents a single unit
#Jazmin Gonzalez-Rivero, Zachary Homans, Elizabeth Mahon, Brendan Ritter
#Artificial Intelligence, Olin College, Spring 13

class unit:
    #units have:
    #   the space they're on
    #   their class
    #   their weapons
    #   their stats
    #all we need at the beginning is the space.
    #everything else will be constant.
    def __init__(self, space = None):
        self.space = space
        self.attack = 10
        self.hp = 35
        self.move = 5 #units can move 5 spaces by default
    def add_space(self, space):
        #units need to know what space they're on
        #need some way to make sure that units and spaces are always paired
        self.space = space
    def move(self, space):
        deltax = abs(self.space.get_x() - space.get_x())
        deltay = abs(self.space.get_y() - space.get_y())
        if (deltax + deltay) <= self.space:
            self.space.add_unit(None)
            space.add_unit(self)
            self.space = space
        else:
            #error!!