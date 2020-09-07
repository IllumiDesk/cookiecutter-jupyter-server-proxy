# IllumiDesk {{cookiecutter.project_name}}

This package was built using the [`illumidesk-server-proxy` cookiecutter template](https://github.com/illumidesk/illumidesk-server-proxy).

## Requirements

- Python 3.6+
- Jupyter Notebook 6.0+
- JupyterLab 2.1+

This package executes the standard `{{cookiecutter.executable_name}}` command. This command assumes the `{{cookiecutter.executable_name}}` command is available in the environment's `PATH`.

### Install illumidesk-{{cookiecutter.executable_name}}-proxy

Install the package with pip:

```
pip install illumidesk-{{cookiecutter.executable_name}}-proxy
```

## Notes

- If you would like to use a docker container, you may use any of the [Jupyter docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/) images.
- You may also run this package with `binder`.

## Credits

- [`jupyter-server-proxy`](https://github.com/jupyterhub/jupyter-server-proxy)

## License

BSD 3-Clause
