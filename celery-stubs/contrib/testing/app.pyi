from celery import Celery as Celery
from typing import Any, Optional

DEFAULT_TEST_CONFIG: Any

class Trap:
    def __getattr__(self, name: Any) -> None: ...

class UnitLogging:
    already_setup: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

def TestApp(name: Optional[Any] = ..., config: Optional[Any] = ..., enable_logging: bool = ..., set_as_current: bool = ..., log: Any = ..., backend: Optional[Any] = ..., broker: Optional[Any] = ..., **kwargs: Any): ...
def set_trap(app: Any) -> None: ...
def setup_default_app(app: Any, use_trap: bool = ...) -> None: ...
