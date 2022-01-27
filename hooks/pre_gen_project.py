"""Pre-generate hook script for cookiecutter.

Validate variables.
"""
import re
import subprocess  # nosec
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Sequence, Union


def run_cmd(cmd: "Union[str, Sequence[str]]") -> subprocess.CompletedProcess:
    """Run a command via `subprocess.run()`.

    Parameters:
        cmd: The command to run as a subprocess. If this is a string, it will be
            converted to a list via the `split()`-method.

    Returns:
        The complete process object from the `subprocess` run.

    """
    cmd = cmd.split() if isinstance(cmd, str) else list(cmd)
    try:
        result_run = subprocess.run(cmd, check=True, capture_output=True)  # nosec
    except subprocess.CalledProcessError as exc:
        sys.exit(
            f"ERROR: Running cmd {cmd!r} in generated project dir "
            f"{Path.cwd().resolve()} failed.\n\nException: {exc}"
        )
    return result_run


# Ensure package_name is a valid Python module name
MODULE_REGEX = re.compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")
MODULE_NAME = "{{ cookiecutter.package_name }}"
if not MODULE_REGEX.match(MODULE_NAME):
    sys.exit(f"ERROR: {MODULE_NAME!r} is not a valid Python module name!")


# Warn if package_name does not start with `"oteapi_"`
PROJECT_NAME = "{{ cookiecutter.project_slug }}"
if not MODULE_NAME.startswith("oteapi_"):
    print(f"WARNING: package_name ({MODULE_NAME!r}) does not start with 'oteapi_' !")
if not PROJECT_NAME.startswith("oteapi-"):
    print(f"WARNING: project_slug ({PROJECT_NAME!r}) does not start with 'oteapi-' !")


# Ensure there is no white space in `project_slug` or `package_name`
ERROR_MSG = "ERROR: {input_key} may not contain white space."
if re.match(r"\s", MODULE_NAME):
    sys.exit(ERROR_MSG.format(input_key="package_name"))
if re.match(r"\s", PROJECT_NAME):
    sys.exit(ERROR_MSG.format(input_key="project_slug"))

# Ensure git has already been configured
result = run_cmd("git config --list")
if result.stdout:
    git_config: "List[str]" = result.stdout.decode("utf8").splitlines()
    VALID = 0
    for config in git_config:
        if re.match(r"^user\.(email|name)=.+$", config):
            VALID += 1
    if VALID != 2:
        sys.exit(
            "ERROR: git has not been configured.\nPlease set user information by "
            "running for example:\n\n  git config --global user.email "
            '"{{ cookiecutter.email }}"\n  git config --global user.name '
            '"{{ cookiecutter.author }}"\n'
        )
