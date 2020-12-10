from celery._state import current_app as current_app, current_task as current_task
from celery.app import shared_task as shared_task
from celery.app.base import Celery as Celery
from celery.app.utils import bugreport as bugreport
from celery.app.task import Task as Task
from celery.canvas import chain as chain, chord as chord, chunks as chunks, group as group, maybe_signature as maybe_signature, signature as signature, xmap as xmap, xstarmap as xstarmap
from celery.utils import uuid as uuid
from collections import namedtuple

version_info_t = namedtuple('version_info_t', ['major', 'minor', 'micro', 'releaselevel', 'serial'])

# Names in __all__ with no definition:
#   task
