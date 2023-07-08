import json
from fastapi import FastAPI

from sqlalchemy import update
from sqlalchemy.orm import Session

from database.connector import ConnectorSQLAlchemy
from WebScrap.StarcrafLadder import Starcraft2Ladder
from database.database_model import Starcraft2Ladder_model

app = FastAPI()

with open(r'F:\pythonProject\StarCraft2Ladder\database\db_credential.json', 'r') as databasedatcredential:
    credential = json.load(databasedatcredential)

    connector_database = ConnectorSQLAlchemy(
        username=credential['DB_CREDENTIAL']['username'],
        password=credential['DB_CREDENTIAL']['password'],
        host=credential['DB_CREDENTIAL']['host'],
        port=credential['DB_CREDENTIAL']['port'],
        database=credential['DB_CREDENTIAL']['database']
    )


@app.get('/start/')
async def test():
    return {'work': "work"}


#
@app.post('/insert_ladder/')
async def insert():
    sc = Starcraft2Ladder()
    data = await sc.get_rank()
    engine = connector_database.connector()
    with Session(engine) as session:
        for _ in data:
            stmt = Starcraft2Ladder_model(
                rank=_['rank'],
                name=_['name'],
                ratting=_['ratting'],
                game_played=_['game_played'],
                winrate=_['winrate'],
                region=_['region'],
                commander=_["commander"]
            )
            session.add(stmt)
            session.commit()

    return {'World': "Work"}


@app.put('/update_ladder/')
async def update_ladder():
    sc = Starcraft2Ladder()
    data = await sc.get_rank()
    engine = connector_database.connector()
    with Session(engine) as session:
        for _ in data:
            stmt = (
                update(Starcraft2Ladder_model).where(Starcraft2Ladder_model.rank == _['rank']).values(
                    name=_['name'],
                    ratting=_['ratting'],
                    game_played=_['game_played'],
                    winrate=_['winrate'],
                    region=_['region'],
                    commander=_['commander']
                )
            )

            session.execute(stmt)
            session.commit()


