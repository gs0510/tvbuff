r"""
heloooooooooooo
TV buff is a command line guide that helps you track your favorite shows
Usage:
  tvbuff next <show-name>
  	example: tvbuff next "Game of thrones"
  tvbuff previous <show-name>
  	example: tvbuff previous "Game of thrones"
  tvbuff episodes <show-name> 
  	example: tvbuff episodes "Game of thrones"
  tvbuff list <country> <date> 
  	example : tvbuff list "US" "2016-12-25"
  tvbuff (-h |--help)
Options:
  -h --help   Show this screen.
  --version   Show version.
"""

import requests
from docopt import docopt
import json
from tabulate import tabulate
import re

__version__ = '0.0.9'

def getUrl(show, number):
	url = "http://api.tvmaze.com/search/shows"
	params = { 'q': show}
	response = requests.get(url, params=params)
	if response.status_code == 200:
		data = response.json()
		if number == -1:
			try:
				url = data[0]['show']['_links']['previousepisode']['href']
				return url
			except:
				return "null"
		elif number == 1:
			try:
				url = data[0]['show']['_links']['nextepisode']['href']
				return url
			except:
				return "null"
	else:
		print "API Issues"

def nextEpisode(show):
	url = getUrl(show,1)
	if url != "null":
		response = requests.get(url)
		if response.status_code == 200:
			try:
				data = response.json()
				table = [[data['name'], data['airdate']]]
				print tabulate(table, headers=["Name", "Air Date"])
			except:
				print "API Issues"
		else:
			print "API Issues"
	else:
		print "Next episode does not exist!"

def previous(show):
	url = getUrl(show,-1)
	if url != "null":
		response = requests.get(url)
		if response.status_code == 200:
			try:
				data = response.json()
				table = [[data['name'], data['airdate']]]
				print tabulate(table, headers=["Name", "Air Date"])
			except:
				print "API Issues"
		else:
			print "API Issues"
	else:
		print "Previous episode does not exist!"

def listEpisodes(country, date):
	url = "http://api.tvmaze.com/schedule"
	params = { 'country': country, 'date': date}
	response = requests.get(url, params)
	if response.status_code == 200:
		try:
			data = response.json()
			table = []
			for show in data:
				table.append([show['show']['name'], show['name'], show['airtime'], show['show']['network']['name']])
			print tabulate(table, headers=["Show Name", "Episode Name", "Airtime", "Network"])
		except Exception, e:
			print "API Issues"
	else:
		print "API Issues"

def episodes(show):
	url = "http://api.tvmaze.com/singlesearch/shows"
	params = { 'q': show, 'embed':'episodes'}
	response = requests.get(url, params)
	if response.status_code == 200:
		try:
			data = response.json()
			episodes = data['_embedded']['episodes']
			table = []
			for episode in episodes:
				try:
					summary = re.sub('<[^>]*>', '', episode['summary'])
				except:
					summary = ""
				table.append([episode['name'], episode['season'], episode['number'], episode['airdate'], summary])
			print tabulate(table, headers=["Episode Name", "Season", "Number", "Air Date", "Summary"])
		except Exception, e:
			print "API Issues"
	else:
		print "API Issues"

def main():
  
  arguments = docopt(__doc__, version=__version__)
  
  if arguments['next']:
    nextEpisode(arguments['<show-name>'])
  elif arguments['previous']:
    previous(arguments['<show-name>'])
  elif arguments['episodes']:
    episodes(arguments['<show-name>'])
  elif arguments['list']:
    listEpisodes(arguments['<country>'],arguments['<date>'])
  else:
   	print "bahaha"

if __name__ == '__main__':
  main()