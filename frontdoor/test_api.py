import json
import sys
from api_functions import BlizzardAPI

JSON_STRING = {'request': {'requesting-member-name': 'Taltost', 'requesting-member-realm': 'Grizzly Hills', 'group': {'members': [{'realm': 'Grizzly Hills', 'name': 'Peppiwyn'}, {'realm': 'Lothar', 'name': 'Fuzzy'}, {'realm': 'Grizzly Hills', 'name': 'Shyne'}]}}}

JSON_STRING = json.loads(str(JSON_STRING).replace('\'', '"'))

api_call = BlizzardAPI()

toon_info = []

for item in JSON_STRING['request']['group']['members']:
    results = api_call.get_character_stats(item['name'], item['realm'].replace(' ','-'))
    toon_class = results['class']
    toon_faction = results['faction']
    toon_ilevel = results['equipped_ilevel']
    toon_name = results['name']
    toon_race = results['race']
    toon_spec = results['spec']
    toon_legendaries = results['legendaries']
    toon_realm = results['server']

    toon_stash = "(%s,%s,%s,%s,%s,%s,%s,%s)" % (toon_class, toon_faction, toon_ilevel, toon_name, toon_race, toon_spec, toon_legendaries, toon_realm)
    toon_info.append(toon_stash)
