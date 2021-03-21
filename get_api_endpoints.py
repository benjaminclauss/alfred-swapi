#!/usr/bin/python

import sys
from workflow import Workflow, web

def main(wf):
	url = 'https://swapi.dev/api/'
	params = dict(format='json')
	r = web.get(url, params)
	
	r.raise_for_status()
	result = r.json()
	
	# Loop through the returned endpoint and add an item for each to the list of results for Alfred.
	for dataType, endpoint in result.items():
		subtitle = "Look up " + dataType + " data"
		wf.add_item(title=dataType.capitalize(), subtitle=subtitle, arg=endpoint, valid=True)
	
	wf.send_feedback()

if __name__ == "__main__":
	wf = Workflow()
	sys.exit(wf.run(main))
