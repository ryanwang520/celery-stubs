from typing import Any, Optional

class Request:
    acknowledged: bool = ...
    time_start: Any = ...
    worker_pid: Any = ...
    time_limits: Any = ...
    id: Any = ...
    name: Any = ...
    def __init__(self, message: Any, on_ack: Any = ..., hostname: Optional[Any] = ..., eventer: Optional[Any] = ..., app: Optional[Any] = ..., connection_errors: Optional[Any] = ..., request_dict: Optional[Any] = ..., task: Optional[Any] = ..., on_reject: Any = ..., body: Optional[Any] = ..., headers: Optional[Any] = ..., decoded: bool = ..., utc: bool = ..., maybe_make_aware: Any = ..., maybe_iso8601: Any = ..., **opts: Any) -> None: ...
    @property
    def delivery_info(self): ...
    @property
    def message(self): ...
    @property
    def request_dict(self): ...
    @property
    def body(self): ...
    @property
    def app(self): ...
    @property
    def utc(self): ...
    @property
    def content_type(self): ...
    @property
    def content_encoding(self): ...
    @property
    def type(self): ...
    @property
    def root_id(self): ...
    @property
    def parent_id(self): ...
    @property
    def argsrepr(self): ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...
    @property
    def kwargsrepr(self): ...
    @property
    def on_ack(self): ...
    @property
    def on_reject(self): ...
    @on_reject.setter
    def on_reject(self, value: Any) -> None: ...
    @property
    def hostname(self): ...
    @property
    def eventer(self): ...
    @eventer.setter
    def eventer(self, eventer: Any) -> None: ...
    @property
    def connection_errors(self): ...
    @property
    def task(self): ...
    @property
    def eta(self): ...
    @property
    def expires(self): ...
    @expires.setter
    def expires(self, value: Any) -> None: ...
    @property
    def tzlocal(self): ...
    @property
    def store_errors(self): ...
    @property
    def task_id(self): ...
    @task_id.setter
    def task_id(self, value: Any) -> None: ...
    @property
    def task_name(self): ...
    @task_name.setter
    def task_name(self, value: Any) -> None: ...
    @property
    def reply_to(self): ...
    @property
    def correlation_id(self): ...
    def execute_using_pool(self, pool: Any, **kwargs: Any): ...
    def execute(self, loglevel: Optional[Any] = ..., logfile: Optional[Any] = ...): ...
    def maybe_expire(self): ...
    def terminate(self, pool: Any, signal: Optional[Any] = ...) -> None: ...
    def revoked(self): ...
    def send_event(self, type: Any, **fields: Any) -> None: ...
    def on_accepted(self, pid: Any, time_accepted: Any) -> None: ...
    def on_timeout(self, soft: Any, timeout: Any) -> None: ...
    def on_success(self, failed__retval__runtime: Any, **kwargs: Any): ...
    def on_retry(self, exc_info: Any) -> None: ...
    def on_failure(self, exc_info: Any, send_failed_event: bool = ..., return_ok: bool = ...): ...
    def acknowledge(self) -> None: ...
    def reject(self, requeue: bool = ...) -> None: ...
    def info(self, safe: bool = ...): ...
    def humaninfo(self): ...
    def chord(self): ...
    def errbacks(self): ...
    def group(self): ...
