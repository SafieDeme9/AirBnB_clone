#!/usr/bin/python3

import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {"BaseModel": BaseModel, "User": User,
           "State": State, "City": City,
           "Amenity": Amenity, "Place": Place,
           "Review": Review}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, command):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        exit()

    def emptyline(self):
        """
        an empty line + ENTER will not execute anything
        """
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        try:
            cls = classes[args]
        except KeyError:
            print("** class doesn't exist **")
            return
        obj = cls()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Show the string representation of an instance based on the class
        name and id
        """
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        try:
            cls = classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all().keys():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        args = args.split()
        try:
            cls = classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all().keys():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        objs = storage.all()
        if not args:
            print([str(objs[obj]) for obj in objs.keys()])
        else:
            try:
                cls = classes[args]
            except KeyError:
                print("** class doesn't exist **")
                return
            print([str(objs[obj]) for obj in objs.keys() if obj.startswith(args)])


if __name__ == '__main__':
    hbnb = HBNBCommand()
    hbnb.cmdloop()
