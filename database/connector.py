import sqlalchemy


class ConnectorSQLAlchemy:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.passord = password
        self.host = host
        self.port = port
        self.database = database

    def connector(self):
        return sqlalchemy.create_engine(
            f"mariadb+mariadbconnector://{self.username}:{self.passord}@{self.host}:{self.port}/{self.database}?CHARSET=utf8mb3;")
