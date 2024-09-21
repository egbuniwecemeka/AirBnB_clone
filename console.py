#!/usr/bin/python3
""" The entry point to a command interpreter """

import cmd
import shlex
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

    def do_show(self, arg):
        """ Prints class string representation using class name and id
        Usage: show <class_name> <class_id>
        """
        if not arg:
            print("** class name missing **")
            return
        
        args = shlex.split(arg)

        # Check if class name and id are provided
        if len(args) < 1:
            print("** instance name missing **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        class_id = args[1]
        
        try:
            # Check if class exist
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        # Accessing the storage and check if instance exists
        key = f"{class_name}.{class_id}"
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
        else:
            # print the string representation of the instance
            print(all_objects[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and is
        Usage: destroy <class_name> <class_id>
        """
        args = shlex.split(arg)
        
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_id = args[1]

        key = f"{class_name}.{class_id}"
        all_objects = storage.all()

        # Checks if instance exists then deletes it
        if key not in all_objects:
            print("** no instance found **")
            return
        else:
            del all_objects[key]
            storage.save()


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