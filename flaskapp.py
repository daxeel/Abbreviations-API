# Import required modules
import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<filter_type>/<word>')
def search(filter_type, word):
	URL = "http://fullforms.com/"+ word
	PAGE = requests.get(URL)
	HTML = PAGE.content
	soup = BeautifulSoup(HTML, "html.parser")

	if filter_type == 'popular':
		try:
			ff = soup.tr.strong.string
			mean = soup.p.string
		except:
			ff = 'Not found'
			mean = 'Not found'
		return json.dumps({'fullform': ff, 'meaning': mean}, sort_keys=True, indent=4, separators=(',', ': '))

	elif filter_type == 'all':
		found = 0
		ALL_URLS = []
		final = []

		try:
			ff = soup.tr.strong.string
			mean = soup.p.string
			final.append({'fullform': ff, 'meaning': mean})
			found = 1
		except:
			ff = 'Not found'
			mean = 'Not found'
			final.append({'fullform': ff, 'meaning': mean})

		if found == 1:
			all_trs = soup.find_all('table')[2].tbody.find_all('tr')
			print len(all_trs)
			for i in all_trs:
				try:
					all_tds = i.find_all('td')
					ALL_URLS.append(all_tds[3].a['href'])
				except:
					pass

			for i in ALL_URLS:
				URL = i
				PAGE = requests.get(URL)
				HTML = PAGE.content
				soup = BeautifulSoup(HTML, "html.parser")

				try:
					ff = soup.tr.strong.string
					mean = soup.p.string
				except:
					ff = 'Not found'
					mean = 'Not found'

				final.append({'fullform': ff, 'meaning': mean})

		return json.dumps(final, sort_keys=True, indent=4, separators=(',', ': '))

	else:
		return json.dumps({'error': 'Invalid API syntax'}, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    app.run(debug=True)
