#!/usr/bin/python3

import cmd

from models import storage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
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
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        key = args[0] + "." + args[1]

        if key not in storage.all():
            print("** no instance found **")
            return

        # Get dictionary representation
        obj_dict = storage.all()[key]

        # Recreate instance from dict
        cls_name = obj_dict["__class__"]
        cls = classes[cls_name]
        instance = cls(**obj_dict)

        # If attribute doesn't exist, add it
        if not hasattr(instance, args[2]):
            setattr(instance, args[2], args[3].strip('"'))
        # Otherwise update existing attribute
        else:
            attr_type = type(getattr(instance, args[2]))
            attr_value = attr_type(args[3].strip('"'))
            setattr(instance, args[2], attr_value)

        # Convert updated instance back to dict
        new_obj_dict = instance.to_dict()

        # Save updated dict to storage
        storage.all()[key] = new_obj_dict
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
