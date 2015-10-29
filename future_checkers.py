
import requests
from concurrent.futures import *

urls = [
	'http://gu-email-renderer.appspot.com/daily-email-us/v6',
	'http://gu-email-renderer.appspot.com/daily-email/v1',
	'http://gu-email-renderer.appspot.com/daily-email-aus/v1',
	'http://gu-email-renderer.appspot.com/comment-is-free/v1',
	'http://gu-email-renderer.appspot.com/fashion-statement/v1',
	'http://gu-email-renderer.appspot.com/zip-file/v1',
	'http://gu-email-renderer.appspot.com/bookmarks/v1',
]

failed_urls = []

with ThreadPoolExecutor(max_workers=3) as executor:
	url_reads = [executor.submit(lambda url: requests.get(url), url) for url in urls]

	for read in url_reads:
		r = read.result()

		if not r.status_code == 200:
			failed_urls.append(url)

if not failed_urls:
	print 'All urls okay'
else:
	print 'Failing urls found'
	print failed_urls
	exit(1)