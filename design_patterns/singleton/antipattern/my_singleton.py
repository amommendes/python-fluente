from __future__ import annotations
from typing import Optional


class SingletonMeta(type):
    _instance: Optional[MySingleton] = None

    def __call__(self) -> MySingleton:
        if self._instance is None:
            print("First time, take a new brand Singleton")
            self._instance = super().__call__()
        self.my_id(self)
        return self._instance

    def __repr__(self):
        return f"I'm a metaclass, {self.__class__.__name__}"


class MySingleton(metaclass=SingletonMeta):

    def __init__(self):
        pass

    def my_id(self):
        print(id(self))
