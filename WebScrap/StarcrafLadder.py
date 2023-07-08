import json
import asyncio

import aiohttp
from bs4 import BeautifulSoup


class Starcraft2Ladder:
    def __init__(self):
        pass

    async def get_rank(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://ds-rating.com/players') as response:
                soup = BeautifulSoup(await response.text(), 'html.parser')
                # print(soup)
                details = soup.find('tbody', {"id":"players_table"})
                # print(details)
                rows = details.find_all("tr")
                details = []
                for row in rows:

                    rank = row.find('th').text.split('.')[0]
                    name = row.findNext('th').text.split('.')[1].strip()
                    ratting = row.find_next('td').text
                    game_played = row.findNext('td').findNext('td').text
                    winrate = row.findNext('td').findNext('td').findNext('td').text
                    region = row.findNext('td').findNext('td').findNext('td').findNext('td').text
                    commander = row.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').text

                    details.append({
                        'rank': rank,
                        'name': name,
                        'ratting': ratting,
                        "game_played": game_played,
                        "winrate": winrate,
                        'region': region,
                        "commander": commander
                    })
                return details

# sc = Starcraft2Ladder()
# print(asyncio.run(sc.get_rank()))





                # return arr

#
# sc = Starcraft2Ladder()
# print(asyncio.run(sc.get_rank()))