from .base import KeyValueStoreBackend
from typing import Any

class S3Backend(KeyValueStoreBackend):
    endpoint_url: Any = ...
    aws_region: Any = ...
    aws_access_key_id: Any = ...
    aws_secret_access_key: Any = ...
    bucket_name: Any = ...
    base_path: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def get(self, key: Any): ...
    def set(self, key: Any, value: Any) -> None: ...
    def delete(self, key: Any) -> None: ...
