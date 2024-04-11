from typing import Union

import pytest
from _pytest.config import PytestPluginManager, Config, ExitCode
from _pytest.config.argparsing import Parser
from _pytest.main import Session


def pytest_addoption(parser: Parser, pluginmanager: PytestPluginManager) -> None:
    """
    Register argparse-style options and ini-style config values, called once at the beginning of a test run.
    :param parser: To add command line options, call parser.addoption(...).
                   To add ini-file values call parser.addini(...).
    :param pluginmanager: The pytest plugin manager, which can be used to install hookspec()’s or hookimpl()’s
                          and allow one plugin to call another plugin’s hooks to change how command line options
                          are added.
    :return: None
    Note: Options can later be accessed through the config object, respectively:
        -> config.getoption(name) to retrieve the value of a command line option.
        -> config.getini(name) to retrieve a value read from an ini-style file.
    """
    pass


def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    """
    Called at plugin registration time to allow adding new hooks via a call to
    pluginmanager.add_hookspecs(module_or_class, prefix)
    :param pluginmanager: The pytest plugin manager.
    :return: None
    Note: If a conftest plugin implements this hook, it will be called immediately when the conftest is registered.
    """
    pass


def pytest_configure(config: Config) -> None:
    """
    Allow plugins and conftest files to perform initial configuration.
    :param config: The pytest config object.
    :return: None
    Note: This hook is incompatible with hook wrappers.
    """


def pytest_unconfigure(config: Config) -> None:
    """
    Called before test process is exited.
    :param config: The pytest config object.
    :return:
    """
    pass


@pytest.hookimpl
def pytest_sessionstart(session: Session) -> None:
    """
    Called after the Session object has been created and before performing collection
    and entering the run test loop.
    :param session: The pytest session object.
    :return: None
    """
    print("Test session is starting")


def pytest_sessionfinish(session: Session, exitstatus: Union[ExitCode, int]) -> None:
    """
    Called after whole test run finished, right before returning the exit status to the system.
    :param session: The pytest session object.
    :param exitstatus: The status which pytest will return to the system.
    :return: None
    """
    print("Test session is finished", exitstatus)


def pytest_plugin_registered(plugin, plugin_name: str, manager: PytestPluginManager) -> None:
    """
    A new pytest plugin got registered.
    :param plugin: The plugin module or instance.
    :param plugin_name: The name by which the plugin is registered.
    :param manager: The pytest plugin manager.
    :return: None
    """
    pass
