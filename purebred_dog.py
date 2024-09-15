from dog import Dog

class PurebredDog(Dog):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self._breed = breed

    def breed(self):
        return self._breed

    def bark(self):
        return super().bark()

    def go_to_dog_show(self):
        return f"Собака {self.name}, породы {self.breed} участвует в выставке."