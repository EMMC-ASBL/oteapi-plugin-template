"""Pre-generate hook script for cookiecutter.

Validate variables.
"""
import re
import sys


# Ensure package_name is a valid Python module name
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{ cookiecutter.package_name }}"
if not re.match(MODULE_REGEX, module_name):
    sys.exit(f"ERROR: {module_name!r} is not a valid Python module name!")


# Ensure package_name starts with `"oteapi_"`
if not module_name.startswith("oteapi_"):
    sys.exit(f"ERROR: package_name ({module_name!r}) must start with 'oteapi_'.")
