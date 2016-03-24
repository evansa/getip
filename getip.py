import os
import sys
import json
import urllib
from texttable import Texttable

t = Texttable()
def query(address):
	result = urllib.urlopen('http://ip-api.com/json/'+address)
	result = result.read()
	try:
		data = json.loads(result)
	except ValueError, e:
		print 'sorry your query could not be completed.'
		sys.exit(1)
	extract_address(data)
		
def extract_address(to_extract):
	if len(to_extract) < 6:
		print 'We don\'t have enough information for you, sorry'
		quit()
		
	t.add_rows([["Value",'Response'], 
				["Country:",to_extract['country']], 
				["Country Code:", to_extract['countryCode']], 
				["Region:", to_extract['region']],
				["Region Name:", to_extract['regionName']],
				["City:", to_extract['city']],
				["Latitude:", to_extract['lat']],
				["Longitude:", to_extract['lon']],
				["Timezone:", to_extract['timezone']],
				["ISP:", to_extract['isp']],
				["Organisation:", to_extract['org']],
				["Autonomous System Number & Name:", to_extract['as']],
				["Querying data Address (You):", to_extract['query']]
				
				])
	print t.draw()

def help():
	#add more meaningful info
	print 'Invalid arguments'	
	
if __name__ == "__main__":
	args = sys.argv
	if len(args) < 2 or len(args)  > 2:
		help()
		quit()
	
	to_query = args[1]
	query(to_query)
