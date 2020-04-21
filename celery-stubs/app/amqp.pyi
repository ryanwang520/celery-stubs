from collections import namedtuple
from typing import Any, Optional

task_message = namedtuple('task_message', ['headers', 'properties', 'body', 'sent_event'])

class Queues(dict):
    aliases: Any = ...
    default_exchange: Any = ...
    default_routing_key: Any = ...
    create_missing: Any = ...
    ha_policy: Any = ...
    autoexchange: Any = ...
    max_priority: Any = ...
    def __init__(self, queues: Optional[Any] = ..., default_exchange: Optional[Any] = ..., create_missing: bool = ..., ha_policy: Optional[Any] = ..., autoexchange: Optional[Any] = ..., max_priority: Optional[Any] = ..., default_routing_key: Optional[Any] = ...) -> None: ...
    def __getitem__(self, name: Any): ...
    def __setitem__(self, name: Any, queue: Any) -> None: ...
    def __missing__(self, name: Any): ...
    def add(self, queue: Any, **kwargs: Any): ...
    def add_compat(self, name: Any, **options: Any): ...
    def format(self, indent: int = ..., indent_first: bool = ...): ...
    def select_add(self, queue: Any, **kwargs: Any): ...
    def select(self, include: Any) -> None: ...
    def deselect(self, exclude: Any): ...
    def new_missing(self, name: Any): ...
    @property
    def consume_from(self): ...

class AMQP:
    Connection: Any = ...
    Consumer: Any = ...
    Producer: Any = ...
    BrokerConnection: Any = ...
    queues_cls: Any = ...
    autoexchange: Any = ...
    argsrepr_maxsize: int = ...
    kwargsrepr_maxsize: int = ...
    app: Any = ...
    task_protocols: Any = ...
    def __init__(self, app: Any) -> None: ...
    def create_task_message(self): ...
    def send_task_message(self): ...
    def Queues(self, queues: Any, create_missing: Optional[Any] = ..., ha_policy: Optional[Any] = ..., autoexchange: Optional[Any] = ..., max_priority: Optional[Any] = ...): ...
    def Router(self, queues: Optional[Any] = ..., create_missing: Optional[Any] = ...): ...
    def flush_routes(self) -> None: ...
    def TaskConsumer(self, channel: Any, queues: Optional[Any] = ..., accept: Optional[Any] = ..., **kw: Any): ...
    def as_task_v2(self, task_id: Any, name: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., countdown: Optional[Any] = ..., eta: Optional[Any] = ..., group_id: Optional[Any] = ..., expires: Optional[Any] = ..., retries: int = ..., chord: Optional[Any] = ..., callbacks: Optional[Any] = ..., errbacks: Optional[Any] = ..., reply_to: Optional[Any] = ..., time_limit: Optional[Any] = ..., soft_time_limit: Optional[Any] = ..., create_sent_event: bool = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ..., shadow: Optional[Any] = ..., chain: Optional[Any] = ..., now: Optional[Any] = ..., timezone: Optional[Any] = ..., origin: Optional[Any] = ..., argsrepr: Optional[Any] = ..., kwargsrepr: Optional[Any] = ...): ...
    def as_task_v1(self, task_id: Any, name: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., countdown: Optional[Any] = ..., eta: Optional[Any] = ..., group_id: Optional[Any] = ..., expires: Optional[Any] = ..., retries: int = ..., chord: Optional[Any] = ..., callbacks: Optional[Any] = ..., errbacks: Optional[Any] = ..., reply_to: Optional[Any] = ..., time_limit: Optional[Any] = ..., soft_time_limit: Optional[Any] = ..., create_sent_event: bool = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ..., shadow: Optional[Any] = ..., now: Optional[Any] = ..., timezone: Optional[Any] = ..., **compat_kwargs: Any): ...
    def default_queue(self): ...
    @queues.setter
    def queues(self, queues: Any): ...
    @property
    def routes(self): ...
    @router.setter
    def router(self, value: Any): ...
    @property
    def producer_pool(self): ...
    publisher_pool: Any = ...
    def default_exchange(self): ...
    def utc(self): ...

# Names in __all__ with no definition:
#   task_message