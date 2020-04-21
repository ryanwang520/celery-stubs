from typing import Any

def str_to_list(s: str) -> List[str]: ...
def dedent_initial(s: str, n: int=...) -> str: ...
def dedent(s: str, n: int=..., sep: str=...) -> str: ...
def fill_paragraphs(s: str, width: int, sep: str=...) -> str: ...
def join(l: str, sep: str=...) -> str: ...
def ensure_sep(sep: str, s: str, n: int=...) -> str: ...

ensure_newlines: Any

def abbr(S: str, max: int, ellipsis: str=...) -> str: ...
def abbrtask(S: str, max: int) -> str: ...
def indent(t: str, indent: int=..., sep: str=...) -> str: ...
def truncate(s: str, maxlen: int=..., suffix: str=...) -> str: ...
def pluralize(n: int, text: str, suffix: str=...) -> str: ...
def pretty(value: str, width: int=..., nl_width: int=..., sep: str=..., **kw: Any) -> str: ...
def simple_format(s: str, keys: Mapping[str, str], pattern: Pattern=..., expand: str=...) -> str: ...
