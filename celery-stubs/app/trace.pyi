from collections import namedtuple
from typing import Any, Optional

log_policy_t = namedtuple('log_policy_t', ['format', 'description', 'severity', 'traceback', 'mail'])

trace_ok_t = namedtuple('trace_ok_t', ['retval', 'info', 'runtime', 'retstr'])

class TraceInfo:
    state: Any = ...
    retval: Any = ...
    def __init__(self, state: Any, retval: Optional[Any] = ...) -> None: ...
    def handle_error_state(self, task: Any, req: Any, eager: bool = ..., call_errbacks: bool = ...): ...
    def handle_reject(self, task: Any, req: Any, **kwargs: Any) -> None: ...
    def handle_ignore(self, task: Any, req: Any, **kwargs: Any) -> None: ...
    def handle_retry(self, task: Any, req: Any, store_errors: bool = ..., **kwargs: Any): ...
    def handle_failure(self, task: Any, req: Any, store_errors: bool = ..., call_errbacks: bool = ...): ...

def build_tracer(name: Any, task: Any, loader: Optional[Any] = ..., hostname: Optional[Any] = ..., store_errors: bool = ..., Info: Any = ..., eager: bool = ..., propagate: bool = ..., app: Optional[Any] = ..., monotonic: Any = ..., trace_ok_t: Any = ..., IGNORE_STATES: Any = ...): ...
def trace_task(task: Any, uuid: Any, args: Any, kwargs: Any, request: Optional[Any] = ..., **opts: Any): ...
def setup_worker_optimizations(app: Any, hostname: Optional[Any] = ...) -> None: ...
def reset_worker_optimizations() -> None: ...
