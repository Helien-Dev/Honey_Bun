import os
import importlib

# Obtiene la ruta absoluta de este directorio
module_dir = os.path.dirname(__file__)

# Lista de todos los archivos .py excepto __init__.py
__all__ = []

for filename in os.listdir(module_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]  # sin .py
        importlib.import_module(f"{__name__}.{module_name}")
        __all__.append(module_name)