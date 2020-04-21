from optparse import Option as Option
from typing import Any, Optional

input = raw_input

class Error(Exception):
    status: Any = ...
    reason: Any = ...
    def __init__(self, reason: Any, status: Optional[Any] = ...) -> None: ...

class UsageError(Error):
    status: Any = ...

class Extensions:
    names: Any = ...
    namespace: Any = ...
    register: Any = ...
    def __init__(self, namespace: Any, register: Any) -> None: ...
    def add(self, cls: Any, name: Any) -> None: ...
    def load(self): ...

class Command:
    Error: Any = ...
    UsageError: Any = ...
    Parser: Any = ...
    args: str = ...
    version: Any = ...
    supports_args: bool = ...
    option_list: Any = ...
    doc: Any = ...
    respects_app_option: bool = ...
    enable_config_from_cmdline: bool = ...
    namespace: Any = ...
    epilog: Any = ...
    description: str = ...
    leaf: bool = ...
    show_body: bool = ...
    show_reply: bool = ...
    prog_name: str = ...
    args_name: str = ...
    app: Any = ...
    get_app: Any = ...
    stdout: Any = ...
    stderr: Any = ...
    quiet: Any = ...
    def __init__(self, app: Optional[Any] = ..., get_app: Optional[Any] = ..., no_color: bool = ..., stdout: Optional[Any] = ..., stderr: Optional[Any] = ..., quiet: bool = ..., on_error: Optional[Any] = ..., on_usage_error: Optional[Any] = ...) -> None: ...
    def run(self, *args: Any, **options: Any) -> None: ...
    def on_error(self, exc: Any) -> None: ...
    def on_usage_error(self, exc: Any) -> None: ...
    def on_concurrency_setup(self) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def verify_args(self, given: Any, _index: int = ...) -> None: ...
    def execute_from_commandline(self, argv: Optional[Any] = ...): ...
    def run_from_argv(self, prog_name: Any, argv: Optional[Any] = ..., command: Optional[Any] = ...): ...
    def maybe_patch_concurrency(self, argv: Optional[Any] = ...) -> None: ...
    def usage(self, command: Any): ...
    def add_arguments(self, parser: Any) -> None: ...
    def get_options(self): ...
    def add_preload_arguments(self, parser: Any) -> None: ...
    def prepare_arguments(self, parser: Any) -> None: ...
    def expanduser(self, value: Any): ...
    def ask(self, q: Any, choices: Any, default: Optional[Any] = ...): ...
    def handle_argv(self, prog_name: Any, argv: Any, command: Optional[Any] = ...): ...
    def prepare_args(self, options: Any, args: Any): ...
    def check_args(self, args: Any) -> None: ...
    def error(self, s: Any) -> None: ...
    def out(self, s: Any, fh: Optional[Any] = ...) -> None: ...
    def die(self, msg: Any, status: Any = ...) -> None: ...
    def early_version(self, argv: Any) -> None: ...
    parser: Any = ...
    def parse_options(self, prog_name: Any, arguments: Any, command: Optional[Any] = ...): ...
    def create_parser(self, prog_name: Any, command: Optional[Any] = ...): ...
    def add_compat_options(self, parser: Any, options: Any) -> None: ...
    def prepare_parser(self, parser: Any): ...
    def setup_app_from_commandline(self, argv: Any): ...
    def find_app(self, app: Any): ...
    def symbol_by_name(self, name: Any, imp: Any = ...): ...
    get_cls_by_name: Any = ...
    def process_cmdline_config(self, argv: Any): ...
    def parse_preload_options(self, args: Any): ...
    def add_append_opt(self, acc: Any, opt: Any, value: Any) -> None: ...
    def parse_doc(self, doc: Any): ...
    def with_pool_option(self, argv: Any) -> None: ...
    def node_format(self, s: Any, nodename: Any, **extra: Any): ...
    def host_format(self, s: Any, **extra: Any): ...
    def pretty_list(self, n: Any): ...
    def pretty_dict_ok_error(self, n: Any): ...
    def say_remote_command_reply(self, replies: Any) -> None: ...
    def pretty(self, n: Any): ...
    def say_chat(self, direction: Any, title: Any, body: str = ...) -> None: ...
    @property
    def colored(self): ...
    @colored.setter
    def colored(self, obj: Any) -> None: ...
    @property
    def no_color(self): ...
    @no_color.setter
    def no_color(self, value: Any) -> None: ...

def daemon_options(parser: Any, default_pidfile: Optional[Any] = ..., default_logfile: Optional[Any] = ...) -> None: ...
