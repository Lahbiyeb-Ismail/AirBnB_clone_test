#!/usr/bin/python3

import cmd

from models import storage
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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + "." + args[1]

        if key not in obj_dict:
            print("** no instance found **")
            return

        print(BaseModel.__str__(BaseModel(**obj_dict[key])))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = args[0] + "." + args[1]

        if key not in obj_dict:
            print("** no instance found **")
            return

        del obj_dict[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()
        obj_list = []

        for key, value in obj_dict.items():
            if key.split(".")[0] == "BaseModel":
                obj_list.append(BaseModel.__str__(BaseModel(**value)))

        print(obj_list)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
