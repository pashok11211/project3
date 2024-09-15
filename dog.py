class Dog:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    def name(self):
        return self._name

    def age(self):
        return self._age

    def color(self):
        return self._color

    def age(self, value):
        self._age = value

    def bark(self):
        return f"Собака {self.name}, возраста {self.age}, цвета {self.color} гавкает громко"