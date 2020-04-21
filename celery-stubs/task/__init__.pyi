from .base import BaseTask as BaseTask, PeriodicTask as PeriodicTask, Task as Task, periodic_task as periodic_task, task as task
from celery.canvas import chord as chord, group as group, subtask as subtask
from celery.local import LazyModule
from typing import Any

class module(LazyModule):
    def __call__(self, *args: Any, **kwargs: Any): ...
