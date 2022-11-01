import assets.pyFiles.enviroment_info as private
import requests
url = f"https://api.the-odds-api.com/v4/sports/?apiKey={private.bet_api_key}"
betRequest = requests.get(url)
bet = betRequest.json()
sport = 'icehockey_nhl'
region = 'us'
markets = ['h2h', 'spreads', 'totals']
market = 'h2h'
print(bet)
url_upcoming = 'https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=us&markets=h2h&apiKey=YOUR_API_KEY'
url_upcoming = f"https://api.the-odds-api.com/v4/sports/{sport}/odds/?apiKey={private.bet_api_key}&regions={region}&markets={market}"
betRequest = requests.get(url_upcoming)
bet = betRequest.json()
for game in bet:
    print(game['home_team'], game['away_team'], game['commence_time'])
    for book in game['bookmakers']:
        print(book['title'])
        for odds in book['markets'][0]['outcomes']:
            print(odds)