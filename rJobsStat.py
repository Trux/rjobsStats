#!usr/bin/python
#-*-coding:utf-8-*-
import requests, collections, json
from collections import defaultdict

result=''
companyTemp=[]
companyList=[]
companyRank = {}

start = datetime.datetime.now()
for i in range (0,30):
	page = requests.get('https://remixjobs.com/offre/emploi/page/'+str(i))
	temp =page.text
	result = result + temp

#get company name
answer =[n for n in xrange(len(result)) if result.find('/company/', n) == n]

#get rid of eveything before and after the company's name

for j in range(0,len(answer)):
	companyTemp.append(result[answer[j]+9:answer[j]+40])

for k in range(0,len(companyTemp)):
	end = companyTemp[k].find('/')
	companyList.append(companyTemp[k][0:end])
companyList.sort()

freq = collections.defaultdict(int)
for company in companyList:
    freq[company] += 1

jsonOutput = json.dumps(freq)

stop = datetime.datetime.now()




