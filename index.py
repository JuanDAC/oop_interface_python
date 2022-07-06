# /usr/bin/env python3

from cmd import Cmd
from animals.cat import Cat
from animals.dog import Dog


class Console(Cmd):
    def do_animal(self, line):
        animalClass, name, color, type, *_ = (*line.split(), None, None, None, None)
        try:
            animal = eval(animalClass)(name, color, getattr(eval(animalClass), type))
            print(animal)
        except Exception as e:
            print("ERROR: ", e)
    def do_population(self, line):
        animalClass, *_ = (*line.split(), None, None, None, None)
        print(eval(animalClass).show_population())


Console().cmdloop()
