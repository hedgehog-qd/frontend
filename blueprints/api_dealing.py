import requests


def request_data(mode,sort):
    url = "https://api.yukiharu.pw/get_leaderboard"
    url = url+"?mode="+mode+"&sort="+sort
    req = requests.get(url, timeout=30)  # CONNECT
    req_json = req.json()  # GET THE DATA
    return req_json