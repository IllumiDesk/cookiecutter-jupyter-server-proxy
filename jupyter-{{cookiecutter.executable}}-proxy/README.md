# jupyter-{{cookiecutter.executable}}-proxy

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{{cookiecutter.github_username}}/jupyter-{{cookiecutter.executable}}-proxy/main?urlpath={{cookiecutter.executable}})

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `{{cookiecutter.executable}}` command. This command assumes the `{{cookiecutter.executable}}` command is available in the environment's `PATH`.


### Install jupyter-{{cookiecutter.executable}}-proxy

1. Install the package with pip:

```bash
pip install git+https://github.com/{{cookiecutter.github_username}}/jupyter-{{cookiecutter.executable}}-proxy.git
```

2. (Optional) Replace icon in `icons` folder

3. Install and enable extension for Jupyter Classic and Jupyter Lab:

```bash
jupyter serverextension enable --sys-prefix --py jupyter_server_proxy \
 && jupyter labextension install @jupyterlab/server-proxy@^2.1.1 \
 && jupyter lab build -y \
 && jupyter lab clean -y
```

## Notes

- If you would like to use a docker container, you may use any of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) images.
- You may also run this package with `binder`.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
