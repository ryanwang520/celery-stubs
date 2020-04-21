from .base import Celery as Celery
from .utils import AppPickler as AppPickler
from celery._state import app_or_default as app_or_default, disable_trace as disable_trace, enable_trace as enable_trace, pop_current_task as pop_current_task, push_current_task as push_current_task
from typing import Any, Optional

default_app: Any

def bugreport(app: Optional[Any] = ...): ...
def shared_task(*args: Any, **kwargs: Any): ...
