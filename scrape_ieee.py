from bs4 import BeautifulSoup
import requests
import spynner

max_pages = 4
page_no = 1
browser = spynner.Browser()

with open('data.csv', 'a') as csvfile:
    fieldnames = ['abstract', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    while page_no <= max_pages:
		url = 'http://ieeexplore.ieee.org/search/searchresult.jsp?queryText=signal%20processing&pageNumber=%d&rowsPerPage=10'%page_no
		browser.load(url)
		source_code = browser.html
		plain_text = source_code.encode('utf-8')
		soup = BeautifulSoup(plain_text, "lxml")
		links = soup.findAll('a',{'class': 'ng-binding ng-scope' })
		links = [link for link in links if link['href'][:2] == "/d"]
		print len(links)
		for link in links:
			url2 = "http://ieeexplore.ieee.org" + link['href']
			print url2
			browser.load(url2)
			source_code = browser.html
			plain_text = source_code.encode('utf-8')
			soup = BeautifulSoup(plain_text, "lxml")	
			div_data =  soup.find('div',attrs={"class":"abstract-text ng-binding"})
			s = div_data.text
			abstract_text = s.split("\n")[0].encode('utf-8')
			writer.writerow({'abstract':abstract_text,'category': "Signal Processing"})