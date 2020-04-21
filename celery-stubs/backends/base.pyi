from collections import namedtuple
from typing import Any, Optional

pending_results_t = namedtuple('pending_results_t', ['concrete', 'weak'])

class _nulldict(dict):
    def ignore(self, *a: Any, **kw: Any) -> None: ...
    __setitem__: Any = ...
    update: Any = ...
    setdefault: Any = ...

class Backend:
    READY_STATES: Any = ...
    UNREADY_STATES: Any = ...
    EXCEPTION_STATES: Any = ...
    TimeoutError: Any = ...
    subpolling_interval: Any = ...
    supports_native_join: bool = ...
    supports_autoexpire: bool = ...
    persistent: bool = ...
    retry_policy: Any = ...
    app: Any = ...
    serializer: Any = ...
    expires: Any = ...
    accept: Any = ...
    url: Any = ...
    def __init__(self, app: Any, serializer: Optional[Any] = ..., max_cached_results: Optional[Any] = ..., accept: Optional[Any] = ..., expires: Optional[Any] = ..., expires_type: Optional[Any] = ..., url: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def as_uri(self, include_password: bool = ...): ...
    def mark_as_started(self, task_id: Any, **meta: Any): ...
    def mark_as_done(self, task_id: Any, result: Any, request: Optional[Any] = ..., store_result: bool = ..., state: Any = ...) -> None: ...
    def mark_as_failure(self, task_id: Any, exc: Any, traceback: Optional[Any] = ..., request: Optional[Any] = ..., store_result: bool = ..., call_errbacks: bool = ..., state: Any = ...) -> None: ...
    def mark_as_revoked(self, task_id: Any, reason: str = ..., request: Optional[Any] = ..., store_result: bool = ..., state: Any = ...) -> None: ...
    def mark_as_retry(self, task_id: Any, exc: Any, traceback: Optional[Any] = ..., request: Optional[Any] = ..., store_result: bool = ..., state: Any = ...): ...
    def chord_error_from_stack(self, callback: Any, exc: Optional[Any] = ...): ...
    def fail_from_current_stack(self, task_id: Any, exc: Optional[Any] = ...): ...
    def prepare_exception(self, exc: Any, serializer: Optional[Any] = ...): ...
    def exception_to_python(self, exc: Any): ...
    def prepare_value(self, result: Any): ...
    def encode(self, data: Any): ...
    def meta_from_decoded(self, meta: Any): ...
    def decode_result(self, payload: Any): ...
    def decode(self, payload: Any): ...
    def prepare_expires(self, value: Any, type: Optional[Any] = ...): ...
    def prepare_persistent(self, enabled: Optional[Any] = ...): ...
    def encode_result(self, result: Any, state: Any): ...
    def is_cached(self, task_id: Any): ...
    def store_result(self, task_id: Any, result: Any, state: Any, traceback: Optional[Any] = ..., request: Optional[Any] = ..., **kwargs: Any): ...
    def forget(self, task_id: Any) -> None: ...
    def get_state(self, task_id: Any): ...
    get_status: Any = ...
    def get_traceback(self, task_id: Any): ...
    def get_result(self, task_id: Any): ...
    def get_children(self, task_id: Any): ...
    def get_task_meta(self, task_id: Any, cache: bool = ...): ...
    def reload_task_result(self, task_id: Any) -> None: ...
    def reload_group_result(self, group_id: Any) -> None: ...
    def get_group_meta(self, group_id: Any, cache: bool = ...): ...
    def restore_group(self, group_id: Any, cache: bool = ...): ...
    def save_group(self, group_id: Any, result: Any): ...
    def delete_group(self, group_id: Any): ...
    def cleanup(self) -> None: ...
    def process_cleanup(self) -> None: ...
    def on_task_call(self, producer: Any, task_id: Any): ...
    def add_to_chord(self, chord_id: Any, result: Any) -> None: ...
    def on_chord_part_return(self, request: Any, state: Any, result: Any, **kwargs: Any) -> None: ...
    def fallback_chord_unlock(self, header_result: Any, body: Any, countdown: int = ..., **kwargs: Any) -> None: ...
    def ensure_chords_allowed(self) -> None: ...
    def apply_chord(self, header_result: Any, body: Any, **kwargs: Any) -> None: ...
    def current_task_children(self, request: Optional[Any] = ...): ...
    def __reduce__(self, args: Any = ..., kwargs: Optional[Any] = ...): ...

class SyncBackendMixin:
    def iter_native(self, result: Any, timeout: Optional[Any] = ..., interval: float = ..., no_ack: bool = ..., on_message: Optional[Any] = ..., on_interval: Optional[Any] = ...) -> None: ...
    def wait_for_pending(self, result: Any, timeout: Optional[Any] = ..., interval: float = ..., no_ack: bool = ..., on_message: Optional[Any] = ..., on_interval: Optional[Any] = ..., callback: Optional[Any] = ..., propagate: bool = ...): ...
    def wait_for(self, task_id: Any, timeout: Optional[Any] = ..., interval: float = ..., no_ack: bool = ..., on_interval: Optional[Any] = ...): ...
    def add_pending_result(self, result: Any, weak: bool = ...): ...
    def remove_pending_result(self, result: Any): ...
    @property
    def is_async(self): ...

class BaseBackend(Backend, SyncBackendMixin): ...
BaseDictBackend = BaseBackend

class BaseKeyValueStoreBackend(Backend):
    key_t: Any = ...
    task_keyprefix: str = ...
    group_keyprefix: str = ...
    chord_keyprefix: str = ...
    implements_incr: bool = ...
    apply_chord: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get(self, key: Any) -> None: ...
    def mget(self, keys: Any) -> None: ...
    def set(self, key: Any, value: Any) -> None: ...
    def delete(self, key: Any) -> None: ...
    def incr(self, key: Any) -> None: ...
    def expire(self, key: Any, value: Any) -> None: ...
    def get_key_for_task(self, task_id: Any, key: str = ...): ...
    def get_key_for_group(self, group_id: Any, key: str = ...): ...
    def get_key_for_chord(self, group_id: Any, key: str = ...): ...
    def get_many(self, task_ids: Any, timeout: Optional[Any] = ..., interval: float = ..., no_ack: bool = ..., on_message: Optional[Any] = ..., on_interval: Optional[Any] = ..., max_iterations: Optional[Any] = ..., READY_STATES: Any = ...) -> None: ...
    def on_chord_part_return(self, request: Any, state: Any, result: Any, **kwargs: Any): ...

class KeyValueStoreBackend(BaseKeyValueStoreBackend, SyncBackendMixin): ...

class DisabledBackend(BaseBackend):
    def store_result(self, *args: Any, **kwargs: Any) -> None: ...
    def ensure_chords_allowed(self) -> None: ...
    def as_uri(self, *args: Any, **kwargs: Any): ...
    get_state: Any = ...
    get_status: Any = ...
    get_result: Any = ...
    get_traceback: Any = ...
    get_task_meta_for: Any = ...
    wait_for: Any = ...
    get_many: Any = ...