from typing import Any, Optional

class SecureSerializer:
    def __init__(self, key: Optional[Any] = ..., cert: Optional[Any] = ..., cert_store: Optional[Any] = ..., digest: Any = ..., serializer: str = ...) -> None: ...
    def serialize(self, data: Any): ...
    def deserialize(self, data: Any): ...

def register_auth(key: Optional[Any] = ..., cert: Optional[Any] = ..., store: Optional[Any] = ..., digest: Any = ..., serializer: str = ...) -> None: ...
