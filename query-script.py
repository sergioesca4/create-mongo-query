import json

def getChefSites():
	with open('site.json') as s:
		dataSite = json.load(s)
	with open('results.json') as f:
		data = json.load(f)
	for result in data:
		numChefSites = len(result['CHEF'])
		print('db.customers.updateOne(')
		print('{ "cdir": ' + '"' + result['CUSTOMER'] + '"},')
		print('{ $set: { "onboardedChefSites": [')
		for i in range(numChefSites):
			dataSite['siteCode'] = result['CHEF'][i]
			print(json.dumps(dataSite, indent = 2, sort_keys = True),','if i < numChefSites-1 else '', sep='')
		print('] } } )')

getChefSites()