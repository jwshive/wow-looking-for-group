import urllib
from urllib import request
import json
import math

# STATIC VALUES
CLASSES = {
    1: "Warrior",
    2: "Paladin",
    3: "Hunter",
    4: "Rogue",
    5: "Priest",
    6: "Death Knight",
    7: "Shaman",
    8: "Mage",
    9: "Warlock",
    10: "Monk",
    11: "Druid",
    12: "Demon Hunter",
}
RACES = {
    1: "Human",
    2: "Orc",
    3: "Dwarf",
    4: "Night Elf",
    5: "Undead",
    6: "Tauren",
    7: "Gnome",
    8: "Troll",
    9: "Goblin",
    10: "Blood Elf",
    11: "Draenei",
    22: "Worgen",
    24: "Pandaren",
    25: "Pandaren",
    26: "Pandaren",

}

FACTION = {
    0: 'Alliance',
    1: 'Horde',
}

ITEMS_OF_VALUE = [
    'head',
    'neck',
    'shoulder',
    'back',
    'chest',
    'wrist',
    'hands',
    'waist',
    'legs',
    'feet',
    'finger1',
    'finger2',
    'trinket1',
    'trinket2',
    'mainHand',
    'offHand'
]

RAID_IDS = [
        8026,
        8440,
        8025,
        8524,
        ]

RAID_LEVELS = [
        'lfr',
        'normal',
        'heroic',
        'mythic',
        ]


class BlizzardAPI:
    def __init__(self):
        pass

    def get_character_stats(self, character_name, server_name, blizzard_api_url_base, client_id, debug=False):

        character_string = "/character/" + server_name.lower() + "/" + character_name.lower()
        character_fields = "?fields=items,talents,progression&local=en_US"

        url_string = blizzard_api_url_base + character_string + character_fields + "&apikey=" + client_id

        if debug:
            print(url_string)

        try:
            response = urllib.request.urlopen(url_string)
            stat_data = json.loads(response.read().decode('UTF-8'))
        except urllib.request.HTTPError:
            return False

        if debug:
            print(stat_data)

        character_level = stat_data['level']
        race = stat_data['race']
        character_class = stat_data['class']
        faction = stat_data['faction']
        thumbnail = stat_data['thumbnail']

        # Determine Spec
        myRange = (len(stat_data['talents']))
        for spec_num in range(myRange):
            try:
                if stat_data['talents'][spec_num]['selected']:
                    spec = (stat_data['talents'][spec_num]['spec']['name'])

            except KeyError:
                pass

        # Get Progression	
        # NEW CODE
        num_raids = len(stat_data['progression']['raids'])
        # this gets me all the raids
        #for raid in range(num_raids):
        #    print(stat_data['progression']['raids'][raid]['name'])

        all_progression = []
    
        for raid in range(num_raids):
            for tracked_raid_id in RAID_IDS:
                if stat_data['progression']['raids'][raid]['id'] == tracked_raid_id:
                    bosses_dead_lfr = []
                    bosses_dead_normal = []
                    bosses_dead_heroic = []
                    bosses_dead_mythic = []
    
                    raid_name = stat_data['progression']['raids'][raid]['name']
                    num_bosses = len(stat_data['progression']['raids'][raid]['bosses'])
                    for boss_kills in range(num_bosses):
                        if stat_data['progression']['raids'][raid]['bosses'][boss_kills]['lfrKills'] != 0:
                            bosses_dead_lfr.append(stat_data['progression']['raids'][raid]['bosses'][boss_kills]['name'])
                        if stat_data['progression']['raids'][raid]['bosses'][boss_kills]['normalKills'] != 0:
                            bosses_dead_normal.append(stat_data['progression']['raids'][raid]['bosses'][boss_kills]['name'])
                        if stat_data['progression']['raids'][raid]['bosses'][boss_kills]['heroicKills'] != 0:
                            bosses_dead_heroic.append(stat_data['progression']['raids'][raid]['bosses'][boss_kills]['name'])
                        if stat_data['progression']['raids'][raid]['bosses'][boss_kills]['mythicKills'] != 0:
                            bosses_dead_mythic.append(stat_data['progression']['raids'][raid]['bosses'][boss_kills]['name'])
    



                    lfr_kills = str(len(bosses_dead_lfr)) + " / " + str(num_bosses)
                    normal_kills = str(len(bosses_dead_normal)) + " / " + str(num_bosses)
                    heroic_kills = str(len(bosses_dead_heroic)) + " / " + str(num_bosses)
                    mythic_kills = str(len(bosses_dead_mythic)) + " / " + str(num_bosses)
    
                    progression_entry = {"raid_name": raid_name, "Normal": normal_kills, "Heroic": heroic_kills, "Mythic": mythic_kills, "LFR": lfr_kills}
                    all_progression.append(progression_entry)

        # END

        legendary_fields = "?fields=items&local=en_US"
        legendary_url_string = blizzard_api_url_base + character_string + legendary_fields + "&apikey=" + client_id

        response = urllib.request.urlopen(legendary_url_string)
        legendary_data = json.loads(response.read().decode('UTF-8'))

        equipped_ilevel = legendary_data['items']['averageItemLevelEquipped']
        weapon_ilevel = legendary_data['items']['mainHand']['itemLevel']

        points_spent = 0

        for item in stat_data['items']['mainHand']['artifactTraits']:
                points_spent += item['rank']

        legendary_items = []

        for item in legendary_data['items']:
            if item in ITEMS_OF_VALUE:
                if legendary_data['items'][item]['quality'] == 5:
                    legendary_items.append(legendary_data['items'][item]['name'])

        if debug:
            print(legendary_data)

        toon_dict = {
                'name': character_name.title(),
                'server': server_name.title(),
                'faction': FACTION[faction], 
                'race': RACES[race],
                'class': CLASSES[character_class],
                'level': character_level,
                'equipped_ilevel': equipped_ilevel,
                'weapon_ilevel': weapon_ilevel,
                'legendaries': '<br>'.join(legendary_items) if legendary_items else "No Legendary Items.",
                'thumbnail': thumbnail,
                'spec': spec,
                'all_progression': all_progression,
                'points_spent': points_spent,
                }
        return toon_dict

