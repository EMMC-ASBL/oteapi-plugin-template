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
        rm -rf .github
        echo "Congratulations on creating '{{ cookiecutter.project_name }}' !

Please write TEAM4.0@SINTEF.no or create issues on GitHub if there are any issues.

Enjoy !"
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

# Create permanent branch for CI concerning dependency updates through Dependabot.
git checkout -b ci/dependabot-updates
# Go back to `main`
git checkot main

# Information message
echo "Congratulations on creating '{{ cookiecutter.project_name }}' !

For the following commands, it is expected you are in a virtual environment
with at least Python 3.9.

There are still some last things to do to ensure you have a nice CI/CD setup.

(CI: continuous integration)
(CD: continuous deployment)

  1. Push 'main' and 'ci/dependabot-updates' branches to the 'origin' remote:

       git push -u origin main:main
       git push -u origin ci/dependabot-updates:ci/dependabot-updates

  2. Add a 'RELEASE_PAT' secret to GitHub Actions.
     For more information and documentation on this see:

     https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

     https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository

  3. Setup branch protection rules for 'main' and 'ci/dependabot-updates'.
     We recommend to require:

     - Pull requests with at least 1 reviewer approval.
     - Check success for the CI tests:

       - 'pre-commit
       - 'pylint-safety'
       - 'pytest (linux-py3.9)'
       - 'pytest (windows-py3.9)'
       - 'Build distribution package'
       - 'Documentation'

  4. Create a 'CI/CD' label in the GitHub repository.

  5. Start the documentation via GitHub Pages by running:

       # Install the package
       pip install -U pip setuptools wheel
       pip install -U -e .[dev]

       # Build and deploy the documentation to the 'gh-pages' branch on GitHub
       mike deploy --push --config-file mkdocs.yml latest main
       mike set-default --push --config-file mkdocs.yml latest

  6. Uncomment the CI/CD workflows and other code, where necessary,
     when you're ready.

  7. Finally, it is VERY IMPORTANT the protection for the 'ci/dependabot-update'
     branch ONLY allows force pushes for everyone.

Please write TEAM4.0@SINTEF.no or create issues on GitHub if there are any issues.

Enjoy !"
