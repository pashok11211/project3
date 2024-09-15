from dog import Dog
from purebred_dog import PurebredDog

if __name__ == "__main__":
    dog1 = Dog("Бобик", 3, "Белый")
    print(dog1.bark())

    purebred_dog = PurebredDog("Тузик", 5, "Черный", "Лабрадор")
    print(purebred_dog.bark())
    print(purebred_dog.go_to_dog_show())