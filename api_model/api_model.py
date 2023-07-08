from fastapi import FastAPI
from pydantic import BaseModel


class Starcraft2LadderApiModel(BaseModel):
    rank: str
    name: str
    ratting: str
    game_played: str
    winrate: str
    region: str
    commander: str
