#!/usr/bin/python3
"""
    Implementing the command interpreter of AirBnB clone project
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Contains the entry point of the command interpreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """method called when an empty line + ENTER and wich shouldn't
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
