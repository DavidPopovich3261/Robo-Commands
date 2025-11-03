from classes.SpeakableMixin import SpeakableMixin


class GuardRobot(SpeakableMixin):
    def get_command(self,command):
        if command[0] == "SAY":
            SpeakableMixin.speaks(self, command[1::])
        else:
            print(f"“unsupported command{command[0]}")
