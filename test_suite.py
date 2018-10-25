import pytest
import pandas as pd
from etl_config import etl_objects

# @pytest.mark.etl
# @pytest.mark.parametrize("etl_input", etl_objects, ids=[obj.name() for obj in etl_objects])
# def test_param_mark(etl_input, db):
#     etl_input.initialize(db)
#     etl_input.loadData()
#     etl_input.match()
#     etl_input.validate()
#     etl_input.dispose()
#     etl_input.apply()
#     df_result = etl_input.checkResults()
#     assert df_result.empty == True

# what if we only want to run a subset of ETL tests based on the target?
@pytest.mark.etl
def test_param_fixture(etl_object, db):
    etl_object.initialize(db)
    etl_object.loadData()
    etl_object.match()
    etl_object.validate()
    etl_object.dispose()
    etl_object.apply()
    df_result = etl_object.checkResults()
    assert df_result.empty == True
    
@pytest.mark.specimen
def test_incorrect_specimen_hierarchy():
    assert True

@pytest.mark.specimen
def test_correct_specimen_hierarchy():
    assert True
    
@pytest.mark.mutation
def test_failing_record_mutation():
    assert True
    
@pytest.mark.mutation
def test_passing_record_mutation():
    assert True
