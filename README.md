# Cookie Cutter for a `jupyter-server-proxy` Project

Opinionated `jupyter-server-proxy` cookiecutter project.

Use this cookiecutter to create `jupyter-server-proxy` compatible packages.

## Requirements

- Python 3.6+

## Create your project

1. Setup and activate virtual environment (recommended):

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

2. Install cookiecutter:

```bash
pip install "cookiecutter>=1.7.0"
```

3. Run `cookiecutter` against this repo:

```bash
cookiecutter https://github.com/illumidesk/cookiecutter-jupyter-server-proxy
```

## Development

1. Create and activate virtual environment:

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r dev-requirements.txt
```

> Use `pip-compile` to update development requirements. Update dev-requirements.in and then run `pip-compile dev-requirements.in` to create a new version of `dev-requirements.txt`.

## Credits

Based mostly off of the `jupyter-server-proxy` [template](https://github.com/jupyterhub/jupyter-server-proxy/tree/master/contrib/template) project.

## License

BSD 3-Clause
