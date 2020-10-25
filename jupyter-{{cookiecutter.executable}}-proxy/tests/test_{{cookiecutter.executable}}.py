import docker
from docker.errors import ContainerError

import logging

import pytest


LOGGER = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "language,version_output",
    [
        (
            "{{cookiecutter.executable}}",
            [
                "{{cookiecutter.executable}}",
            ],
        ),
    ],
)
def test_{{cookiecutter.executable}}_version(language, version_output):
    """Ensure {{cookiecutter.executable}} is available in the PATH and that it returns the correct version"""
    LOGGER.info(f"Test that language {language} is correctly installed ...")
    client = docker.from_env()
    output = client.containers.run("illumidesk/{{cookiecutter.executable}}:latest", f"{language} --version")
    output_decoded = output.decode("utf-8").split(" ")
    assert output_decoded[0:1].lower() == version_output
    LOGGER.info(f"Output from command: {output_decoded[0:3]}")


def test_invalid_cmd():
    """Ensure that an invalid command returns a docker.errors.ContainerError"""
    with pytest.raises(ContainerError):
        LOGGER.info("Test an invalid command ...")
        client = docker.from_env()
        client.containers.run("illumidesk/{{cookiecutter.executable}}", "foo --version")
