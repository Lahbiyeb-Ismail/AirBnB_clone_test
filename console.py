#!/usr/bin/python3

import cmd
import re

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "City": City,
    "State": State,
    "Amenity": Amenity,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
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
        if arg not in classes:
            print("** class doesn't exist **")
            return

        new_model = classes[arg]()
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
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

        cls_name = obj_dict[key].get("__class__")
        cls_id = obj_dict[key].get("id")
        cls_dict = obj_dict[key]
        del cls_dict["__class__"]

        print("[{}] ({}) {}".format(cls_name, cls_id, cls_dict))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
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
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        obj_dict = storage.all()
        obj_list = []

        for key, value in obj_dict.items():
            cls_name = key.split(".")[0]
            if not arg:
                obj_list.append(classes[cls_name].__str__(classes[cls_name](**value)))
            else:
                if cls_name == arg:
                    obj_list.append(
                        classes[cls_name].__str__(classes[cls_name](**value))
                    )

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
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

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        self._precmd(arg)

    def _precmd(self, arg):
        """parses the input, extracts relevant pieces, constructs
        a standard command string and passes it to the main handler"""
        # regex to match the input line for a class.method(args) (EX: User.all()) pattern.
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)

        # If no match, just return the original input line.
        if not match:
            return arg

        # Extract the class name, method name and arguments from the regex match groups.
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        # Try to further parse the arguments to extract a UID and other arguments.
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)

        # Extract the UID and attr/dict arguments into separate variables.
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        # If no match, args is just the UID.
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        # For update method, try to parse attribute/value from dict or string.
        if method == "update" and attr_or_dict:
            match_dict = re.search("^({.*})$", attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict
            )
            if match_attr_and_value:
                attr_and_value = (
                    (match_attr_and_value.group(1) or "")
                    + " "
                    + (match_attr_and_value.group(2) or "")
                )

        # Construct final command string and pass to main handler.
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)

        # Return the processed command string.
        return command

    def do_count(self, arg):
        """Prints the number of instances of a class"""
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        count = 0
        for key in storage.all():
            if key.split(".")[0] == args[0]:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
