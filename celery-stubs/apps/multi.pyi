from celery.five import UserList
from typing import Any, Optional

class NamespacedOptionParser:
    args: Any = ...
    options: Any = ...
    values: Any = ...
    passthrough: str = ...
    namespaces: Any = ...
    def __init__(self, args: Any): ...
    def parse(self) -> None: ...
    def process_long_opt(self, arg: Any, value: Optional[Any] = ...) -> None: ...
    def process_short_opt(self, arg: Any, value: Optional[Any] = ...) -> None: ...
    def optmerge(self, ns: Any, defaults: Optional[Any] = ...): ...
    def add_option(self, name: Any, value: Any, short: bool = ..., ns: Optional[Any] = ...) -> None: ...

class Node:
    name: Any = ...
    cmd: Any = ...
    append: Any = ...
    extra_args: Any = ...
    options: Any = ...
    expander: Any = ...
    argv: Any = ...
    def __init__(self, name: Any, cmd: Optional[Any] = ..., append: Optional[Any] = ..., options: Optional[Any] = ..., extra_args: Optional[Any] = ...) -> None: ...
    def alive(self): ...
    def send(self, sig: Any, on_error: Optional[Any] = ...): ...
    def start(self, env: Optional[Any] = ..., **kwargs: Any): ...
    def handle_process_exit(self, retcode: Any, on_signalled: Optional[Any] = ..., on_failure: Optional[Any] = ...): ...
    def prepare_argv(self, argv: Any, path: Any): ...
    def getopt(self, *alt: Any): ...
    def pidfile(self): ...
    def logfile(self): ...
    @property
    def pid(self): ...
    @pid.setter
    def pid(self, value: Any) -> None: ...
    def executable(self): ...
    def argv_with_executable(self): ...
    @classmethod
    def from_kwargs(cls, name: Any, **kwargs: Any): ...

class MultiParser:
    Node: Any = ...
    cmd: Any = ...
    append: Any = ...
    prefix: Any = ...
    suffix: Any = ...
    range_prefix: Any = ...
    def __init__(self, cmd: str = ..., append: str = ..., prefix: str = ..., suffix: str = ..., range_prefix: str = ...) -> None: ...
    def parse(self, p: Any): ...

class Cluster(UserList):
    nodes: Any = ...
    cmd: Any = ...
    env: Any = ...
    on_stopping_preamble: Any = ...
    on_send_signal: Any = ...
    on_still_waiting_for: Any = ...
    on_still_waiting_progress: Any = ...
    on_still_waiting_end: Any = ...
    on_node_start: Any = ...
    on_node_restart: Any = ...
    on_node_shutdown_ok: Any = ...
    on_node_status: Any = ...
    on_node_signal: Any = ...
    on_node_signal_dead: Any = ...
    on_node_down: Any = ...
    on_child_spawn: Any = ...
    on_child_signalled: Any = ...
    on_child_failure: Any = ...
    def __init__(self, nodes: Any, cmd: Optional[Any] = ..., env: Optional[Any] = ..., on_stopping_preamble: Optional[Any] = ..., on_send_signal: Optional[Any] = ..., on_still_waiting_for: Optional[Any] = ..., on_still_waiting_progress: Optional[Any] = ..., on_still_waiting_end: Optional[Any] = ..., on_node_start: Optional[Any] = ..., on_node_restart: Optional[Any] = ..., on_node_shutdown_ok: Optional[Any] = ..., on_node_status: Optional[Any] = ..., on_node_signal: Optional[Any] = ..., on_node_signal_dead: Optional[Any] = ..., on_node_down: Optional[Any] = ..., on_child_spawn: Optional[Any] = ..., on_child_signalled: Optional[Any] = ..., on_child_failure: Optional[Any] = ...) -> None: ...
    def start(self): ...
    def start_node(self, node: Any): ...
    def send_all(self, sig: Any) -> None: ...
    def kill(self): ...
    def restart(self, sig: Any = ...): ...
    def stop(self, retry: Optional[Any] = ..., callback: Optional[Any] = ..., sig: Any = ...): ...
    def stopwait(self, retry: int = ..., callback: Optional[Any] = ..., sig: Any = ...): ...
    def shutdown_nodes(self, nodes: Any, sig: Any = ..., retry: Optional[Any] = ...) -> None: ...
    def find(self, name: Any): ...
    def getpids(self, on_down: Optional[Any] = ...) -> None: ...
    @property
    def data(self): ...
