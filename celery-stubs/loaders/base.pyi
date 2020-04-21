from typing import Any, Optional

class BaseLoader:
    builtin_modules: Any = ...
    configured: bool = ...
    override_backends: Any = ...
    worker_initialized: bool = ...
    app: Any = ...
    task_modules: Any = ...
    def __init__(self, app: Any, **kwargs: Any) -> None: ...
    def now(self, utc: bool = ...): ...
    def on_task_init(self, task_id: Any, task: Any) -> None: ...
    def on_process_cleanup(self) -> None: ...
    def on_worker_init(self) -> None: ...
    def on_worker_shutdown(self) -> None: ...
    def on_worker_process_init(self) -> None: ...
    def import_task_module(self, module: Any): ...
    def import_module(self, module: Any, package: Optional[Any] = ...): ...
    def import_from_cwd(self, module: Any, imp: Optional[Any] = ..., package: Optional[Any] = ...): ...
    def import_default_modules(self): ...
    def init_worker(self) -> None: ...
    def shutdown_worker(self) -> None: ...
    def init_worker_process(self) -> None: ...
    def config_from_object(self, obj: Any, silent: bool = ...): ...
    def find_module(self, module: Any): ...
    def cmdline_config_parser(self, args: Any, namespace: str = ..., re_type: Any = ..., extra_types: Optional[Any] = ..., override_types: Optional[Any] = ...): ...
    def read_configuration(self, env: str = ...): ...
    def autodiscover_tasks(self, packages: Any, related_name: str = ...) -> None: ...
    def default_modules(self): ...
    @property
    def conf(self): ...