#!/usr/bin/python3
""" Module Console """
import cmd
import models
from models.base_model import BaseModel
import shlex
classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

class HBNBCommand(cmd.Cmd):
    """ Class command """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """Quit the program using EOF"""
        print("")
        raise SystemExit

    def do_quit(self, args):
        """Quit the program"""
        print("", end="")
        raise SystemExit

    def emptyline(self):
        """Dont do anything"""
        pass

    def do_create(self, arg):
        """Create a new class instance, usage: (hbnb) create <name of class>"""
        argv = shlex.split(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if argv[0] in classes:
            instance = eval(argv[0])()
        else:
            print("** class doesn't exist **")
            return
        print(instance.id)
        instance.save()
    
    def do_show(self, arg):
        """ Print an instance like a string, usage (hbnb) show <class.name> <class.id>"""
        argv = shlex.split(arg)
        if len(argv) == 0:
            print("** class name missing **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
            return
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        if argv[0] in classes:
            k = argv[0] + "." + argv[1] # usage
            if k in models.storage.all():
                print(models.storage.all()[k])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
