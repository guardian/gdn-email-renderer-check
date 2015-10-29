# Email scraper checker

This is a bunch of scripts that checks whether the email app is in a healthy state or not by crawling all the links on the index page.

As pages get cached it is most effectively run immediately after a new release.

```
source ve/bin/activate

python email_self_check.py

```

## Notes

All the previous versions of the scripts are still there because I was going to using them as examples of evolving tests scripts.
