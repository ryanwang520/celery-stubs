from typing import Any

class AsyncResult:
    state: str
    info: Any
    result: Any
    id: str
    def __init__(
        self,
        id: str,
        backend: Any = None,
        task_name: str | None = None,
        app: Any = None,
        parent: Any = None,
    ): ...
