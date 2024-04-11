from typing import Optional, Tuple, Union

from _pytest.main import Session
from _pytest.nodes import Item
from _pytest.python import Function
from _pytest.runner import CallInfo


def pytest_runtestloop(session: Session) -> None:
    """
    Perform the main runtest loop (after collection finished).

    The default hook implementation performs the runtest protocol for all items collected in the
    session (session.items), unless the collection failed or the collectonly pytest option is set.

    If at any point pytest.exit() is called, the loop is terminated immediately.
    :param session: The pytest session object.
    :return: None
    """
    pass


def pytest_runtest_protocol(item: Item, nextitem: Optional[Item]) -> None:
    """
    Perform the runtest protocol for a single test item.
    :param item: Test item for which the runtest protocol is performed.
    :param nextitem: The scheduled-to-be-next test item (or None if this is the end my friend).
    :return: None
    Note:
    The default runtest protocol is this (see individual hooks for full details):

    pytest_runtest_logstart(nodeid, location)

    Setup phase:
        call = pytest_runtest_setup(item) (wrapped in CallInfo(when="setup"))
        report = pytest_runtest_makereport(item, call)
        pytest_runtest_logreport(report)
        pytest_exception_interact(call, report) if an interactive exception occurred

    Call phase, if the setup passed and the setuponly pytest option is not set:
        call = pytest_runtest_call(item) (wrapped in CallInfo(when="call"))
        report = pytest_runtest_makereport(item, call)
        pytest_runtest_logreport(report)
        pytest_exception_interact(call, report) if an interactive exception occurred

    Teardown phase:
        call = pytest_runtest_teardown(item, nextitem) (wrapped in CallInfo(when="teardown"))
        report = pytest_runtest_makereport(item, call)
        pytest_runtest_logreport(report)
        pytest_exception_interact(call, report) if an interactive exception occurred

    pytest_runtest_logfinish(nodeid, location)
    """
    pass


def pytest_runtest_logstart(nodeid: str, location: Tuple[str, int | None, str]) -> None:
    """
    Called at the start of running the runtest protocol for a single item.
    :param nodeid: Full node ID of the item.
    :param location: A tuple of (filename, lineno, testname) where filename is a file path
    relative to config.rootpath and lineno is 0-based.
    :return:
    """
    pass


def pytest_runtest_logfinish(nodeid: str, location: Tuple[str, int | None, str]) -> None:
    """
    Called at the end of running the runtest protocol for a single item.
    :param nodeid: Full node ID of the item.
    :param location: A tuple of (filename, lineno, testname) where filename is a file path relative to
    config.rootpath and lineno is 0-based.
    :return:
    """
    pass


def pytest_runtest_setup(item: Item) -> None:
    """
    Called to perform the setup phase for a test item.
    :param item: The item.
    :return: None
    """
    pass


def pytest_runtest_call(item: Item) -> None:
    """
    Called to run the test for test item (the call phase).
    :param item: The item.
    :return: None
    """
    pass


def pytest_runtest_teardown(item: Item, nextitem: Union[Item | None]) -> None:
    """
    Called to perform the teardown phase for a test item.
    :param item: The item.
    :param nextitem: The scheduled-to-be-next test item.
    :return: None
    """
    pass


def pytest_runtest_makereport(item: Item, call: CallInfo[None]) -> None:
    """
    Called to create a TestReport for each of the setup, call and teardown runtest phases of a test item.
    :param item: The item.
    :param call: The CallInfo for the phase.
    :return: None
    """
    pass


def pytest_pyfunc_call(pyfuncitem: Function) -> None:
    """
     Call underlying test function.
    :param pyfuncitem: The function item.
    :return:
    """
    print("Function: ", pyfuncitem)
