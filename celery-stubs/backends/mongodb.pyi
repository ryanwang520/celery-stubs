from .base import BaseBackend
from typing import Any, Optional

class InvalidDocument(Exception): ...

class MongoBackend(BaseBackend):
    mongo_host: Any = ...
    host: str = ...
    port: int = ...
    user: Any = ...
    password: Any = ...
    database_name: str = ...
    taskmeta_collection: str = ...
    groupmeta_collection: str = ...
    max_pool_size: int = ...
    options: Any = ...
    supports_autoexpire: bool = ...
    url: Any = ...
    def __init__(self, app: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def encode(self, data: Any): ...
    def decode(self, data: Any): ...
    def cleanup(self) -> None: ...
    def __reduce__(self, args: Any = ..., kwargs: Optional[Any] = ...): ...
    def database(self): ...
    def collection(self): ...
    def group_collection(self): ...
    def expires_delta(self): ...
    def as_uri(self, include_password: bool = ...): ...
