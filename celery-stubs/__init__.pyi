from collections.abc import Callable
from typing import (
    Any,
    Concatenate,
    Generic,
    Literal,
    NotRequired,
    ParamSpec,
    TypedDict,
    TypeVar,
    overload,
)

from .result import AsyncResult

def __getattr__(name: str) -> Any: ...

P = ParamSpec("P")
T = TypeVar("T")

class Signature:
    pass

class Request:
    id: str
    properties: Any

class TaskGeneric(Generic[P, T]):
    name: str
    request: Request
    def update_state(self, state: Any = ..., meta: Any = ...) -> None: ...
    def run(self) -> Any: ...
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...
    def delay(self, *args: P.args, **kwargs: P.kwargs) -> AsyncResult: ...
    def apply_async(self, *args: Any, **kwargs: Any) -> AsyncResult: ...
    def si(self, *args: Any, **kwargs: Any) -> Signature: ...
    def s(self, *args: Any, **kwargs: Any) -> Signature: ...
    def retry(
        self, exc: Exception | None = ..., countdown: int | None = None
    ) -> Any: ...

class Task(TaskGeneric[Any, Any]):
    pass

class RetryArgs(TypedDict):
    max_retries: NotRequired[int]

# Case 1: shared_task is used as a decorator directly without any arguments.
@overload
def shared_task(func: Callable[P, T]) -> TaskGeneric[P, T]: ...

# Case 2: shared_task is called with keyword arguments and bind is set to False.
@overload
def shared_task(
    *,
    name: str | None = None,
    bind: Literal[False] = False,
    autoretry_for: tuple[type[Exception], ...] | None = None,
    base: type[Task] | None = None,
    default_retry_delay: int | None = None,
    retry_kwargs: RetryArgs | None = None,
) -> Callable[[Callable[P, T]], TaskGeneric[P, T]]: ...

# Case 3: shared_task is called with keyword arguments and bind is set to True.
@overload
def shared_task(
    *,
    name: str | None = None,
    bind: Literal[True],
    autoretry_for: tuple[type[Exception], ...] | None = None,
    base: type[Task] | None = None,
    default_retry_delay: int | None = None,
    retry_kwargs: RetryArgs | None = None,
) -> Callable[[Callable[Concatenate[Task, P], T]], TaskGeneric[P, T]]: ...
