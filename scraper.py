from bs4 import BeautifulSoup
import csv
import requests

max_pages = 4
page_no = 1

with open('data.csv', 'a') as csvfile:
    fieldnames = ['abstract', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    while page_no <= max_pages:
		url = 'http://projectabstracts.com/tag/asp-net' + '/page/' + str(page_no) +'/'
		page_no += 1
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "lxml")
		links = soup.findAll('a',{'class': 'more-link' })
		print len(links)
		for link in links:
			url2 = link['href']
			source_code = requests.get(url2)
			plain_text = source_code.text
			soup = BeautifulSoup(plain_text, "lxml")
			div_data =  soup.findAll('div',attrs={"class":"entry-content"})
			paras = div_data[0].findAll('p')
			s = ""
			for para in paras:
				s += para.text
			abstract_text = s.split("\n")[0].encode('utf-8')
			writer.writerow({'abstract':abstract_text,'category': "Software Design"})