from dog import Dog
from purebred_dog import PurebredDog

dog1 = Dog("Бобик", 3, "черный")
dog2 = PurebredDog("Шарик", 5, "белый", "Пудель")
print(dog1.bark())

print(dog2.bark())

print(dog2.go_to_dog_show())

dog1.age = 4
print(dog1.bark())
