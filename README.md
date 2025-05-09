# OTEAPI Plugin Cookiecutter Template

[![DOI](https://zenodo.org/badge/447298593.svg)](https://zenodo.org/badge/latestdoi/447298593)

<!-- markdownlint-disable MD033 -->

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating an OTEAPI Plugin repository.

## What you get

The template contains pre-configured features for:

- Documentation via a [MkDocs](https://www.mkdocs.org/) setup.
- MIT License.
- [Pre-commit](https://pre-commit.com/) configuration with several useful hooks.
- Python unit tests through [pytest](https://docs.pytest.org/).
- Plugin integration tests for [OTEAPI Core](https://github.com/EMMC-ASBL/oteapi-core).
- [pip](https://pip.pypa.io/) installable package.

Furthermore, the repository will contain **dummy/demo** strategies for each of the currently available OTE strategy types:

- Download (`scheme`)
- Filter (`filterType`)
- Mapping (`mappingType`)
- Parse (`mediaType`)
- Resource (`accessService`)
- Transformation (`transformationType`)

These should be **updated** to **your specific needs** according to the strategy or strategies you intend to implement.
The ones that are not used should be deleted.

It is **important** to update the [`pyproject.toml`](%7B%7B%20cookiecutter.project_slug%20%7D%7D/pyproject.toml) according to the updated strategies in order for the strategies to be importable through OTEAPI Core.
Please ensure to either uncomment the strategies as they are needed or remove them altogether if they are not needed.

## Usage

To start up a new OTEAPI Plugin repository you need to have the following pre-requisites in your system:

- Access to a command line.
- Have [`git`](https://git-scm.com/) installed.
- Have minimum [Python 3.10](https://www.python.org/) installed.

Also, it might be good to operate within a virtual environment.
For more information about what suits your needs, take a look at [this guide from python.org](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) or [this guide from towardsdatascience.com](https://towardsdatascience.com/virtual-environments-104c62d48c54).

If you are using a virtual environment, it is understood that it has already been activated in the following examples.

Install cookiecutter according to [the documentation](https://cookiecutter.readthedocs.io/en/latest/installation.html).

Then run the following to generate a new OTEAPI Plugin repository:

```console
$ cookiecutter gh:EMMC-ASBL/oteapi-plugin-template  # Download from GitHub and generate repo
project_name [OTEAPI My Plugin]:
...
```

Now type in the required inputs to customize your repository.

Alternatively, you can pre-define the inputs in a JSON file and pass it to the `cookiecutter` command using the `--config-file` option.
The list of input keys and default values can be found in [`cookiecutter.json`](cookiecutter.json).  
An overview is also provided in the following table:

| Input key | Description | Default value |
|:---:|:--- |:--- |
| `project_name` | A human-readable name of the project. | `OTEAPI My Plugin` |
| `project_slug` | The official package name to be used when installing the package via a package manager (e.g., `pip` or `conda`).<br>This will be the root directory name and should also be the repository name on an online git repository (like GitHub or GitLab).<br><br>It is recommended to have the project slug start with `oteapi-`.<br><br>**Important**: A project slug value may *not* include white space. | `oteapi-myplugin` |
| `package_name` | The Python importable root module.<br>This will be the root module repository name, under which the source code will be placed.<br><br>It is recommended to have the package name start with `oteapi_`.<br><br>**Important**: A package name value may *not* include white space. A package name value may *only* be made up of the character set: a-z, A-Z, `_`, 0-9, and may *not* start with a number. | `oteapi_myplugin` |
| `author` | The author of the package. This can also be your organization name. | `Firstname Lastname` |
| `organization` | Your organization. | `SINTEF` |
| `email` | The author's email address. | `firstname.lastname@SINTEF.org` |
| `version` | Start version.<br><br>**Important**: Must follow semantic versioning. For more information see [semver.org](https://semver.org). | `0.0.1` |
| `year` | The current year. | `2023` |
| `use_git` | Whether or not the generated repository should be initialized using [`git`](https://git-scm.com). | `True` |
| `username` | A public source code platform username, e.g., for [GitHub](https://github.com), [GitLab](https://gitlab.com), [BitBucket](https://bitbucket.org) | `GitHub_GitLab_BitBucket_etc_Username` |
| `scm_url` | The intended or existing URL to the repository's source code. | `https://github.com/FirstnameLastname/oteapi-myplugin` |

## License and copyright

OTEAPI Plugin Cookiecutter Template is released under the [MIT license](LICENSE) with copyright &copy; SINTEF.

## Acknowledgment

OTEAPI Plugin Cookiecutter Template has been supported by the following projects:

- **OntoTrans** (2020-2024) that receives funding from the European Union’s Horizon 2020 Research and Innovation Programme, under Grant Agreement n. 862136.

- **VIPCOAT** (2021-2025) receives funding from the European Union’s Horizon 2020 Research and Innovation Programme - DT-NMBP-11-2020 Open Innovation Platform for Materials Modelling, under Grant Agreement no: 952903.

- **OpenModel** (2021-2025) receives funding from the European Union’s Horizon 2020 Research and Innovation Programme - DT-NMBP-11-2020 Open Innovation Platform for Materials Modelling, under Grant Agreement no: 953167.
