# just a stup for a database class

# no running tests on production!
allowed_targets = [
 'pusheen_test',
 'hellokitty_test'
]

class Database(object):
    def __init__(self, target):
        if target not in allowed_targets:
            raise ValueError("target %s not found in allowed targets" % target)
        self.__config = target
        
def execute_stored_proc(query, dbconn):
    # function stub for running a stored procedure
    return True