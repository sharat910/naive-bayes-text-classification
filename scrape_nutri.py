import spynner
from bs4 import BeautifulSoup
import csv
import requests

max_pages = 3
page_no = 0
browser = spynner.Browser()
with open('data.csv', 'a') as csvfile:
    fieldnames = ['abstract', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    while page_no <= max_pages:
		url = 'http://www.nrjournal.com/action/doSearch?searchType=quick&searchText=health&occurrences=abstract&journalCode=ntr&searchScope=fullSite&startPage=' + str(page_no)
		page_no += 1
		browser.load(url)
		source_code = browser.html
		plain_text = source_code.encode('utf-8')
		soup = BeautifulSoup(plain_text, "lxml")
		spans = soup.find_all('span', {'class' : 'content'})
		print len(spans)
		for span in spans:
			abstract_text = span.get_text().encode('utf-8')
			writer.writerow({'abstract':abstract_text,'category': "Health and Nutrition"})