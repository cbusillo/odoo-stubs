from typing import Any, Callable

from ..fields import Field
from ..models import BaseModel, MAGIC_COLUMNS as MAGIC_COLUMNS
from ..sql_db import Cursor
from ..tools.query import Query

_Domain = list

NOT_OPERATOR: str
OR_OPERATOR: str
AND_OPERATOR: str
DOMAIN_OPERATORS: tuple[str, ...]
TERM_OPERATORS: tuple[str, ...]
NEGATIVE_TERM_OPERATORS: tuple[str, ...]
DOMAIN_OPERATORS_NEGATION: dict[str, str]
TERM_OPERATORS_NEGATION: dict[str, str]
TRUE_LEAF: tuple
FALSE_LEAF: tuple
TRUE_DOMAIN: list[tuple]
FALSE_DOMAIN: list[tuple]

def normalize_domain(domain: _Domain) -> _Domain: ...
def is_false(model, domain: _Domain) -> bool: ...
def combine(operator: str, unit, zero, domains: list[_Domain]) -> _Domain: ...
def AND(domains: list[_Domain]) -> _Domain: ...
def OR(domains: list[_Domain]) -> _Domain: ...
def distribute_not(domain: _Domain) -> _Domain: ...
def _quote(to_quote: str) -> str: ...
def normalize_leaf(element): ...
def is_operator(element) -> bool: ...
def is_leaf(element, internal: bool = ...) -> bool: ...
def is_boolean(element) -> bool: ...
def check_leaf(element, internal: bool = ...) -> None: ...
def _unaccent_wrapper(x) -> str: ...
def get_unaccent_wrapper(cr: Cursor) -> Callable[[Any], str]: ...

class expression:
    _unaccent_wrapper: Callable[[Any], str]
    _has_trigram: bool
    root_model: BaseModel
    root_alias: str | None
    expression: _Domain
    query: Query | None
    result: tuple[str, list]
    def __init__(self, domain: _Domain, model: BaseModel, alias: str | None = ..., query: Query | None = ...) -> None: ...
    def _unaccent(self, field: Field) -> Callable[[Any], str]: ...
    def get_tables(self) -> tuple[str, ...]: ...
    def parse(self): ...
    def __leaf_to_sql(self, leaf, model: BaseModel, alias: str) -> tuple[str, list]: ...
    def to_sql(self) -> tuple[str, list]: ...
