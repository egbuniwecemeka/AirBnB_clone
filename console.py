#!/usr/bin/python3
""" The entry point to a command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ HBNB Command Interpreter class """
    prompt = '(hbnb) '

    def do_create(self, line):
        """ Creates a new instance, saves to (JSON file) and print it's id 
        Usage: create <className> (e.g create BaseModel)
        """
        if not line:
            print("** class name missing **")
            return

        try:
            # Dynamically create a new instance of the class
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_help(self, line):
        """ List all interpreter commands"""
        if cmd.Cmd.do_help(self, line):
            print("Documented commands (type help <command>)")
            print("EOF help quit")

    def do_EOF(self, line):
        """ Handles end-of-file and exits the program"""
        print("")
        return True
    
    def do_quit(self, line):
        """ To successfully quit the interpreter"""
        return True
    
    def emptyline(self):
        """ Do nothing and overide empty lines """  
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()