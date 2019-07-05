import os

import requests
import json

with open('ranks.json') as f:
    json_object = json.load(f)

serverName = 'Dalaran'
serverRegion = 'US'
API_KEY = '341c82fa145e16d0c4be777652293a9f'
counterMax = 15

data = []

for guild in json_object:
    guildRank = guild['Rank']
    guildName = guild['Guild']
    dirName = f'{serverName}/{guildName}'

    print(f"Creating {guildName}")
    r = requests.get(
        f'https://www.warcraftlogs.com/v1/reports/guild/{guildName}/{serverName}/{serverRegion}?limit=1&api_key={API_KEY}',
    )

    if r.ok:
        try:
            os.mkdir(dirName)
        except FileExistsError:
            print("Directory ", dirName, " already exists")

        with open(f'{serverName}/{guildName}/All.json', 'w') as outfile:
            json.dump(r.json(), outfile)

        with open(f'{serverName}/{guildName}/{counterMax}_Latest.json', 'w') as outfile:
            json.dump(r.json()[:counterMax], outfile)

        latest = r.json()[:counterMax]

        for i in latest:
            print(f"{i['id']}")

        with open(f'{serverName}/{guildName}/Latest_links.html', 'w') as outfile:
            outfile.write('<html>')
            outfile.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">')
            outfile.write('</header>')
            outfile.write('<body style="background-color: #343a40; padding: 1em;">')
            outfile.write(f"<h2 class='bg-inverse text-white'>{guildName}</h2>")
            outfile.write(f"<h5 class='bg-inverse text-white'>Ranked #{guildRank} on {serverName}</h5>")
            outfile.write('<table class="table table-dark">')
            outfile.write('<tr>')
            outfile.write('<th>Log Name</th>')
            outfile.write('<th>Log Report</th>')
            outfile.write('<th>Wipefest Report</th>')
            outfile.write('</tr>')
            for i in latest:
                outfile.write('<tr>')
                outfile.write(f"<td>{i['title']}</td>")
                outfile.write(f"<td><a href=https://www.warcraftlogs.com/reports/{i['id']}>https://www.warcraftlogs.com/reports/{i['id']}</a></td>")
                outfile.write(f"<td><a href=https://www.wipefest.net/report/{i['id']}>https://www.wipefest.net/report/{i['id']}</a></td>")
                outfile.write('</tr>')
            outfile.write('</table>')
            outfile.write('</body>')
            outfile.write('</html>')
