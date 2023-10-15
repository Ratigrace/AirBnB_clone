#!/usr/bin/python3
"""HBNBCommand test"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
import console
import os
import sys
from io import StringIO
import pycodestyle


class TestHBNBCommand(unittest.TestCase):
    """The console test"""

    instance_not_found = "** no instance found **\n"
    class_not_found = "** class doesn't exist **\n"
    no_instance_id = "** instance id missing **\n"
    no_class_name = "** class name missing **\n"
    attribute_name_missing = "** attribute name missing **\n"
    value_missing = "** value missing **\n"

    def setUp(self):
        """Basic test setup"""

        self.cmd = HBNBCommand()
        self.file_path = "console.py"

    def tearDown(self):
        """test clean up"""

        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pycodestyle_compliance(self):
        """Check pycodestyle compliance"""

        style = pycodestyle.StyleGuide(quiet=False)
        p = style.check_files([self.file_path])
        self.assertEqual(p.total_errors, 0, 'Fix pycodestyle')

    def test_docstrings_in_cmde(self):
        """check for docstrings"""

        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.spread_func_call.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("\n")
            self.assertEqual('', stdout.getvalue())

    def test_quit(self):
        """test the quit command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("quit")
            self.assertEqual('', stdout.getvalue())

    def test_create(self):
        """Test the create command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("create")
            self.assertEqual(
                TestHBNBCommand.no_class_name, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("create asdfsfsd")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd('create User email="hoal@.com" password="1234"')

    def test_show(self):
        """Test the show command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("show")
            self.assertEqual(
                TestHBNBCommand.no_class_name, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("show asdfsdrfs")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("show BaseModel")
            self.assertEqual(
                TestHBNBCommand.no_instance_id, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())

    def test_destroy(self):
        """Test the destroy command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("destroy")
            self.assertEqual(
                TestHBNBCommand.no_class_name, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("destroy Galaxy")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("destroy User")
            self.assertEqual(
                TestHBNBCommand.no_instance_id, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())

    def test_all(self):
        """Test the all command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all asdfsdfsd")
            self.assertEqual(TestHBNBCommand.class_not_found,
                             stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all State")
            self.assertEqual("[]\n", stdout.getvalue())

    def test_update(self):
        """Test the update command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update")
            self.assertEqual(
                TestHBNBCommand.no_class_name, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update sldkfjsl")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update User")
            self.assertEqual(
                TestHBNBCommand.no_instance_id, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update User 12345")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all User")
            obj = stdout.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update User " + my_id)
            self.assertEqual(
                TestHBNBCommand.attribute_name_missing, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                TestHBNBCommand.value_missing, stdout.getvalue())

    def test_z_all(self):
        """Test the alternate all command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("asdfsdfsd.all()")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("State.all()")
            self.assertEqual("[]\n", stdout.getvalue())

    def test_z_count(self):
        """Test the count command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("asdfsdfsd.count()")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("State.count()")
            self.assertEqual("0\n", stdout.getvalue())

    def test_z_show(self):
        """Test the alternate show command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("safdsa.show()")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("BaseModel.show(abcd-123)")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())

    def test_destroy(self):
        """Test the alternate destroy command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("Galaxy.destroy()")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("User.destroy(12345)")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())

    def test_update(self):
        """Test the alternate update command"""

        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("sldkfjsl.update()")
            self.assertEqual(
                TestHBNBCommand.class_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("User.update(12345)")
            self.assertEqual(
                TestHBNBCommand.instance_not_found, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all User")
            obj = stdout.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("User.update(" + my_id + ")")
            self.assertEqual(
                TestHBNBCommand.attribute_name_missing, stdout.getvalue())
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("User.update(" + my_id + ", name)")
            self.assertEqual(
                TestHBNBCommand.value_missing, stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
