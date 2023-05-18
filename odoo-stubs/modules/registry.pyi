import threading
from collections import defaultdict, deque
from collections.abc import Mapping
from threading import RLock
from typing import Any, Callable, ClassVar, Collection, Iterable, Iterator

from .graph import Node
from ..models import BaseModel
from ..fields import Field
from ..sql_db import Connection, Cursor
from ..tests.result import OdooTestResult
from ..tools import Collector
from ..tools.lru import LRU

class Registry(Mapping[str, type[BaseModel]]):
    _lock: RLock
    _saved_lock: RLock | None
    registries: ClassVar[LRU]
    def __new__(cls, db_name: str) -> Registry: ...
    @classmethod
    def new(cls, db_name: str, force_demo: bool = ..., status: Any | None = ..., update_module: bool = ...) -> Registry: ...
    models: dict[str, type[BaseModel]]
    _sql_constraints: set
    _init: bool
    _database_translated_fields: Collection[str]
    _assertion_report: OdooTestResult
    _fields_by_model: Any
    _ordinary_tables: set[str] | None
    _constraint_queue: deque
    __cache: LRU
    _init_modules: set[str]
    updated_modules: list[str]
    loaded_xmlids: set
    db_name: str
    _db: Connection
    test_cr: Cursor | None
    test_lock: RLock | None
    loaded: bool
    ready: bool
    field_depends: Collector
    field_depends_context: Collector
    field_inverses: Collector
    _field_trigger_trees: dict[Field, TriggerTree]
    _is_modifying_relations: dict[Field, bool]
    registry_sequence: int | None
    cache_sequence: int | None
    _invalidation_flags: threading.local
    has_unaccent: bool
    has_trigram: bool
    def init(self, db_name: str) -> None: ...
    @classmethod
    def delete(cls, db_name: str) -> None: ...
    @classmethod
    def delete_all(cls) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, model_name: str) -> type[BaseModel]: ...
    def __call__(self, model_name: str) -> type[BaseModel]: ...
    def __setitem__(self, model_name: str, model: type[BaseModel]) -> None: ...
    def __delitem__(self, model_name: str) -> None: ...
    def descendants(self, model_names: Iterable[str], *kinds) -> set[str]: ...
    def load(self, cr: Cursor, module: Node) -> set[str]: ...
    _m2m: defaultdict[Any, list]
    def setup_models(self, cr: Cursor) -> None: ...
    @property
    def field_computed(self) -> dict[Field, list[Field]]: ...
    def get_trigger_tree(self, fields: list, select: Callable = ...) -> TriggerTree: ...
    def get_dependent_fields(self, field: Field) -> Iterator[Field]: ...
    def _discard_fields(self, fields: list[Field]) -> None: ...
    def get_field_trigger_tree(self, field: Field) -> TriggerTree: ...
    @property
    def _field_triggers(self) -> defaultdict[Field, Any]: ...
    def is_modifying_relations(self, field: Field) -> bool: ...
    def post_init(self, func: Callable, *args, **kwargs) -> None: ...
    def post_constraint(self, func: Callable, *args, **kwargs) -> None: ...
    def finalize_constraints(self) -> None: ...
    _post_init_queue: deque
    _foreign_keys: Any
    _is_install: bool
    def init_models(self, cr: Cursor, model_names: Iterable[str], context: dict, install: bool = ...) -> None: ...
    def check_indexes(self, cr: Cursor, model_names: Iterable[str]) -> None: ...
    def add_foreign_key(self, table1, column1, table2, column2, ondelete, model, module, force: bool = ...) -> None: ...
    def check_foreign_keys(self, cr: Cursor) -> None: ...
    def check_tables_exist(self, cr: Cursor) -> None: ...
    def _clear_cache(self) -> None: ...
    def clear_caches(self) -> None: ...
    def is_an_ordinary_table(self, model: BaseModel) -> bool: ...
    @property
    def registry_invalidated(self) -> bool: ...
    @registry_invalidated.setter
    def registry_invalidated(self, value: bool) -> None: ...
    @property
    def cache_invalidated(self) -> bool: ...
    @cache_invalidated.setter
    def cache_invalidated(self, value: bool) -> None: ...
    def setup_signaling(self) -> None: ...
    def check_signaling(self) -> Registry: ...
    def signal_changes(self) -> None: ...
    def reset_changes(self) -> None: ...
    def manage_changes(self) -> None: ...
    def in_test_mode(self) -> bool: ...
    def enter_test_mode(self, cr: Cursor) -> None: ...
    def leave_test_mode(self) -> None: ...
    def cursor(self) -> Cursor: ...

class DummyRLock:
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, traceback) -> None: ...

class TriggerTree(dict):
    __slots__ = ['root']
    root: Any
    def __init__(self, root: Any = ..., *args, **kwargs) -> None: ...
    def __bool__(self) -> bool: ...
    def __repr__(self) -> str: ...
    def increase(self, key) -> TriggerTree: ...
    def depth_first(self) -> Iterator[TriggerTree]: ...
    @classmethod
    def merge(cls, trees: list[TriggerTree], select: Callable = ...) -> TriggerTree: ...
