#!/usr/bin/env python

import sys, json, urllib2
from BeautifulSoup import BeautifulSoup
user_agent="/r/tinycode languages finder"

def load_wikipedia_style(url, baseurl, dict):
	soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers={"User-Agent":user_agent})).read())
	tables = soup.findAll('table', {'class': 'multicol'})
	trs = []
	for table in tables: trs.extend(table.findAll('tr')) 
	tds = []
	for tr in trs: tds.extend(tr.findAll('td'))
	uls = filter(lambda x: x != None, map(lambda td: td.ul, tds))
	lis = []
	for ul in uls: lis.extend(ul.findAll('li'))
	for li in lis:
		if li.a: #has a wikipedia page
			name = li.a.contents[0]
			href = baseurl+li.a['href']
			languages[name]=href
		else: #no page, ex. EASY
			name = li.contents[0]
			languages[name]="http://www.google.com?s=%s"%name

def load_esolangs_style(url, baseurl, dict):
	soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers={"User-Agent":user_agent})).read())
	uls = soup.findAll('ul')
	uls = uls[:len(uls)-11] #strip out lists in footer
	lis = []
	for ul in uls: lis.extend(ul.findAll('li'))
	for li in lis:
		if li.a: #has a wikipedia page
			name = li.a.contents[0]
			href = baseurl+li.a['href']
			languages[name]=href
		else: #no page, ex. EASY
			name = li.contents[0]
			languages[name]="http://www.google.com?s=%s"%name


languages={}
load_esolangs_style("http://esolangs.org/wiki/Language_list", "http://esolangs.org", languages)
load_wikipedia_style("http://en.wikipedia.org/wiki/List_of_programming_languages", "http://en.wikipedia.org", languages)
f=open(sys.argv[1], 'w')
j=json.dumps(languages)
f.write(j)
print "Wrote %d bytes (%d languages)"%(len(j),len(languages))
f.close()