import pytest


@pytest.fixture(scope="function")
def first_fix():
    print("Calling first_fix")
    yield
    print("Teardown first_fix")
