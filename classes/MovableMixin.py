from classes.Robot import Robot


class MovableMixin(Robot):
    x=0
    y=0
    def moves(self,command):
        MovableMixin.x=int(command[1])
        MovableMixin.y=int(command[2])
        return MovableMixin.x,MovableMixin.y
    def where(self):
        print(MovableMixin.x,MovableMixin.y)


