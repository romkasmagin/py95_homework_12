from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('Gav gav')


class Cat(Animal):
    def speak(self):
        print("Muy muy")


class AnimalFactory:
    @staticmethod
    def create_animal(type_animal):
        if type_animal == 'dog':
            return Dog()
        elif type_animal == 'cat':
            return Cat()


factory = AnimalFactory()
print(type(factory))
animal = factory.create_animal('dog')
print(type(animal))
animal.speak()
animal = factory.create_animal('cat')
print(type(animal))
animal.speak()
