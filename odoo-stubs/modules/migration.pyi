from typing import Any

_logger: Any

def load_script(path: Any, module_name: Any): ...

class MigrationManager:
    cr: Any = ...
    graph: Any = ...
    migrations: Any = ...
    def __init__(self, cr: Any, graph: Any) -> None: ...
    def _get_files(self): ...
    def migrate_module(self, pkg: Any, stage: Any): ...