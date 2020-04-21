from typing import Any, Optional

class EventDispatcher:
    DISABLED_TRANSPORTS: Any = ...
    app: Any = ...
    on_enabled: Any = ...
    on_disabled: Any = ...
    connection: Any = ...
    channel: Any = ...
    hostname: Any = ...
    buffer_while_offline: Any = ...
    buffer_group: Any = ...
    buffer_limit: Any = ...
    on_send_buffered: Any = ...
    mutex: Any = ...
    producer: Any = ...
    serializer: Any = ...
    groups: Any = ...
    tzoffset: Any = ...
    clock: Any = ...
    delivery_mode: Any = ...
    enabled: Any = ...
    exchange: Any = ...
    headers: Any = ...
    pid: Any = ...
    def __init__(self, connection: Optional[Any] = ..., hostname: Optional[Any] = ..., enabled: bool = ..., channel: Optional[Any] = ..., buffer_while_offline: bool = ..., app: Optional[Any] = ..., serializer: Optional[Any] = ..., groups: Optional[Any] = ..., delivery_mode: int = ..., buffer_group: Optional[Any] = ..., buffer_limit: int = ..., on_send_buffered: Optional[Any] = ...) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *exc_info: Any) -> None: ...
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    def publish(self, type: Any, fields: Any, producer: Any, blind: bool = ..., Event: Any = ..., **kwargs: Any): ...
    def send(self, type: Any, blind: bool = ..., utcoffset: Any = ..., retry: bool = ..., retry_policy: Optional[Any] = ..., Event: Any = ..., **fields: Any): ...
    def flush(self, errors: bool = ..., groups: bool = ...) -> None: ...
    def extend_buffer(self, other: Any) -> None: ...
    def close(self) -> None: ...
    publisher: Any = ...
