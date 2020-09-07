# IllumiDesk {{cookiecutter.project_name}}

This package was built using the [`jupyter-server-proxy` cookiecutter template](https://github.com/illumidesk/cookiecutter-jupyter-server-proxy).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/{{cookiecutter.github_username}}/jupyter-{{cookiecutter.executable}}-proxy/main?urlpath={{cookiecutter.executable}})

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `{{cookiecutter.executable}}` command. This command assumes the `{{cookiecutter.executable}}` command is available in the environment's `PATH`.

<<<<<<< HEAD
### Install illumidesk-{{cookiecutter.executable}}-proxy
=======
### Install illumidesk-{{cookiecutter.executable_name}}-proxy
>>>>>>> 7bd7e09... update readme and vars

Install the package with pip:

```
<<<<<<< HEAD
pip install jupyter-{{cookiecutter.executable}}-proxy
=======
pip install illumidesk-{{cookiecutter.executable}}-proxy
>>>>>>> 7bd7e09... update readme and vars
```

## Notes

- If you would like to use a docker container, you may use any of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) images.
- You may also run this package with `binder`.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
