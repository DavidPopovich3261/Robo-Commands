from classes.Robot import Robot



class SpeakableMixin(Robot):
    def speaks(self,command):
        print(command)


