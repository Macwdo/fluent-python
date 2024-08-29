from typing import Any


class MyClass:
    
    def __init__(self):
        self.my_attr = 42    
    
    def __getitem__(self, key):
        print(f"get item called {key}")
        return key
    
    
    def __getattribute__(self, name: str) -> Any:
        # print(f"__getattribute__ called with {name}")
        return super().__getattribute__(name)
    
    
c = MyClass()

print(c.my_attr)

print(c["sei la"])
        
        
