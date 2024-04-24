import json
import os
import requests
import sys
import urllib.request

folder = sys.argv[2]
page = 0
steamId = sys.argv[1]

if not os.path.isdir(folder):
    os.mkdir(folder)

while page >= 0:
    with urllib.request.urlopen('https://store.steampowered.com/wishlist/profiles/' + steamId + '/wishlistdata/?p=' + str(page)) as url:
        data = json.load(url)
        if(len(data) == 0):
            sys.exit()

#gomes = open('gomes.json')

#data = json.load(gomes)

        for i in data.keys():
            urln = data[i]['capsule'].replace('\\','')
            img_data = requests.get(urln).content
            name = i + '.jpg'
            print(name)
            with open(folder + '/' + name, 'wb') as handler:
                handler.write(img_data)
                
    page = page + 1
	
#gomes.close()