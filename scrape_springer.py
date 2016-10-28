from bs4 import BeautifulSoup
import csv
import spynner
import requests


max_pages = 2
page_no = 1
browser = spynner.Browser()

with open('data.csv', 'a') as csvfile:
    fieldnames = ['abstract', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    while page_no <= max_pages:
		url = 'http://link.springer.com/search/page/' + str(page_no) + '?facet-discipline=%22Materials%22&facet-subject=%22Materials+Science%2C+general%22&facet-content-type=%22Article%22' 
		page_no += 1
		source_code = requests.get(url)
		plain_text = source_code.text
		#print plain_text
		soup = BeautifulSoup(plain_text, "lxml")
		links = soup.findAll('a',{'class': 'title' })
		#links = [link for link in links if link['href'][:2] == "/a"]
		print len(links)
		for link in links:
			url2 = "http://link.springer.com" + link['href']
			print url2
			browser.load(url2)
			source_code = browser.html
			plain_text = source_code.encode('utf-8')
			soup = BeautifulSoup(plain_text, "lxml")
			p_data =  soup.find('p',attrs={"id":"Par1"})
			if p_data == None:
				p_data =  soup.find('p',attrs={"id":"Para"})		
			try:				
				s = p_data.text
			except:
				continue			
			abstract_text = s.encode('utf-8')			
			writer.writerow({'abstract':abstract_text,'category': "Material Science"})