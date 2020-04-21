from .asynchronous import AsyncBackendMixin, BaseResultConsumer
from .base import BaseKeyValueStoreBackend
from typing import Any, Optional

class ResultConsumer(BaseResultConsumer):
    subscribed_to: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def on_after_fork(self) -> None: ...
    def reconnect_on_error(self) -> None: ...
    def on_state_change(self, meta: Any, message: Any) -> None: ...
    def start(self, initial_task_id: Any, **kwargs: Any) -> None: ...
    def on_wait_for_pending(self, result: Any, **kwargs: Any) -> None: ...
    def stop(self) -> None: ...
    def drain_events(self, timeout: Optional[Any] = ...) -> None: ...
    def consume_from(self, task_id: Any): ...
    def cancel_for(self, task_id: Any) -> None: ...

class RedisBackend(BaseKeyValueStoreBackend, AsyncBackendMixin):
    ResultConsumer: Any = ...
    redis: Any = ...
    max_connections: Any = ...
    supports_autoexpire: bool = ...
    supports_native_join: bool = ...
    connparams: Any = ...
    url: Any = ...
    result_consumer: Any = ...
    def __init__(self, host: Optional[Any] = ..., port: Optional[Any] = ..., db: Optional[Any] = ..., password: Optional[Any] = ..., max_connections: Optional[Any] = ..., url: Optional[Any] = ..., connection_pool: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def on_task_call(self, producer: Any, task_id: Any) -> None: ...
    def get(self, key: Any): ...
    def mget(self, keys: Any): ...
    def ensure(self, fun: Any, args: Any, **policy: Any): ...
    def on_connection_error(self, max_retries: Any, exc: Any, intervals: Any, retries: Any): ...
    def set(self, key: Any, value: Any, **retry_policy: Any): ...
    def forget(self, task_id: Any) -> None: ...
    def delete(self, key: Any) -> None: ...
    def incr(self, key: Any): ...
    def expire(self, key: Any, value: Any): ...
    def add_to_chord(self, group_id: Any, result: Any) -> None: ...
    def apply_chord(self, header_result: Any, body: Any, **kwargs: Any) -> None: ...
    def on_chord_part_return(self, request: Any, state: Any, result: Any, propagate: Optional[Any] = ..., **kwargs: Any): ...
    @property
    def ConnectionPool(self): ...
    def client(self): ...
    def __reduce__(self, args: Any = ..., kwargs: Optional[Any] = ...): ...
    def host(self): ...
    def port(self): ...
    def db(self): ...
    def password(self): ...

class SentinelBackend(RedisBackend):
    sentinel: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
