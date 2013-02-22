#!usr/bin/python
#-*-coding:utf-8-*-
import requests, datetime

result=''

start = datetime.datetime.now()
for i in range (0, 30):
	print i
	page = requests.get('https://remixjobs.com/offre/emploi/page/'+str(i))
	temp =page.text
	result = result + temp

print len(result)

answer =[n for n in xrange(len(result)) if result.find('/company/', n) == n]


print result[answer[0]+9:answer[0]+40]

stop = datetime.datetime.now()
#print when the soft started and ended
print str(start)
print str(stop)