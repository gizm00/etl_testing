from EtlStub import Etl

pusheen_etls = ["treatment", "specimen"]
hellokitty_etls = ["genomics", "new"]

treatment_etl = Etl(
    'etl_files/treatment_test_data.csv',
    'etl.treatment_interface',
    'etl.f_treatment_match',
    'etl.f_treatment_validate',
    'etl.f_treatment_dispose',
    'etl.f_treatment_apply',
    ['agentid', 'deliveryid', 'accept'],
    "treatment"
)

genomics_etl = Etl(
    'etl_files/genomics_test_data.csv',
    'etl.genomics_interface',
    'etl.f_genomics_match',
    'etl.f_genomics_validate',
    'etl.f_genomics_dispose',
    'etl.f_genomics_apply',
    ['geneid', 'accept'],
    "genomics"
)

specimen_etl = Etl(
    'etl_files/specimen_test_data.csv',
    'etl.specimen_interface',
    'etl.f_specimen_match',
    'etl.f_specimen_validate',
    'etl.f_specimen_dispose',
    'etl.f_specimen_apply',
    ['typeid', 'ownerid', 'accept'],
    "specimen"
)

new_etl = Etl(
    'etl_files/specimen_test_data.csv',
    'etl.specimen_interface',
    'etl.f_specimen_match',
    'etl.f_specimen_validate',
    'etl.f_specimen_dispose',
    'etl.f_specimen_apply',
    ['typeid', 'ownerid', 'accept'],
    "new"
)

etl_objects = [treatment_etl, genomics_etl, specimen_etl, new_etl]

# for obj in etl_object:
#     obj.initialize(db)
#     obj.loadData()
#     obj.match()
#     obj.validate()
#     obj.dispose()
#     obj.apply()
#     df_result = obj.checkResults()