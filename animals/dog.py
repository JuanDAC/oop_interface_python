

from animals.animals import Animals


class Dog(Animals):
    """" Blueprint than represent a Cat """

    __population = 0
    pincher = "pincher"
    golden = "golden"
    labrador = "labrador"
    pitbull = "pitbull"

    def __init__(self, name, color, typeOfcat):
        Dog.add_population()
        self._name = name
        self._color = color
        self._type = typeOfcat

    @property
    def _name(self):
        return self.__name

    @property
    def _color(self):
        return self.__color

    @property
    def _type(self):
        return self.__type

    @_name.setter
    def _name(self, value):
        if value is None or type(value) is not str:
            raise ValueError("will be a string")
        self.__name = value

    @_color.setter
    def _color(self, value):
        if value is None or type(value) is not str:
            raise ValueError("will be a string")
        self.__color = value

    @_type.setter
    def _type(self, value):
        if value is None or type(value) is not str:
            raise ValueError("will be a string")
        if not value in (Dog.pincher , Dog.golden, Dog.labrador, Dog.pitbull):
            raise ValueError("will be a type of Cat")
        self.__type = value

    def __str__(self):
        return f"\n\
            Name: {self._name}\n\
            Color: {self._color}\n\
            Type: {self._type}\n\
        "

    @classmethod
    def add_population(cls):
        cls.__population += 1

    @classmethod
    def show_population(cls):
        return cls.__population
