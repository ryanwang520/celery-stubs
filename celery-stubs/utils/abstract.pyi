import abc
from abc import abstractmethod
from collections import Callable
from typing import Any, Optional

class _AbstractClass:
    __required_attributes__: Any = ...
    @classmethod
    def register(cls, other: Any): ...

class CallableTask(_AbstractClass, Callable, metaclass=abc.ABCMeta):
    __required_attributes__: Any = ...
    @abstractmethod
    def delay(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def apply_async(self, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    def apply(self, *args: Any, **kwargs: Any) -> Any: ...
    @classmethod
    def __subclasshook__(cls, C: Any): ...

class CallableSignature(CallableTask, metaclass=abc.ABCMeta):
    __required_attributes__: Any = ...
    @property
    @abc.abstractmethod
    def name(self) -> Any: ...
    @property
    @abc.abstractmethod
    def type(self) -> Any: ...
    @property
    @abc.abstractmethod
    def app(self) -> Any: ...
    @property
    @abc.abstractmethod
    def id(self) -> Any: ...
    @property
    @abc.abstractmethod
    def task(self) -> Any: ...
    @property
    @abc.abstractmethod
    def args(self) -> Any: ...
    @property
    @abc.abstractmethod
    def kwargs(self) -> Any: ...
    @property
    @abc.abstractmethod
    def options(self) -> Any: ...
    @property
    @abc.abstractmethod
    def subtask_type(self) -> Any: ...
    @property
    @abc.abstractmethod
    def chord_size(self) -> Any: ...
    @property
    @abc.abstractmethod
    def immutable(self) -> Any: ...
    @abstractmethod
    def clone(self, args: Optional[Any] = ..., kwargs: Optional[Any] = ...) -> Any: ...
    @abstractmethod
    def freeze(self, id: Optional[Any] = ..., group_id: Optional[Any] = ..., chord: Optional[Any] = ..., root_id: Optional[Any] = ...) -> Any: ...
    @abstractmethod
    def set(self, immutable: Optional[Any] = ..., **options: Any) -> Any: ...
    @abstractmethod
    def link(self, callback: Any) -> Any: ...
    @abstractmethod
    def link_error(self, errback: Any) -> Any: ...
    @abstractmethod
    def __or__(self, other: Any) -> Any: ...
    @abstractmethod
    def __invert__(self) -> Any: ...
    @classmethod
    def __subclasshook__(cls, C: Any): ...
