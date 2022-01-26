# pylint: disable=line-too-long
"""Post-generate hook script for cookiecutter.

Initialize the generated repository as a `git` repo and create initial commit.

According to the
[cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#current-working-directory)
the current working directory for this script is in the generated project folder.
"""
import subprocess  # nosec
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Sequence, Union

PROJECT_DIR = Path.cwd().resolve()


def run_cmd(cmd: "Union[str, Sequence[str]]") -> None:
    """Run a command via `subprocess.run()`."""
    cmd = cmd.split() if isinstance(cmd, str) else list(cmd)
    try:
        subprocess.run(cmd, check=True)  # nosec
    except subprocess.CalledProcessError as exc:
        sys.exit(
            f"ERROR: Running cmd {cmd!r} in generated project dir {PROJECT_DIR} "
            f"failed.\n\nException: {exc}"
        )


for _ in (
    "git init",
    "git add .",
    [
        "git",
        "commit",
        "--author",
        "SINTEF <Team4.0@SINTEF.no>",
        "-m",
        """Initial commit

Generated {{ cookiecutter.project_name }} using
oteapi-plugin-template: A cookiecutter template developed by SINTEF.
https://github.com/EMMC-ASBL/oteapi-plugin-template
""",
    ],
    "git remote add origin {{ cookiecutter.git_url }}.git",
    "git branch -M main",
):
    run_cmd(_)
