from typing import List, Union

from _pytest.config import Config, PytestPluginManager, ExitCode
from _pytest.config.argparsing import Parser


def pytest_load_initial_conftests(early_config: Config, parser: List[str], args: Parser) -> None:
    """
    Called to implement the loading of initial conftest files ahead of command line option parsing.
    :param early_config: The pytest config object.
    :param parser: Arguments passed on the command line.
    :param args: To add command line options.
    :return: None
    """
    pass


def pytest_cmdline_parse(pluginmanager: PytestPluginManager, args: List[str]) -> Union[Config, None]:
    """
    Return an initialized Config, parsing the specified args.
    This hook is only called for plugin classes passed to the plugins arg when using
    pytest.main to perform an in-process test run.
    :param pluginmanager: The pytest plugin manager.
    :param args: List of arguments passed on the command line.
    :return: Config | None
    """
    pass


def pytest_cmdline_main(config: Config) -> Union[ExitCode, int, None]:
    """
    Called for performing the main command line action.
    The default implementation will invoke the configure hooks and pytest_runtestloop.
    :param config: The pytest config object.
    :return: ExitCode | int | None
    """
    pass
