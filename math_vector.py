from __future__ import annotations

import math
from typing import overload

class Vector:
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        
    def __repr__(self) -> str:
        return f"Vector({self.x!r}, {self.y!r})"
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    # def __bool__(self, ov):
    #     return bool(self.x or self.y)
    
    def __add__(self, vector: Vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)
        
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        
        
        