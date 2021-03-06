from . import base
from kombu.asynchronous import timer as _timer
from typing import Any, Optional

class Timer(_timer.Timer):
    GreenletExit: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def clear(self) -> None: ...
    def cancel(self, tref: Any) -> None: ...
    @property
    def queue(self): ...

class TaskPool(base.BasePool):
    Timer: Any = ...
    signal_safe: bool = ...
    is_green: bool = ...
    task_join_will_block: bool = ...
    Pool: Any = ...
    getcurrent: Any = ...
    getpid: Any = ...
    spawn_n: Any = ...
    def __init__(self, *args: Any, **kwargs: Any): ...
    def on_start(self) -> None: ...
    def on_stop(self) -> None: ...
    def on_apply(self, target: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., callback: Optional[Any] = ..., accept_callback: Optional[Any] = ..., **_: Any) -> None: ...
    limit: Any = ...
    def grow(self, n: int = ...) -> None: ...
    def shrink(self, n: int = ...) -> None: ...
