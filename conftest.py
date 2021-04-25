import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def tests_setup_and_teardown():
    # Will be executed before the first test
    os.environ['ENV'] = 'test'

    yield
    # Will be executed after the last test
    os.environ.pop('ENV')
