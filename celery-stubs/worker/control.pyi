from celery.five import UserDict
from collections import namedtuple
from typing import Any

controller_info_t = namedtuple('controller_info_t', ['alias', 'type', 'visible', 'default_timeout', 'help', 'signature', 'args', 'variadic'])

class Panel(UserDict):
    data: Any = ...
    meta: Any = ...
    @classmethod
    def register(cls, *args: Any, **kwargs: Any): ...
