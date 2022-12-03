from enum import Enum
import requests


class SportradarRequestType(Enum):
    SR_UNDEFINED = 0
    SR_GAME_SUMMARY = 1
    SR_PLAYER_INFO = 2
    SR_STANDINGS = 3


class SportradarRequest:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = ""
        self.type = SportradarRequestType.SR_UNDEFINED

    def build_gs_url(self, gid):
        self.url = f"https://api.sportradar.us/nhl/trial/v7/en/games/{gid}/summary.json?api_key={self.api_key}"
        self.type = SportradarRequestType.SR_GAME_SUMMARY

    def build_pi_url(self, tid):
        self.url = f"https://api.sportradar.us/nhl/trial/v7/en/teams/{tid}/profile.json?api_key={self.api_key}"
        self.type = SportradarRequestType.SR_PLAYER_INFO

    def build_stnd_url(self, year, season):
        self.url = f"https://api.sportradar.us/nhl/trial/v7/en/seasons/{year}/{season}/standings.json?api_key={self.api_key}"
        self.type = SportradarRequestType.SR_STANDINGS
    
    def json_req(self):
        req = requests.get(self.url)

        if req.ok:
            return req.json()
        else:
            print(f"Request failed: {req.status_code}")
            return -1
