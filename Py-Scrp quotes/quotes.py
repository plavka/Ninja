from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

csv = open("quotes.csv", "w")
quotes = soup.findAll("p", attrs={"class": "quoteContent"}) [0].string

    #print soup.findAll("p", attrs={"class": "quoteContent"})
csv.write(quotes + "\n")
csv.close()

