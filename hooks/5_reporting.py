from pathlib import Path
from typing import Sequence, Union, Tuple, Mapping

from _pytest.config import Config
from _pytest.fixtures import SubRequest
from _pytest.nodes import Collector, Item
from _pytest.reports import CollectReport, TestReport
from _pytest.terminal import TestShortLogReport


def pytest_collectstart(collector: Collector) -> None:
    """
    Collector starts collecting.
    :param collector: The collector.
    :return: None
    """
    print("Collector: ", collector.name)


def pytest_make_collect_report(collector) -> None:
    """
    Perform collector.collect() and return a CollectReport.
    :param collector: The collector.
    :return: None
    """
    pass


def pytest_itemcollected(item: Item) -> None:
    """
    We just collected a test item.
    :param item: The item.
    :return: None
    """
    pass


def pytest_collectreport(report: CollectReport) -> None:
    """
    Collector finished collecting.
    :param report: The collect report.
    :return:
    """
    pass


def pytest_deselected(items: Sequence[Item]) -> None:
    """
    Called for deselected test items, e.g. by keyword.
    May be called multiple times.
    :param items: The items.
    :return:
    """
    pass


def pytest_report_header(config: Config, start_path: Path, startdir) -> None:
    """
    Return a string or list of strings to be displayed as header info for terminal reporting.
    :param config: The pytest config object.
    :param start_path: The starting dir.
    :param startdir: The starting dir (deprecated).
    :return: None
    """
    pass


def pytest_report_collectionfinish(config: Config, start_path: Path, startdir, items: Sequence[Item]) -> None:
    """

    :param config: The pytest config object.
    :param start_path: The starting dir.
    :param startdir: The starting dir (deprecated).
    :param items: ist of pytest items that are going to be executed; this list should not be modified.
    :return:
    """
    pass


def pytest_report_teststatus(report: Union[CollectReport | TestReport], config: Config) -> None:
    """
    Return result-category, short letter and verbose word for status reporting.

    The result-category is a category in which to count the result, for example “passed”, “skipped”, “error” or
    the empty string.

    The short letter is shown as testing progresses, for example “.”, “s”, “E” or the empty string.

    The verbose word is shown as testing progresses in verbose mode, for example “PASSED”,
    “SKIPPED”, “ERROR” or the empty string.

    pytest may style these implicitly according to the report outcome.
    To provide explicit styling, return a tuple for the verbose word, for example
    "rerun", "R", ("RERUN", {"yellow": True}).
    :param report: The report object whose status is to be returned.
    :param config: The pytest config object.
    :return: TestShortLogReport | Tuple[str, str, Union[str, Tuple[str, Mapping[str, bool]]]]
    """
    print("Status: ", report.when)


def pytest_fixture_setup(fixturedef, request: SubRequest) -> Union[object, None]:
    """
    Perform fixture setup execution.
    :param fixturedef: The fixture definition object.
    :param request: The fixture request object.
    :return: object | None
    """
    pass


def pytest_fixture_post_finalizer(fixturedef, request: SubRequest) -> None:
    """
    Called after fixture teardown, but before the cache is cleared,
    so the fixture result fixturedef.cached_result is still available (not None).
    :param fixturedef: The fixture definition object.
    :param request: The fixture request object.
    :return:
    """
    pass
