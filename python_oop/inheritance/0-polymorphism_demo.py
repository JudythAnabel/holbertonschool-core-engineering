#!/usr/bin/env python3
"""Demonstrates inheritance and polymorphism with animals."""


class Animal:
    """Represents a generic animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog, a kind of Animal."""

    def speak(self):
        """Return the sound a dog makes."""
        return "Woof"


class Cat(Animal):
    """Represents a cat, a kind of Animal."""

    def speak(self):
        """Return the sound a cat makes."""
        return "Meow"


if __name__ == "__main__":
    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
