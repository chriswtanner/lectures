# DEMO CODE
import requests
from bs4 import BeautifulSoup
import re

def download_website(url):
	'''
	purpose: downoads a given, passed-in webpage url
	input: url
	output: saves the webpage to the hard drive
	'''

	# gets the webpage
	page = requests.get(url)
	if page.status_code != 200:
		return
	soup = BeautifulSoup(page.content, 'html.parser')
	# gets paragraphs of text
	paragraphs = soup.find_all('p')

def main():
	'''
	purpose: illustrates how to grab a webpage and its links
	input: url (which we hard-code; it's not a parameter)
	output: saves webpages to the hard drive
	'''

	# gets the webpage
	url = "http://transcripts.cnn.com/TRANSCRIPTS/2017.04.25.html"
	page = requests.get(url)
	if page.status_code != 200:
		exit(1)
	soup = BeautifulSoup(page.content, 'html.parser')

	# returns a list of BeautifulSoup elements
	links = soup.find_all('a', href=True)

	# iterates throught each Beautiful Link
	transcript_urls = []
	for link in links:
		url = link['href']
		match = re.search("/TRANSCRIPTS/.*\.html", url)
		if match is not None:
			transcript_urls.append(url)
	transcript_urls = transcript_urls[1:]
	print(transcript_urls)

	# let's download each link
	for link in transcript_urls:
		new_url = "http://transcripts.cnn.com" + link
		download_website(new_url)

if __name__ == '__main__':
    main()
