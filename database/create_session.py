import json


from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.orm import Session

from database.connector import ConnectorSQLAlchemy
from database.database_model import Base, Starcraft2Ladder_model

if __name__ == '__main__':
    with open(r'F:\data\db_credential.json', "r") as database_credential:
        credential = json.load(database_credential)

        connector_database = ConnectorSQLAlchemy(
            username=credential['DB_CREDENTIAL']['username'],
            password=credential['DB_CREDENTIAL']['password'],
            host=credential['DB_CREDENTIAL']['host'],
            port=credential['DB_CREDENTIAL']['port'],
            database=credential['DB_CREDENTIAL']['database']
        )

    engine = connector_database.connector()
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        stmt = (
            update(Starcraft2Ladder_model).where(Starcraft2Ladder_model.rank == '200').values(name='test')
        )
        print(stmt)
        session.execute(stmt)
        session.commit()


