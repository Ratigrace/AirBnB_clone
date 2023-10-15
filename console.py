#!/usr/bin/python3
"""Implements the HBNBCommand console program"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.city import City
from models.place import Place
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """The Holberton Command Interpreter"""

    prompt = "(hbnb) "
    __models = {
        "BaseModel",
        "City",
        "Place",
        "State",
        "Review",
        "Amenity",
        "User",
    }

    def do_quit(self, args):
        """Exits the program"""
        return True

    def do_EOF(self, args):
        """Handles the EOF signal to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Handles empty line input"""

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
        """ Prints the string representation of an instance
        based on the class name and id"""

        try:
            if not args:
                raise SyntaxError()

            model, *id = args.split(" ")

            """ Check if the class exist """
            if model not in HBNBCommand.__models:
                raise NameError()
            if len(id) == 0:
                raise ValueError()
            instance = models.storage.all()[f"{model}.{id[0]}"]
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

            model, *id = args.split(" ")

            """ Check if the class exist """
            if model not in HBNBCommand.__models:
                raise NameError()
            if len(id) == 0:
                raise ValueError()
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
        """Prints all string representation of all instances
        based or not on the class name"""

        try:
            if not arg:
                print([str(v) for v in models.storage.all().values()])
            else:
                model, *res = arg.split(" ")
                if model not in HBNBCommand.__models:
                    raise NameError()
                filtered = list(filter(lambda x: x.__class__.__name__ == model,
                                       models.storage.all().values()))
                print([str(x) for x in filtered])
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""

        try:
            if not args:
                raise SyntaxError("** class name missing **")
            args = args.split(" ")
            if args[0] not in HBNBCommand.__models:
                raise NameError()
            if len(args) < 2:
                raise SyntaxError("** instance id missing **")
            model, id = args[:2]
            instance = models.storage.all()[f"{model}.{id}"]
            if len(args) < 3:
                raise SyntaxError("** attribute name missing **")
            if len(args) < 4:
                raise SyntaxError("** value missing **")
            attr, value = args[2:4]

            instance.__dict__[eval(attr)] = eval(value)
            instance.save()
        except SyntaxError as e:
            print(e.msg)
        except NameError:
            print("** class doesn't exist **")
        except KeyError:
            print("** no instance found **")

    def spread_func_call(self, args):
        """tokenizes the args. This also does cleaning
        """

        tokens = []
        tokens.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            tokens.append(((new_str.split(", "))[0]).strip('"'))
            tokens.append(my_dict)
            return tokens
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        tokens.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in tokens).strip()

    def count(self, model):
        """Counts the number of instance of the class"""

        try:
            if model not in HBNBCommand.__models:
                raise NameError()
            print(len([x for x in models.storage.all().values()
                       if type(x) is eval(model)]))
        except NameError:
            print("** class doesn't exist **")

    def command(self, arg):
        index = arg.find("(")
        if index == -1:
            return arg
        return arg[:index]

    def default(self, line):
        """runs customized models commands
        """

        handlers = {
            "all": self.do_all,
            "count": self.count,
            "destroy": self.do_destroy,
            "show": self.do_show,
            "update": self.do_update
        }
        my_list = line.split('.')

        if len(my_list) >= 2:
            command = self.command(my_list[1])
            if command not in handlers:
                cmd.Cmd.default(self, line)
                return

            if command in ("all", "count"):
                handlers[command](my_list[0])
            elif command == "update":
                args = self.spread_func_call(my_list)
                if isinstance(args, list):
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
            else:
                handlers[command](self.spread_func_call(my_list))
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
