from django.shortcuts import render, HttpResponse
from .models import RequestedParses
import json
from base64 import b64encode, b64decode
import sys
from frontdoor.api_functions import BlizzardAPI

# Create your views here.
def index(request):
    return render(request, 'index.html')

def parse_group(request):
    ENCODING = 'utf-8'

    # Convert to JSON
    json_data = json.loads(b64decode(request.POST['JSON']).decode(ENCODING).replace('\'', '"'))

    # Store group string in db
    new_data = RequestedParses.objects.create(requesting_member=json_data['request']['requesting-member-name'], requesting_member_realm=json_data['request']['requesting-member-realm'], group_string=request.POST['JSON'], json_string=json_data)

    # get the information I just stored and start the api calls
    toons_to_parse = RequestedParses.objects.get(id=new_data.id)

    # When parsing toons, store the resulting toon information in the database.
    # Find a way to cache that for an hour so that we're not making 1000 api calls for the same data.import sysrom api_functions import BlizzardAPI
    
    api_call = BlizzardAPI()
    
    toon_info = []
    
    for item in json_data['request']['group']['members']:
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
        # Send the info back
    return render(request, 'result.html', {'toon_info': toon_info})


def show_parses(request):
    my_stuff = RequestedParses.objects.all()
    return render(request, 'show.html', {'my_stuff': my_stuff})


