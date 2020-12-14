from pytest import fixture


@fixture(scope='function')  # for each function one browser
# @fixture(scope='session')   # run one browser for on session
def some_func():
    pass
