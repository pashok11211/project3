class Dog:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self.color = color

    def name(self):
        return self._name

    def age(self):
        return self._age

    def bark(self):
        return f"Собака {self.name()}, возраст {self.age}, цвет {self.color} гавкает громко."
