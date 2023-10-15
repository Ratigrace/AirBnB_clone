#!/usr/bin/python3
"""Implements the HBNBCommand console program"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from datetime import datetime

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    
    def do_quit(self, args):
        """Exits the program"""
        return True
    
    def do_EOF(self, args):
        """Handles the EOF signal to exit the program"""
        print("")
        return True
    
    def do_create(self, args):
        """Creates a new instance of a model"""
        
        try:
            if not args:
                raise SyntaxError()
            
            model, *rest = args.split(" ")
            instance = eval(model)() 
            models.storage.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")
        except SyntaxError:
            print("** class name missing **")
            
    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name and id"""
        try:
            if not args:
                raise SyntaxError()
            
            model, id = args.split(" ")
            
            """ Check if the class exist """
            eval(model)
            instance = models.storage.all()[f"{model}.{id}"]
            print(instance)
            
        except SyntaxError as e:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
            
    def do_destroy(self, args):
        """Destroys an instance"""
        try:
            if not args:
                raise SyntaxError()
            
            model, id = args.split(" ")
            
            """ Check if the class exist """
            eval(model)
            del models.storage.all()[f"{model}.{id}"]
            models.storage.save()
              
        except SyntaxError as e:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
            
    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        try:
            if not arg:
                print([str(v) for v in models.storage.all().values()])
            else:
                model, *res = arg.split(" ")
                eval(model)
                filtered = list(filter(lambda x: x.__class__.__name__ == model, models.storage.all().values()))
                print([str(x) for x in filtered])
        except NameError:
            print("** class doesn't exist **")
            
    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        try:
            if not args:
                raise SyntaxError()
            model, id, attr, value = args.split(" ")
            eval(model)
            print(value)
            """ instance = models.storage.all()[f"{model}.{id}"]
            setattr(instance, attr, value)
            instance.save() """
        except SyntaxError:
            print("** class name missing **")
        except ValueError:
            error_messages = [
                "** instance id missing **",
                "** attribute name missing **",
                "** value missing **"
            ]
            print(error_messages[len(args.split(" ")) - 1])
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")
            
    def default(self, line):
        """runs customized models commands
        """
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = models.storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()