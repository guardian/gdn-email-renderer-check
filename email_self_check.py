import requests
import concurrent.futures as futures
from bs4 import BeautifulSoup

url = 'http://gu-email-renderer.appspot.com'

home_page_request = requests.get(url)

if not home_page_request.status_code == 200:
	print 'Could not load the home page'
	exit(1)

front_page_soup = BeautifulSoup(home_page_request.text)

urls = {url + a['href'] for a in front_page_soup.find_all('a') if a['href'].startswith('/')}

failed_urls = []

with futures.ThreadPoolExecutor(max_workers=3) as executor:
	url_reads = [executor.submit(lambda url: requests.get(url), url) for url in urls]

	for read in url_reads:
		r = read.result()

		if not r.status_code == 200:
			failed_urls.append(r.url)

if not failed_urls:
	print 'All urls okay'
else:
	print 'Failing urls found'
	print failed_urls
	exit(1)