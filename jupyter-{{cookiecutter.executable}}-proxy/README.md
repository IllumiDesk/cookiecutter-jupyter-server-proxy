# jupyter-{{cookiecutter.executable}}-proxy

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{{cookiecutter.github_username}}/jupyter-{{cookiecutter.executable}}-proxy/main?urlpath={{cookiecutter.executable}})

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `{{cookiecutter.executable}}` command. This command assumes the `{{cookiecutter.executable}}` command is available in the environment's `PATH`.

## Quick Starts

### Launch with `binder`

This test requires you to have a database instance available as a public endpoint or installed within the notebook container itself.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/illumidesk/jupyter-{{cookiecutter.executable}}-proxy/main?urlpath={{cookiecutter.executable}})

## The Hard Way

### Create and Activate Environment

```bash
virtualenv -p python3 venv
source venv/bin/activate
```

### Install jupyter-{{cookiecutter.executable}}-proxy

```bash
pip install git+https://github.com/{{cookiecutter.}}/jupyter-{{cookiecutter.executable}}-proxy.git
```

### Enable jupyter-{{cookiecutter.executable}}-proxy Extensions

1. For Jupyter Classic, activate the `jupyter-server-proxy` extension:

```bash
jupyter serverextension enable --sys-prefix jupyter_server_proxy
```

2. For Jupyter Lab, install the `@jupyterlab/server-proxy` extension:

```bash
jupyter labextension install @jupyterlab/server-proxy
jupyter lab build
```

3. Start Jupyter Classic or Jupyter Lab

4. Click on the `{{cookiecutter.executable}}` icon from the Jupyter Lab Launcher or the `{{cookiecutter.executable}}` item from the `New` dropdown in Jupyter Classic.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause



## Install jupyter-{{cookiecutter.executable}}-proxy

Install the package directly from the git repo or install in editable mode.

1. Clone and install the package from the git repo:

```
git clone https://github.com/{{cookiecutter.github_username}}/jupyter-{{cookiecutter.executable}}-proxy.git
```

2. Install the package in editable mode with pip:

```
pip install -e .
```

## Notes

- If you would like to use a docker container, you may use any of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) images.
- You may also run this package with `binder`.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
