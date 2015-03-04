
import requests

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

for url in urls:
	r = requests.get(url)

	if not r.status_code == 200:
		failed_urls.append(url)

if not failed_urls:
	print 'All urls okay'
else:
	print 'Failing urls found'
	print failed_urls
	exit(1)