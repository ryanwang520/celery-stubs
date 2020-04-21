from typing import Any

NONE_PRECEDENCE = PRECEDENCE_LOOKUP[None]

def precedence(state: Any): ...

class state(str):
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...

PENDING: str
RECEIVED: str
STARTED: str
SUCCESS: str
FAILURE: str
REVOKED: str
RETRY: str
IGNORED: str
READY_STATES: Any
UNREADY_STATES: Any
EXCEPTION_STATES: Any
PROPAGATE_STATES: Any
