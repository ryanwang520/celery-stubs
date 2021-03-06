from typing import Any, Optional

def subclass_exception(name: Any, parent: Any, module: Any): ...
def find_pickleable_exception(exc: Any, loads: Any = ..., dumps: Any = ...): ...
def create_exception_cls(name: Any, module: Any, parent: Optional[Any] = ...): ...

class UnpickleableExceptionWrapper(Exception):
    exc_module: Any = ...
    exc_cls_name: Any = ...
    exc_args: Any = ...
    text: Any = ...
    def __init__(self, exc_module: Any, exc_cls_name: Any, exc_args: Any, text: Optional[Any] = ...) -> None: ...
    def restore(self): ...
    @classmethod
    def from_exception(cls, exc: Any): ...

def get_pickleable_exception(exc: Any): ...
def get_pickleable_etype(cls, loads: Any = ..., dumps: Any = ...): ...
def get_pickled_exception(exc: Any): ...
def strtobool(term: Any, table: Optional[Any] = ...): ...
