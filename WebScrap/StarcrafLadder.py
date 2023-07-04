import json
import asyncio

import aiohttp
from bs4 import BeautifulSoup


class Starcraft2Ladder:
    def __init__(self):
        pass

    async def get_rank(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.rankedftw.com/ladder/lotv/1v1/mmr/') as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                table = soup.find_all('a', {'class': "row"})
                arr = []
                for i in table:
                    details = i.find_all('div', {'class': 'cell number'})

                    rank = details[0].text
                    mmr = details[1].text
                    points = details[2].text
                    wins = details[3].text
                    losses = details[4].text
                    played = details[5].text
                    winrate = details[6].text
                    player_name = i.find('div', 'cell player').text.strip()

                    arr.append({
                        "rank": rank,
                        "name": player_name,
                        "mmr": mmr,
                        "points": points,
                        "win": wins,
                        "lost": losses,
                        "game_played": played,
                        "win_rate": winrate
                    })
                return arr


a = Starcraft2Ladder()
data = asyncio.run(a.get_rank())
# data = json.load(data)

with open('test.json', "w") as file_writer:
    json.dump(data, file_writer, indent=4 )


