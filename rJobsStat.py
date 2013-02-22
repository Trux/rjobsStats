#!usr/bin/python
#-*-coding:utf-8-*-
import requests

page = requests.get('https://remixjobs.com/offre/emploi/at/Paris%2C%20France/lat/48.856614/lng/2.3522219000000177/dist/1000')
result = page.text
where = result.find('class="company"')
print where
print result[where:where+50]