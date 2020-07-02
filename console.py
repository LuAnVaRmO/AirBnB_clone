#!/usr/bin/python3
""" Module Console """
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    """ Class command """
    prompt = '(hbnb)'

    def do_EOF(self, args):
        """Quit the program using EOF"""
        return True

    def do_quit(self, args):
        """Quit the program"""
        return True

    def emptyline(self):
        """Dont do anything"""
        pass

    def do_create(self, arg):
        """Create a new class instance, usage: (hbnb) create <class.name>"""
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
        """ Print an instance like a string, usage: (hbnb) show <name> <id> """
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
        else:
            k = argv[0] + "." + argv[1]
            if k in models.storage.all():
                print(models.storage.all()[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy an instance, usage: destroy <class.name> <class.id> """
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
        else:
            k = argv[0] + "." + argv[1]  # usage
            if k in models.storage.all():
                models.storage.all().pop(k)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string rep of all instances based or not on the class name"""
        argv = shlex.split(arg)
        d = models.storage.all()
        to_print = []
        if len(argv) == 0:
            for item in d.values():
                to_print.append(str(item))
            print(to_print)
        elif argv[0] in classes:
            for k, v in d.items():
                if v.__class__.__name__ == argv[0]:
                    to_print.append(v.__str__())
            print(to_print)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update or add a new attribute from an instanced class. """
        argv = shlex.split(arg)
        if len(argv) == 0 or argv[0] not in classes:
            print("** class name missing **")
            return
        if len(argv) == 1:
            print("** instance id missing **")
            return
        if len(argv) > 1:
            k = argv[0] + "." + argv[1]
            if k not in models.storage.all():
                print("** no instance found **")
                return
            elif len(argv) == 2:
                print("** attribute name missing **")
                return
        if len(argv) == 3:
            print("** value missing **")
            return
        if argv[0] not in classes:
            print("** class doesn't exist **")
            return
        else:
            k = argv[0] + "." + argv[1]
            if k in models.storage.all():
                if argv[2] == 'id':
                    return
                if argv[2] == 'created_at' or argv[2] == 'updated_at':
                    return
                if isinstance(argv[2], int):
                    argv[3] = int(argv[3])
                elif isinstance(argv[2], float):
                    argv[3] = float(argv[3])
                setattr(models.storage.all()[k], argv[2], argv[3])
                models.storage.all()[k].save()
                return
            else:
                print("** no instance found **")

    def default(self, arg):
        """ Default method """
        argv = arg.split(".")
        if len(argv) > 1:
            if argv[1] == 'all()':
                self.do_all(argv[0])
            elif argv[1] == 'count()':
                self.count(argv[0])

    def count(self, arg):
        """ Count instances of class """
        c = 0
        argv = shlex.split(arg, " ")
        if not argv[0] in classes:
            print("** class doesn't exit **")
        else:
            for k, v in models.storage.all().items():
                if argv[0] in k:
                    c += 1
            print(c)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
