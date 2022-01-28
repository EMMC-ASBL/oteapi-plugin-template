#!/usr/bin/env bash
# Post-generate hook script for cookiecutter.
#
# Initialize the generated repository as a `git` repo and create initial commit.
#
# According to the
# [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#current-working-directory)
# the current working directory for this script is in the generated project folder.

git init
git add .
git commit --no-gpg-sign --author "SINTEF <Team4.0@SINTEF.no>" -m "Initial commit

Generated {{ cookiecutter.project_name }} using
oteapi-plugin-template: A cookiecutter template developed by SINTEF.
https://github.com/EMMC-ASBL/oteapi-plugin-template
"
git remote add origin {{ cookiecutter.git_url }}.git
git branch -M main
