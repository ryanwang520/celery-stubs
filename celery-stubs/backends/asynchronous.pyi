from typing import Any, Optional

def register_drainer(name: Any): ...

class Drainer:
    result_consumer: Any = ...
    def __init__(self, result_consumer: Any) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def drain_events_until(self, p: Any, timeout: Optional[Any] = ..., interval: int = ..., on_interval: Optional[Any] = ..., wait: Optional[Any] = ...) -> None: ...
    def wait_for(self, p: Any, wait: Any, timeout: Optional[Any] = ...) -> None: ...

class greenletDrainer(Drainer):
    spawn: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class eventletDrainer(greenletDrainer):
    def spawn(self, func: Any): ...
    def wait_for(self, p: Any, wait: Any, timeout: Optional[Any] = ...) -> None: ...

class geventDrainer(greenletDrainer):
    def spawn(self, func: Any): ...
    def wait_for(self, p: Any, wait: Any, timeout: Optional[Any] = ...) -> None: ...

class AsyncBackendMixin:
    def iter_native(self, result: Any, no_ack: bool = ..., **kwargs: Any) -> None: ...
    def add_pending_result(self, result: Any, weak: bool = ..., start_drainer: bool = ...): ...
    def add_pending_results(self, results: Any, weak: bool = ...): ...
    def remove_pending_result(self, result: Any): ...
    def on_result_fulfilled(self, result: Any) -> None: ...
    def wait_for_pending(self, result: Any, callback: Optional[Any] = ..., propagate: bool = ..., **kwargs: Any): ...
    @property
    def is_async(self): ...

class BaseResultConsumer:
    backend: Any = ...
    app: Any = ...
    accept: Any = ...
    on_message: Any = ...
    buckets: Any = ...
    drainer: Any = ...
    def __init__(self, backend: Any, app: Any, accept: Any, pending_results: Any, pending_messages: Any) -> None: ...
    def start(self, initial_task_id: Any, **kwargs: Any) -> None: ...
    def stop(self) -> None: ...
    def drain_events(self, timeout: Optional[Any] = ...) -> None: ...
    def consume_from(self, task_id: Any) -> None: ...
    def cancel_for(self, task_id: Any) -> None: ...
    def on_after_fork(self) -> None: ...
    def drain_events_until(self, p: Any, timeout: Optional[Any] = ..., on_interval: Optional[Any] = ...): ...
    def on_wait_for_pending(self, result: Any, timeout: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def on_out_of_band_result(self, message: Any) -> None: ...
    def on_state_change(self, meta: Any, message: Any) -> None: ...