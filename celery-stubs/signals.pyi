from collections.abc import Callable
from typing import TypeVar

before_task_publish: BeforePublish

Fn = TypeVar("Fn", bound=Callable[..., None])

class BeforePublish:
    def connect(self, fn: Fn) -> Fn: ...
