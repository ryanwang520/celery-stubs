# Test file to run with mypy. Should produce no output.

from typing_extensions import assert_type

from celery import Celery, Task
from celery.result import AsyncResult, EagerResult

app = Celery("spam")


# Test that @app.task decorator works
@app.task
def bare_task(arg: int) -> str: ...


assert_type(bare_task(1), str)
assert_type(bare_task.delay(1), AsyncResult[str])


@app.task(name="ubnound_task")
def ubnound_task(arg: int) -> str: ...


assert_type(ubnound_task(1), str)
assert_type(ubnound_task.delay(1), AsyncResult[str])


@app.task(bind=True, name="bound_task")
def bound_task(task: Task, arg: int) -> str: ...


assert_type(bound_task(1), str)
assert_type(bound_task.delay(1), AsyncResult[str])

# Test various calling conventions
assert_type(bound_task(arg=1), str)
assert_type(bound_task.delay(arg=1), AsyncResult[str])

assert_type(bound_task.apply_async(args=(1,)), AsyncResult[str])
assert_type(bound_task.apply_async(kwargs={'arg': 1}), AsyncResult[str])

assert_type(bound_task.apply(args=(1,)), EagerResult[str])
