import requests
from bs4 import BeautifulSoup
import json


steam_link = 'https://steamcommunity.com/market/listings/570/'
items_link = 'https://www.dotaweb.com/en/store/'

heroes_dict = {}

heroes = ['abaddon', 'alchemist', 'ancient-apparition',
          'anti-mage', 'arc-warden', 'axe', 'bane', 'batrider',
          'beastmaster', 'bloodseeker', 'bounty-hunter',
          'brewmaster', 'bristleback', 'broodmother', 'centaur-warrunner',
          'chaos-knight', 'clinkz', 'clockwerk', 'crystal-maiden', 'dark-seer', 'dark-willow', 'dazzle',
          'death-prophet', 'disruptor', 'doom', 'dragon-knight',
          'drow-ranger', 'earth-spirit', 'earthshaker', 'elder-titan', 'ember-spirit', 'enchantress', 'enigma',
          'grimstroke', 'gyrocopter', 'huskar', 'invoker', 'jakiro', 'juggernaut', 'keeper-of-the-light', 'kunkka',
          'legion-commander', 'leshrac', 'lich',
          'lifestealer', 'lina', 'lion', 'lone-druid', 'luna',
          'lycan', 'magnus', 'medusa', 'meepo', 'mirana', 'monkey-king', 'morphling', 'naga-siren', 'natures-prophet',
          'necrophos', 'night-stalker', 'nyx-assassin',
          'ogre-magi', 'omniknight',
          'oracle', 'outworld-devourer', 'pangolier', 'phantom-assassin', 'phantom-lancer', 'phoenix', 'puck', 'pudge',
          'pugna', 'queen-of-pain', 'razor', 'riki', 'rubick',
          'sand-king', 'shadow-demon', 'shadow-fiend',
          'shadow-shaman', 'silencer', 'skywrath-mage', 'slardar', 'slark', 'sniper', 'spectre', 'spirit-breaker',
          'storm-spirit', 'sven', 'techies',
          'templar-assassin', 'terrorblade', 'tidehunter', 'timbersaw', 'tinker', 'tiny', 'treant-protector',
          'troll-warlord', 'tusk', 'underlord',
          'undying', 'ursa', 'vengeful-spirit', 'venomancer', 'viper', 'visage', 'warlock', 'weaver', 'windranger',
          'winter-wyvern', 'witch-doctor', 'wraith-king', 'zeus', 'faceless-void']

def all_items_finder(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    want = soup.find_all('a', {"title": True})
    hrefs = []

    for x in want:
        if ((x.get('title')).find("Items Skins") < 1):
            hrefs.append(x.get('href'))

    return hrefs


def set_finder(href):
    wanted = []
    newurl = href
    response1 = requests.get(newurl)
    soup_sets = BeautifulSoup(response1.text, 'lxml')
    quotes = soup_sets.find_all('img', {'alt': True})
    for i in quotes:
        attribute = i.get('alt')[:-9]
        wanted.append(attribute)
    if len(wanted) > 0:
        wanted.pop(-1)

    return wanted


for iter in heroes:

    heroes_dict[iter] = {}
    print(f"I am checkin'   {iter}")
    url = items_link
    url += iter
    hrefs = all_items_finder(url)

    for i in hrefs:
        sets_names = set_finder(i)

        if len(sets_names) > 1:
            heroes_dict[iter][sets_names[0]] = sets_names[1:-1]



with open('all_heroes_sets.json', 'w') as file:
    json.dump(heroes_dict, file)