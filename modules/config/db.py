import sqlitedict
import json


class ConfigDatabase(sqlitedict.SqliteDict):
    def __init__(self, tablename):
        super().__init__(
            filename='config.storage',
            tablename=tablename,
            encode=json.dumps,
            decode=json.loads,
            autocommit=True
        )


config = ConfigDatabase('config')
sessions = ConfigDatabase('sessions')
