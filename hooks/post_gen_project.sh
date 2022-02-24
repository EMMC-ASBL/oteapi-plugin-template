#!/usr/bin/env bash
# Post-generate hook script for cookiecutter.
#
# Initialize the generated repository as a `git` repo and create initial commit.
#
# According to the
# [cookiecutter documentation](https://cookiecutter.readthedocs.io/en/latest/advanced/hooks.html#current-working-directory)
# the current working directory for this script is in the generated project folder.

case {{ cookiecutter.use_git }} in
    y | Y | yes | Yes | YES | true | True | TRUE | on | On | ON)
        ;;
    n | N | no | No | NO | false | False | FALSE | off | Off | OFF)
        exit
        ;;
    *)
        echo "Did not recognize use_git='{{ cookiecutter.use_git }}' as True/False."
        echo "Will use the default: True."
        ;;
esac

git init
git add .
git commit --no-gpg-sign --author "SINTEF <Team4.0@SINTEF.no>" -m "Initial commit

Generated {{ cookiecutter.project_name }} using
oteapi-plugin-template: A cookiecutter template developed by SINTEF.
https://github.com/EMMC-ASBL/oteapi-plugin-template
"
git remote add origin {{ cookiecutter.scm_url }}.git
git branch -M main
