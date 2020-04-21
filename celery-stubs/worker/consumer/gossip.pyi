from celery import bootsteps
from typing import Any, Optional

class Gossip(bootsteps.ConsumerStep):
    label: str = ...
    requires: Any = ...
    compatible_transports: Any = ...
    enabled: Any = ...
    app: Any = ...
    Receiver: Any = ...
    hostname: Any = ...
    full_hostname: Any = ...
    on: Any = ...
    timer: Any = ...
    state: Any = ...
    update_state: Any = ...
    interval: Any = ...
    heartbeat_interval: Any = ...
    consensus_requests: Any = ...
    consensus_replies: Any = ...
    event_handlers: Any = ...
    clock: Any = ...
    election_handlers: Any = ...
    def __init__(self, c: Any, without_gossip: bool = ..., interval: float = ..., heartbeat_interval: float = ..., **kwargs: Any) -> None: ...
    def compatible_transport(self, app: Any): ...
    def election(self, id: Any, topic: Any, action: Optional[Any] = ...) -> None: ...
    def call_task(self, task: Any) -> None: ...
    def on_elect(self, event: Any): ...
    dispatcher: Any = ...
    def start(self, c: Any) -> None: ...
    def on_elect_ack(self, event: Any) -> None: ...
    def on_node_join(self, worker: Any) -> None: ...
    def on_node_leave(self, worker: Any) -> None: ...
    def on_node_lost(self, worker: Any) -> None: ...
    def register_timer(self) -> None: ...
    def periodic(self) -> None: ...
    def get_consumers(self, channel: Any): ...
    def on_message(self, prepare: Any, message: Any): ...