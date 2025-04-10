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

git init >> /dev/null
git add . >> /dev/null
git commit --no-gpg-sign --author "SINTEF <Team4.0@SINTEF.no>" -m "Initial commit

Generated {{ cookiecutter.project_name }} using
oteapi-plugin-template: A cookiecutter template developed by SINTEF.
https://github.com/EMMC-ASBL/oteapi-plugin-template
" >> /dev/null
git remote add origin {{ cookiecutter.scm_url }}.git >> /dev/null
git branch -M main >> /dev/null

# Create permanent branch for CI concerning dependency updates through Dependabot.
git branch ci/dependency-updates >> /dev/null

# Information message
echo "Congratulations on creating '{{ cookiecutter.project_name }}' !

For the following commands, it is expected you are in a virtual environment
with at least Python 3.10.

There are still some last things to do to ensure you have a nice CI/CD setup.

(CI: continuous integration)
(CD: continuous deployment)

  1. Push 'main' and 'ci/dependency-updates' branches to the 'origin' remote:

       git push -u origin main:main
       git push -u origin ci/dependency-updates:ci/dependency-updates

  2. Add a 'RELEASE_PAT' secret to GitHub Actions.
     Add a 'CODECOV_TOKEN' secret to GitHub Actions.
     For more information and documentation on this see:

     https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

     https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository

     https://codecov.io

     https://docs.codecov.com/docs/github-tutorial

  3. Setup branch protection rules for 'main' and 'ci/dependency-updates'.
     We recommend to require:

     - Pull requests with at least 1 reviewer approval.
     - Check success for the CI tests:

       - 'External / Run \`pylint\` & \`safety\`'
       - 'External / Build distribution package'
       - 'External / Build Documentation'
       - 'pytest (linux-py3.10)'
       - 'pytest (windows-py3.10)'
       - 'pre-commit.ci - pr'

       Note, we recommend only requiring the pytest jobs for Python 3.10, since it is
       the minimum supported version.

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

  7. Finally, it is VERY IMPORTANT the protection for the 'ci/dependency-updates'
     branch allows force pushes for the user the 'RELEASE_PAT' secret belongs to.
     This can be set to "Everyone" to ensure this if you are unsure.

Please write TEAM4.0@SINTEF.no or create issues on GitHub if there are any issues.

Enjoy !"
