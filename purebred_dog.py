from dog import Dog


class PurebredDog(Dog):
    def __init__(self, name2, age2, color2, breed):
        super().__init__(name2, age2, color2)
        self._breed = breed

    def breed(self):
        return self._breed

    def bark(self):
        return f"Собака {self.name()}, возвраст {self.age()}, цвет {self.color} гавкает громко."

    def go_to_dog_show(self):
        return f"Собака {self.name()}, породы {self.breed()} участвует в выставке."
