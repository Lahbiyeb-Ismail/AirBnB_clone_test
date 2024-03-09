#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import json
import re

from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, arg):
        """Catch commands if nothing else matches then."""
        self._precmd(arg)

    def _precmd(self, arg):
        """parses the input, extracts relevant pieces, constructs
        a standard command string and passes it to the main handler"""
        # regex to match the input line for a class.method(args) pattern.
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)

        # If no match, just return the original input line.
        if not match:
            return arg

        # Extract the class name, method name and arguments
        # from the regex match groups.
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)

        # Try to further parse the arguments to extract
        # a UID and other arguments.
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

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        s = s_dict.replace("'", '"')
        d = json.loads(s)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, arg):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, arg):
        """Exits the program."""
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """Creates an instance."""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(" ")
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
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
        """Prints all string representation of all instances."""
        if arg and arg not in storage.classes():
            print("** class doesn't exist **")
            return

        obj_list = []

        if arg:
            obj_list = [
                str(obj)
                for key, obj in storage.all().items()
                if type(obj).__name__ == arg
            ]
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]

        print(obj_list)

    def do_count(self, arg):
        """Prints the number of instances of a class"""
        args = arg.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        if arg and arg not in storage.classes():
            print("** class doesn't exist **")
            return

        count = 0
        for key in storage.all():
            if key.split(".")[0] == args[0]:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute."""
        if arg == "" or arg is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, arg)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if "." in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', "")
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
