#!/usr/bin/env python3

# shoe.py

class Shoe:
    def __init__(self, brand: str, size: int):
        self.brand = brand
        self._size = None
        self.size = size  # Use the setter to validate size
        self.condition = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
