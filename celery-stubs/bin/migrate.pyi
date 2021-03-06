from celery.bin.base import Command as Command
from typing import Any

MIGRATE_PROGRESS_FMT: str

class migrate(Command):
    args: str = ...
    progress_fmt: Any = ...
    def add_arguments(self, parser: Any) -> None: ...
    def on_migrate_task(self, state: Any, body: Any, message: Any) -> None: ...
    def run(self, source: Any, destination: Any, **kwargs: Any) -> None: ...
