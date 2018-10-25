# pytest configuration file
import pytest
from database import Database, allowed_targets
from etl_config import etl_objects, pusheen_etls, hellokitty_etls

# command line options
def pytest_addoption(parser):
    parser.addoption(
        "--target", action="store", help="Set target database."
)

# fixtures - something your tests depend on, such as mocks, common resources, etc
@pytest.fixture
def target(request):
    return request.config.getoption("--target")

@pytest.fixture    
def db(target):
    db = Database(target)

# next slide, markers & parametrization       
def pytest_generate_tests(metafunc):
    target_in = metafunc.config.getoption('target')
    assert target_in, "target is required!"
    assert target_in.lower() in allowed_targets, "target not found in allowed targets list"
    target = target_in
    if "etl_object" in metafunc.fixturenames:
        filtered_objects = []
        if target == 'hellokitty_test':
            filtered_objects = [obj for obj in etl_objects if obj.name() in hellokitty_etls]
        if target == 'pusheen_test':
            filtered_objects = [obj for obj in etl_objects if obj.name() in pusheen_etls]

        metafunc.parametrize('etl_object', filtered_objects, ids=[ obj.name() for obj in filtered_objects ])
        