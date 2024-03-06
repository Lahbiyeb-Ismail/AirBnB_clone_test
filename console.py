#!/usr/bin/python3

import cmd

from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return

        new_model = BaseModel()
        new_model.save()
        print(new_model.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
