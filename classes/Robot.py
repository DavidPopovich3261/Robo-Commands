from abc import ABC,abstractmethod


class Robot:

    def __init__(self,name):
        self.name=name

    def command(self,commande):
       commande=commande.split()
       return commande

    def inpoting(self):
        self.command=input("Please write a command.")
        return self.command


