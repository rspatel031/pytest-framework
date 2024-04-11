import random
from pathlib import Path
from typing import Union, List, Dict, Any

from _pytest.config import Config
from _pytest.main import Session
from _pytest.nodes import Item, Collector
from _pytest.python import Module, Class, Metafunc


def pytest_collection(session: Session) -> None:
    """
    Perform the collection phase for the given session.
    :param session: The pytest session object.
    :return: None
    Note:
    The default collection phase is this (see individual hooks for full details):
    1. Starting from session as the initial collector:
        pytest_collectstart(collector)
        report = pytest_make_collect_report(collector)
        pytest_exception_interact(collector, call, report) if an interactive exception occurred
        For each collected node:
            If an item, pytest_itemcollected(item)
            If a collector, recurse into it.
        pytest_collectreport(report)

    2. pytest_collection_modifyitems(session, config, items)
        pytest_deselected(items) for any deselected items (maybe called multiple times)

    3. pytest_collection_finish(session)
    4. Set session.items to the list of collected items
    5. Set session.testscollected to the number of collected items
    """
    pass


def pytest_ignore_collect(collection_path: Path, path, config: Config) -> None:
    """
    Return True to prevent considering this path for collection.
    This hook is consulted for all files and directories prior to calling more specific hooks.
    :param collection_path: The path to analyze.
    :param path: The path to analyze (deprecated).
    :param config: The pytest config object.
    :return: None
    """
    pass


def pytest_collect_directory(path: Path, parent) -> None:
    """
    Create a Collector for the given directory, or None if not relevant.
    New in version 8.0.
        For best results, the returned collector should be a subclass of Directory, but this is not required.
    :param path: The path to analyze.
    :param parent: The new node needs to have the specified parent as a parent.
    :return:
    """
    pass


def pytest_collect_file(file_path: Path, path, parent) -> None:
    """
    Create a Collector for the given path, or None if not relevant.
    For best results, the returned collector should be a subclass of File, but this is not required.
    :param file_path: The path to analyze.
    :param path: The path to collect (deprecated).
    :param parent: The new node needs to have the specified parent as a parent.
    :return:
    """
    pass


def pytest_pycollect_makemodule(module_path: Path, path, parent) -> None:
    """
    Return a pytest.Module collector or None for the given path.
    This hook will be called for each matching test module path. The pytest_collect_file hook needs to be used
    if you want to create test modules for files that do not match as a test module.
    :param module_path: The path of the module to collect.
    :param path: The path of the module to collect (deprecated).
    :param parent:
    :return:
    """
    pass


def pytest_pycollect_makeitem(collector: Union[Module, Class], name: str,
                              obj: object) -> Union[None, Item, Collector, List[Union[Item, Collector]]]:
    """
    Return a custom item/collector for a Python object in a module, or None.
    :param collector: The module/class collector.
    :param name: The name of the object in the module/class.
    :param obj: The object.
    :return: None | Item | Collector | List[Item | Collector]
    """
    pass


def pytest_generate_tests(metafunc: Metafunc) -> None:
    """
    Generate (multiple) parametrized calls to a test function.
    :param metafunc: The Metafunc helper for the test function.
    :return:
    """
    if "custom" in metafunc.fixturenames:
        metafunc.parametrize(
            "custom",
            [1, 2, 3, 4, 5]
        )


def pytest_make_parametrize_id(config: Config, val: object, argname: str) -> None:
    """
    Return a user-friendly string representation of the given val that will be used by
    @pytest.mark.parametrize calls, or None if the hook doesn’t know about val.
    :param config: The pytest config object.
    :param val: The parametrized value.
    :param argname: The automatic parameter name produced by pytest.
    :return:
    """
    pass


def pytest_markeval_namespace(config: Config) -> Dict[str, Any]:
    """
    Called when constructing the globals dictionary used for evaluating string conditions in xfail/skipif markers.
    This is useful when the condition for a marker requires objects that are expensive or impossible to obtain
    during collection time, which is required by normal boolean conditions.
    :param config: The pytest config object.
    :return: Dict[str, Any]
    """
    pass


def pytest_collection_modifyitems(session: Session, config: Config, items: List[Item]) -> None:
    """
    Called after collection has been performed. May filter or re-order the items in-place.
    :param session: The pytest session object.
    :param config: The pytest config object.
    :param items: List of item objects.
    :return: None
    """
    pass


def pytest_collection_finish(session: Session) -> None:
    """
    Called after collection has been performed and modified.
    :param session: The pytest session object.
    :return: None
    """
    print("ITEMS:", session.items)
