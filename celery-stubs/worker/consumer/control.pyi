from celery import bootsteps
from typing import Any

class Control(bootsteps.StartStopStep):
    requires: Any = ...
    is_green: Any = ...
    box: Any = ...
    start: Any = ...
    stop: Any = ...
    shutdown: Any = ...
    def __init__(self, c: Any, **kwargs: Any) -> None: ...
    def include_if(self, c: Any): ...
