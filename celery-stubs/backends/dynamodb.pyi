from .base import KeyValueStoreBackend
from collections import namedtuple
from typing import Any, Optional

DynamoDBAttribute = namedtuple('DynamoDBAttribute', ['name', 'data_type'])

class DynamoDBBackend(KeyValueStoreBackend):
    table_name: str = ...
    read_capacity_units: int = ...
    write_capacity_units: int = ...
    aws_region: Any = ...
    endpoint_url: Any = ...
    time_to_live_seconds: Any = ...
    supports_autoexpire: bool = ...
    url: Any = ...
    def __init__(self, url: Optional[Any] = ..., table_name: Optional[Any] = ..., *args: Any, **kwargs: Any) -> None: ...
    @property
    def client(self): ...
    def get(self, key: Any): ...
    def set(self, key: Any, value: Any) -> None: ...
    def mget(self, keys: Any): ...
    def delete(self, key: Any) -> None: ...
