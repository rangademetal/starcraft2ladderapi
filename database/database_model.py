from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Starcraft2Ladder_model(Base):
    __tablename__ = 'Starcraft2Ladder'
    rank: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    ratting: Mapped[str] = mapped_column(String(10))
    game_played: Mapped[str] = mapped_column(String(10))
    winrate: Mapped[str] = mapped_column(String(10))
    region: Mapped[str] = mapped_column(String(10))
    commander: Mapped[str] = mapped_column(String(10))
