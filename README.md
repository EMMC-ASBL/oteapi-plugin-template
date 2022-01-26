# OTE-API Plugin Cookiecutter Template

A [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating an OTE-API Plugin repository.

## What you get

The template contains pre-configured features for:

- Documentation via a [MkDocs](https://www.mkdocs.org/) setup.
- MIT License.
- [Pre-commit](https://pre-commit.com/) configuration with several useful hooks.
- Python unit tests through [pytest](https://docs.pytest.org/).
- Plugin integration tests for [OTE-API Core](https://github.com/EMMC-ASBL/oteapi-core).
- [pip](https://pip.pypa.io/) installable package.

Furthermore, the repository will contain **dummy/demo** strategies for each of the currently available OTE strategy types:

- Download (`scheme`)
- Filter (`filterType`)
- Mapping (`mappingType`)
- Parse (`mediaType`)
- Resource (`accessService`)
- Transformation (`transformation_type`)

These should be **updated** to **your specific needs** according to the strategy or strategies you intend to implement.
The ones that are not used should be deleted.

It is **important** to update the [`setup.cfg`]({{ cookiecutter.project_slug }}/setup.cfg) according to the updated strategies in order for the strategies to be importable through OTE-API Core.

## License and copyright

OTE-API Plugin Cookiecutter Template is released under the [MIT license](LICENSE) with copyright &copy; SINTEF.

## Acknowledgment

OTE-API Plugin Cookiecutter Template has been supported by the following projects:

- __OntoTrans__ (2020-2024) that receives funding from the European Union’s Horizon 2020 Research and Innovation Programme, under Grant Agreement n. 862136.
