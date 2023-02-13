#!/usr/bin/python3
"""
    Implementing the command interpreter of AirBnB clone project
"""
import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Contains the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def do_create(self, args):
        """ method that creates a new instance of BaseModel, saves it
            (to the JSON file) and prints the id
        """
        cls = ["BaseModel"]
        if len(args) == 0:
            print("** class name missing **")
        elif args not in cls:
            print("** class doesn't exist **")
        else:
            bm_new_instance = BaseModel()
            bm_new_instance.save()
            print(bm_new_instance.id)

    def do_show(self, args):
        """ Prints the string representation of an instance based on
            the class name and id
        """
        cls = ["BaseModel"]
        string = args.split(" ")
        if args == "" or args is None:
            print("** class name missing **")
        else:
            if string[0] not in cls:
                print("** class doesn't exist **")
            elif len(string) < 2:
                print("** instance id missing **")
            else:
                storage = FileStorage()
                storage.reload()
                objs = storage.all()
                k = str(cls[0]) + "." + str(string[1])
                if k not in objs:
                    print("** no instance found **")
                else:
                    print(objs[k])

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file)
        """
        cls = ["BaseModel"]
        string = args.split(" ")
        if args == "" or args is None:
            print("** class name missing **")
        else:
            if string[0] not in cls:
                print("** class doesn't exist **")
            elif len(string) < 2:
                print("** instance id missing **")
            else:
                storage = FileStorage()
                storage.reload()
                objs = storage.all()
                k = str(cls[0]) + "." + str(string[1])
                if k not in objs:
                    print("** no instance found **")
                else:
                    storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances based
            or not on the class name
        """
        cls = ["BaseModel"]
        string = args.split(" ")
        if args == "" or args in str(cls[0]):
            storage = FileStorage()
            storage.reload()
            objs = storage.all()
            lst = []
            for val in objs.values():
                lst.append(str(val))
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Update an instance based on the class name and id
            sent as args.
        """
        cls = ["BaseModel"]
        string = args.split(" ")
        if args == "":
            print("** class name missing **")
            return
        if string[0] not in cls[0]:
            print("** class doesn't exist **")
            return
        if len(string) == 1:
            print("** instance id missing **")
            return
        k = cls[0] + "." + string[1]
        storage = FileStorage()
        storage.reload()
        objs = storage.all()
        if k not in objs:
            print("** no instance found **")
            return
        if len(string) == 2:
            print("** attribute name missing **")
            return
        quote = args.split('"')
        if len(quote) == 1:
            print("** value missing **")
            return
        attr = string[2]
        try:
            val = getattr(objs[k], attr)
            t = type(val)
            setattr(objs[k], attr, t(quote[1]))
        except Exception as excpt:
            setattr(objs[k], attr, quote[1])
        storage.save()

    def emptyline(self):
        """ method called when an empty line + ENTER and wich shouldn't
            execute anything in the prompt
        """
        pass

    def do_quit(self, args):
        """
            quit command to exit the program.
        """
        quit()
        return True

    def do_EOF(self, args):
        """
            logout after receiving the EOF signal/crtl+D
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
