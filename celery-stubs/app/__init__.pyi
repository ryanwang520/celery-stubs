from .base import Celery as Celery
from .utils import AppPickler as AppPickler
from celery._state import app_or_default as app_or_default, disable_trace as disable_trace, enable_trace as enable_trace, pop_current_task as pop_current_task, push_current_task as push_current_task
from typing import Any, Optional, TypeVar, Callable, overload

F = TypeVar('F', bound=Callable[..., Any])

default_app: Celery

def bugreport(app: Optional[Celery] = ...): ...
@overload
def shared_task(__func: F, **kwargs: Any) -> F: ...
@overload
def shared_task(*args: Any, **kwargs: Any) -> Callable[[F], F]: ...
