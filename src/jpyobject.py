from typing import Any, Self
import json

class JPyObject:
    def __init__(self) -> None:
        pass

    def __getattr__(self, __name: str) -> Any | None:
        if __name not in self.__dict__:
            return None
        else:
            return self.__dict__[__name]
        
    def __str__(self):
        return str(self.__dict__)
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict__[__name] = __value

    def _loads(self, s: str | bytes | bytearray, **kwargs) -> Self:
        jsonObj = json.loads(s, **kwargs)
        self.__dict__.update(jsonObj)
        
    def _load(self, s: str) -> Self:
        jsonObj = json.load(s)
        self.__dict__.update(jsonObj)

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__


def loads(s: str | bytes | bytearray, **kwargs) -> JPyObject:
    obj = JPyObject()
    obj._loads(s)
    return obj

def load(s: str, **kwargs) -> JPyObject:
    obj = JPyObject()
    obj._load(s)
    return obj
