from classes.SpeakableMixin import SpeakableMixin
from classes.MovableMixin import MovableMixin

class DeliveryRobot(SpeakableMixin,MovableMixin ):
    def get_command(self,command):
        if command[0]=="SAY" :
            SpeakableMixin.speaks(self,command[1::])
        elif command[0] == "MOVE ":
            MovableMixin.moves(self, command[1::])
        elif command[0] == "WHERE":
            MovableMixin.where(self)
        else:
            print(f"“unsupported command{command[0]}")