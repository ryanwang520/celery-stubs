from celery import worker as worker
from celery.result import allow_join_result as allow_join_result
from celery.utils.dispatch import Signal as Signal
from celery.utils.nodenames import anon_nodename as anon_nodename
from typing import Any, Optional

WORKER_LOGLEVEL: Any
test_worker_starting: Any
test_worker_started: Any
test_worker_stopped: Any

class TestWorkController(worker.WorkController):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def on_consumer_ready(self, consumer: celery.worker.consumer.Consumer) -> None: ...
    def ensure_started(self) -> None: ...

def start_worker(app: Any, concurrency: int = ..., pool: str = ..., loglevel: Any = ..., logfile: Optional[Any] = ..., perform_ping_check: bool = ..., ping_task_timeout: float = ..., **kwargs: Any) -> None: ...
def setup_app_for_worker(app: Celery, loglevel: Union[str, int], logfile: str) -> None: ...
