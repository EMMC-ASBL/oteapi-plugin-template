"""Pre-generate hook script for cookiecutter.

Validate variables.
"""
import re
import sys

# Ensure package_name is a valid Python module name
MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
MODULE_NAME = "{{ cookiecutter.package_name }}"
if not re.match(MODULE_REGEX, MODULE_NAME):
    sys.exit(f"ERROR: {MODULE_NAME!r} is not a valid Python module name!")


# Ensure package_name starts with `"oteapi_"`
if not MODULE_NAME.startswith("oteapi_"):
    sys.exit(f"ERROR: package_name ({MODULE_NAME!r}) must start with 'oteapi_'.")
