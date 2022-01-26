"""Pre-generate hook script for cookiecutter.

Validate variables.
"""
import re
import sys

# Ensure package_name is a valid Python module name
MODULE_REGEX = re.compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")
MODULE_NAME = "{{ cookiecutter.package_name }}"
if not MODULE_REGEX.match(MODULE_NAME):
    sys.exit(f"ERROR: {MODULE_NAME!r} is not a valid Python module name!")


# Ensure package_name starts with `"oteapi_"`
if not MODULE_NAME.startswith("oteapi_"):
    sys.exit(f"ERROR: package_name ({MODULE_NAME!r}) must start with 'oteapi_'.")


# Ensure there is no white space in `project_slug` or `package_name`
ERROR_MSG = "ERROR: {input_key} may not contain white space."
PROJECT_NAME = "{{ cookiecutter.project_slug }}"
if re.match(r"\s", MODULE_NAME):
    sys.exit(ERROR_MSG.format(input_key="package_name"))
if re.match(r"\s", PROJECT_NAME):
    sys.exit(ERROR_MSG.format(input_key="project_slug"))
