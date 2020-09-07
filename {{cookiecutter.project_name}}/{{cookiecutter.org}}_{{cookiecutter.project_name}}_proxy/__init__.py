import os
import shutil
import logging


logger = logging.getLogger(__name__)
logger.setLevel('INFO')


def setup_{{cookiecutter.executable}}():
    # Make sure theia is in $PATH
    def {{cookiecutter.executable}}_command(port):
        executable = shutil.which('{{cookiecutter.executable}}')
        if not executable:
            raise FileNotFoundError('Can not find {{cookiecutter.executable}} executable in $PATH')
        # Create theia working directory
        home_dir = os.environ.get('HOME') or '/home/jovyan'
        working_dir = f'{home_dir}/{{cookiecutter.executable}}'
        if not os.path.exists(working_dir):
            os.makedirs(working_dir)
            logger.info("Created directory %s" % working_dir)
        else:    
            logger.info("Directory %s already exists" % working_dir)
        return ['{{cookiecutter.executable}}', '{{cookiecutter.extra_args}}']
    
    return {
        'command': '{{cookiecutter.executable}}_command',
        'launcher_entry': {
            'title': '{{cookiecutter.project_name}}',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', '{{cookiecutter.executable}}.svg')
        },
    }
