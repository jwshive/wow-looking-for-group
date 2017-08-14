#!/usr/bin/env python
import urllib
from urllib import request
import json

url_string = "https://us.api.battle.net/wow/character/grizzly-hills/peppiwyn?fields=items&local=en_US&apikey=bvzccjmbfrjbrdb85u2fvgqtcu6bcmrk"

response = urllib.request.urlopen(url_string)
stat_data = json.loads(response.read().decode('UTF-8'))

points_spent = 0

for item in stat_data['items']['mainHand']['artifactTraits']:
    points_spent += item['rank']

print(points_spent)
