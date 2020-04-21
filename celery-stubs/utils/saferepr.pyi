from collections import namedtuple
from typing import Any, Optional

_literal = namedtuple('_literal', ['value', 'truncate', 'direction'])

_key = namedtuple('_key', ['value'])

_quoted = namedtuple('_quoted', ['value'])

_dirty = namedtuple('_dirty', ['objid'])

def saferepr(o: Any, maxlen: int=..., maxlevels: int=..., seen: Set=...) -> str: ...
def reprstream(stack: Any, seen: Optional[Any] = ..., maxlevels: int = ..., level: int = ..., isinstance: Any = ...) -> None: ...
