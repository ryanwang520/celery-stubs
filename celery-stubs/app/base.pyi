from typing import Any, Optional, Callable, TypeVar, ParamSpec, overload, Literal, Concatenate

from celery.five import UserDict
from celery.app.task import Task
from celery.utils.collections import AttributeDictMixin

P = ParamSpec('P')
R = TypeVar('R')


class PendingConfiguration(UserDict, AttributeDictMixin):
    callback: Any = ...
    def __init__(self, conf: Any, callback: Any) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def clear(self) -> None: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def setdefault(self, *args: Any, **kwargs: Any): ...
    def __contains__(self, key: Any): ...
    def __len__(self): ...
    def data(self): ...

class Celery:
    Pickler: Any = ...
    SYSTEM: Any = ...
    IS_macOS: Any = ...
    IS_WINDOWS: Any = ...
    main: Any = ...
    user_options: Any = ...
    steps: Any = ...
    builtin_fixups: Any = ...
    amqp_cls: str = ...
    backend_cls: Any = ...
    events_cls: str = ...
    loader_cls: Any = ...
    log_cls: str = ...
    control_cls: str = ...
    task_cls: str = ...
    registry_cls: str = ...
    on_configure: Any = ...
    on_after_configure: Any = ...
    on_after_finalize: Any = ...
    on_after_fork: Any = ...
    clock: Any = ...
    set_as_current: Any = ...
    autofinalize: Any = ...
    namespace: Any = ...
    strict_typing: Any = ...
    configured: bool = ...
    finalized: bool = ...
    fixups: Any = ...
    def __init__(self, main: Optional[Any] = ..., loader: Optional[Any] = ..., backend: Optional[Any] = ..., amqp: Optional[Any] = ..., events: Optional[Any] = ..., log: Optional[Any] = ..., control: Optional[Any] = ..., set_as_current: bool = ..., tasks: Optional[Any] = ..., broker: Optional[Any] = ..., include: Optional[Any] = ..., changes: Optional[Any] = ..., config_source: Optional[Any] = ..., fixups: Optional[Any] = ..., task_cls: Optional[Any] = ..., autofinalize: bool = ..., namespace: Optional[Any] = ..., strict_typing: bool = ..., **kwargs: Any) -> None: ...
    def on_init(self) -> None: ...
    def set_current(self) -> None: ...
    def set_default(self) -> None: ...
    def close(self) -> None: ...
    def start(self, argv: Optional[Any] = ...): ...
    def worker_main(self, argv: Optional[Any] = ...): ...
    @overload
    def task(self, __func: Callable[P, R]) -> Task[P, R]: ...
    @overload
    def task(self, *, bind: Literal[True], **opts: Any) -> Callable[[Callable[Concatenate[Task, P], R]], Task[P, R]]: ...
    @overload
    def task(self, *, bind: Literal[False]=..., **opts: Any) -> Callable[[Callable[P, R]], Task[P, R]]: ...
    def register_task(self, task: Any): ...
    def gen_task_name(self, name: Any, module: Any): ...
    def finalize(self, auto: bool = ...) -> None: ...
    def add_defaults(self, fun: Any): ...
    def config_from_object(self, obj: Any, silent: bool = ..., force: bool = ..., namespace: Optional[Any] = ...): ...
    def config_from_envvar(self, variable_name: Any, silent: bool = ..., force: bool = ...): ...
    def config_from_cmdline(self, argv: Any, namespace: str = ...) -> None: ...
    def setup_security(self, allowed_serializers: Optional[Any] = ..., key: Optional[Any] = ..., cert: Optional[Any] = ..., store: Optional[Any] = ..., digest: Any = ..., serializer: str = ...): ...
    def autodiscover_tasks(self, packages: Optional[Any] = ..., related_name: str = ..., force: bool = ...): ...
    def send_task(self, name: Any, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., countdown: Optional[Any] = ..., eta: Optional[Any] = ..., task_id: Optional[Any] = ..., producer: Optional[Any] = ..., connection: Optional[Any] = ..., router: Optional[Any] = ..., result_cls: Optional[Any] = ..., expires: Optional[Any] = ..., publisher: Optional[Any] = ..., link: Optional[Any] = ..., link_error: Optional[Any] = ..., add_to_parent: bool = ..., group_id: Optional[Any] = ..., retries: int = ..., chord: Optional[Any] = ..., reply_to: Optional[Any] = ..., time_limit: Optional[Any] = ..., soft_time_limit: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ..., route_name: Optional[Any] = ..., shadow: Optional[Any] = ..., chain: Optional[Any] = ..., task_type: Optional[Any] = ..., **options: Any): ...
    def connection_for_read(self, url: Optional[Any] = ..., **kwargs: Any): ...
    def connection_for_write(self, url: Optional[Any] = ..., **kwargs: Any): ...
    def connection(self, hostname: Optional[Any] = ..., userid: Optional[Any] = ..., password: Optional[Any] = ..., virtual_host: Optional[Any] = ..., port: Optional[Any] = ..., ssl: Optional[Any] = ..., connect_timeout: Optional[Any] = ..., transport: Optional[Any] = ..., transport_options: Optional[Any] = ..., heartbeat: Optional[Any] = ..., login_method: Optional[Any] = ..., failover_strategy: Optional[Any] = ..., **kwargs: Any): ...
    broker_connection: Any = ...
    def connection_or_acquire(self, connection: Optional[Any] = ..., pool: bool = ..., *_: Any, **__: Any): ...
    default_connection: Any = ...
    def producer_or_acquire(self, producer: Optional[Any] = ...): ...
    default_producer: Any = ...
    def prepare_config(self, c: Any): ...
    def now(self): ...
    def select_queues(self, queues: Optional[Any] = ...): ...
    def either(self, default_key: Any, *defaults: Any): ...
    def bugreport(self): ...
    def signature(self, *args: Any, **kwargs: Any): ...
    def add_periodic_task(self, schedule: Any, sig: Any, args: Any = ..., kwargs: Any = ..., name: Optional[Any] = ..., **opts: Any): ...
    def create_task_cls(self): ...
    def subclass_with_self(self, Class: Any, name: Optional[Any] = ..., attribute: str = ..., reverse: Optional[Any] = ..., keep_reduce: bool = ..., **kw: Any): ...
    def __enter__(self): ...
    def __exit__(self, *exc_info: Any) -> None: ...
    def __reduce__(self): ...
    def __reduce_v1__(self): ...
    def __reduce_keys__(self): ...
    def __reduce_args__(self): ...
    def Worker(self): ...
    def WorkController(self, **kwargs: Any): ...
    def Beat(self, **kwargs: Any): ...
    def Task(self): ...
    def annotations(self): ...
    def AsyncResult(self): ...
    def ResultSet(self): ...
    def GroupResult(self): ...
    @property
    def pool(self): ...
    @property
    def current_task(self): ...
    @property
    def current_worker_task(self): ...
    def oid(self): ...
    def amqp(self): ...
    def backend(self): ...
    @property
    def conf(self): ...
    @conf.setter
    def conf(self, d: Any) -> None: ...
    def control(self): ...
    def events(self): ...
    def loader(self): ...
    def log(self): ...
    def tasks(self): ...
    @property
    def producer_pool(self): ...
    def uses_utc_timezone(self): ...
    def timezone(self): ...

App = Celery
