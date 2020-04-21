from typing import Any, Optional

class Signature(dict):
    TYPES: Any = ...
    @classmethod
    def register_type(cls, name: Optional[Any] = ...): ...
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    def __init__(self, task: Optional[Any] = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ..., options: Optional[Any] = ..., type: Optional[Any] = ..., subtask_type: Optional[Any] = ..., immutable: bool = ..., app: Optional[Any] = ..., **ex: Any) -> None: ...
    def __call__(self, *partial_args: Any, **partial_kwargs: Any): ...
    def delay(self, *partial_args: Any, **partial_kwargs: Any): ...
    def apply(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **options: Any): ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., route_name: Optional[Any] = ..., **options: Any): ...
    def clone(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **opts: Any): ...
    partial: Any = ...
    def freeze(self, _id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ...): ...
    def replace(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., options: Optional[Any] = ...): ...
    def set(self, immutable: Optional[Any] = ..., **options: Any): ...
    immutable: Any = ...
    def set_immutable(self, immutable: Any) -> None: ...
    def append_to_list_option(self, key: Any, value: Any): ...
    def extend_list_option(self, key: Any, value: Any) -> None: ...
    def link(self, callback: Any): ...
    def link_error(self, errback: Any): ...
    def on_error(self, errback: Any): ...
    def flatten_links(self): ...
    def __or__(self, other: Any): ...
    def election(self): ...
    def reprcall(self, *args: Any, **kwargs: Any): ...
    def __deepcopy__(self, memo: Any): ...
    def __invert__(self): ...
    def __reduce__(self): ...
    def __json__(self): ...
    def items(self) -> None: ...
    @property
    def name(self): ...
    def type(self): ...
    def app(self): ...
    def AsyncResult(self): ...
    id: Any = ...
    parent_id: Any = ...
    root_id: Any = ...
    task: Any = ...
    args: Any = ...
    kwargs: Any = ...
    options: Any = ...
    subtask_type: Any = ...
    chord_size: Any = ...

class _chain(Signature):
    tasks: Any = ...
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    subtask_type: str = ...
    def __init__(self, *tasks: Any, **options: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def clone(self, *args: Any, **kwargs: Any): ...
    def unchain_tasks(self): ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **options: Any): ...
    def run(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., task_id: Optional[Any] = ..., link: Optional[Any] = ..., link_error: Optional[Any] = ..., publisher: Optional[Any] = ..., producer: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ..., app: Optional[Any] = ..., **options: Any): ...
    def freeze(self, _id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ...): ...
    def prepare_steps(self, args: Any, kwargs: Any, tasks: Any, root_id: Optional[Any] = ..., parent_id: Optional[Any] = ..., link_error: Optional[Any] = ..., app: Optional[Any] = ..., last_task_id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord_body: Optional[Any] = ..., clone: bool = ..., from_dict: Any = ...): ...
    def apply(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **options: Any): ...
    @property
    def app(self): ...

class chain(_chain):
    def __new__(cls, *tasks: Any, **kwargs: Any): ...

class _basemap(Signature):
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    def __init__(self, task: Any, it: Any, **options: Any) -> None: ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **opts: Any): ...

class xmap(_basemap): ...
class xstarmap(_basemap): ...

class chunks(Signature):
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    def __init__(self, task: Any, it: Any, n: Any, **options: Any) -> None: ...
    def __call__(self, **options: Any): ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **opts: Any): ...
    def group(self): ...
    @classmethod
    def apply_chunks(cls, task: Any, it: Any, n: Any, app: Optional[Any] = ...): ...

class group(Signature):
    tasks: Any = ...
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    subtask_type: str = ...
    def __init__(self, *tasks: Any, **options: Any) -> None: ...
    def __call__(self, *partial_args: Any, **options: Any): ...
    def skew(self, start: float = ..., stop: Optional[Any] = ..., step: float = ...): ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., add_to_parent: bool = ..., producer: Optional[Any] = ..., link: Optional[Any] = ..., link_error: Optional[Any] = ..., **options: Any): ...
    def apply(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., **options: Any): ...
    def set_immutable(self, immutable: Any) -> None: ...
    def link(self, sig: Any): ...
    def link_error(self, sig: Any): ...
    def freeze(self, _id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ...): ...
    def __len__(self): ...
    @property
    def app(self): ...

class chord(Signature):
    @classmethod
    def from_dict(cls, d: Any, app: Optional[Any] = ...): ...
    subtask_type: str = ...
    def __init__(self, header: Any, body: Optional[Any] = ..., task: str = ..., args: Optional[Any] = ..., kwargs: Optional[Any] = ..., app: Optional[Any] = ..., **options: Any) -> None: ...
    def __call__(self, body: Optional[Any] = ..., **options: Any): ...
    tasks: Any = ...
    id: Any = ...
    def freeze(self, _id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., root_id: Optional[Any] = ..., parent_id: Optional[Any] = ...): ...
    def apply_async(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., task_id: Optional[Any] = ..., producer: Optional[Any] = ..., publisher: Optional[Any] = ..., connection: Optional[Any] = ..., router: Optional[Any] = ..., result_cls: Optional[Any] = ..., **options: Any): ...
    def apply(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ..., propagate: bool = ..., body: Optional[Any] = ..., **options: Any): ...
    def __length_hint__(self): ...
    def run(self, header: Any, body: Any, partial_args: Any, app: Optional[Any] = ..., interval: Optional[Any] = ..., countdown: int = ..., max_retries: Optional[Any] = ..., eager: bool = ..., task_id: Optional[Any] = ..., **options: Any): ...
    def clone(self, *args: Any, **kwargs: Any): ...
    def link(self, callback: Any): ...
    def link_error(self, errback: Any): ...
    def set_immutable(self, immutable: Any) -> None: ...
    def app(self): ...
    body: Any = ...

def signature(varies: Any, *args: Any, **kwargs: Any): ...
subtask = signature

def maybe_signature(d: Any, app: Optional[Any] = ..., clone: bool = ...): ...
maybe_subtask = maybe_signature
