import time
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import datetime
import json
# import beautifulsoup4
from bs4 import BeautifulSoup

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders == [('User-agent', 'Mozilla/5.0')]

def Read(filepath):
	file = open(filepath, 'r')
	text = file.read()
	# print text
	return text

class Hortal(object):
	"""docstring for Hortal"""
	def __init__(self, title,istomorrowhartal, details, source):
		super(Hortal, self).__init__()
		self.title = title
		self.istomorrowhartal = istomorrowhartal
		self.details = details
		self.source = source
		
		

def Download():
	try:
		page = 'http://istomorrowhartal.com/'
		sourceCode = opener.open(page).read()
		# sourceCode = Read('be.html')
		# print sourceCode
		try:



			soup = BeautifulSoup(sourceCode)			
			title = soup.html.head.title
			# print title.string

			div = soup.html.body
			content = div.findAll("div",{"class":"align"})	
			# print div.h2.text		
			# print div.findAll("p")[0].text
			# print div.findAll("p")[1].a['href']

			hortal = Hortal(title.string,
							div.h2.text,
							div.findAll("p")[0].text,
							div.findAll("p")[1].a['href']
							)
			
			print hortal.title
			print hortal.istomorrowhartal
			print hortal.details
			print hortal.source

			Json = json.dumps(vars(hortal))
			return Json
			# print vars(hortal)
		except Exception, e:
			print "2nd try catch : " + str(e)
	except Exception, e:
		print "1st try catch : " + str(e)

Download()