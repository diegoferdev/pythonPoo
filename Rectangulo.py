from abc import ABC, abstractmethod
from math import sqrt

class IFigura(ABC):
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def color(self, color):
        pass

class Figura(IFigura):
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
            return self._color
        
    @color.setter
    def color(self, color):
        self.color = color
    
    def __str__(self)