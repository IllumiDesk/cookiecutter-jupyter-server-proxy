import setuptools
from os import path


# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name="{{cookiecutter.org}}-{{cookiecutter.project_name}}-proxy",
    version='{{cookiecutter.version}}',
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.org}}-{{cookiecutter.project_name}}-proxy",
    author="{{cookiecutter.author_name}}",
    description="{{cookiecutter.author_email}}",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
	keywords=['jupyter', '{{cookiecutter.project_name}}', 'jupyterhub'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            '{{cookiecutter.project_name}} = {{cookiecutter.org}}_{{cookiecutter.project_name}}_proxy:setup_{{cookiecutter.project_name}}',
        ]
    },
    package_data={
        '{{cookiecutter.org}}_{{cookiecutter.project_name}}_proxy': ['icons/{{cookiecutter.project_name}}.svg'],
    },
)
