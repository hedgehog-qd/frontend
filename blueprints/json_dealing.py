from blueprints import api_dealing
import json



def DealJson(mode,sort):
    jsonn = api_dealing.request_data(mode,sort)
    json_str = json.dumps(jsonn)
    data2 = json.loads(json_str)
    sta = data2['status']
    lb = data2['leaderboard']
    return lb
