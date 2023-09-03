import importlib
from types import ModuleType
from typing import Optional


def dynamic_import(module_name: str) -> Optional[ModuleType]:
    """
    Dynamically imports a module using its name.

    :param module_name: The name of the module to import.
    :type module_name: str
    :return: The imported module object if successful, else None.
    :rtype: Optional[ModuleType]
    :raises ImportError: If module cannot be imported
    """
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError:
        print(f"Module '{module_name}' not found. If you wish to make use of this method,"
              + " consider using pip to install the module in question or providing"
              + " your own implementation.")
