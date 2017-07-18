from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "https://scrapebook22.appspot.com"

response = urlopen(url).read()

response = BeautifulSoup(response)

print response.html.head.title.string

csv = open("korisnici.csv","w")

for item in response.findAll("a"):
    if item.string == "See full profile":
        newpage = urlopen(url + item["href"]).read()
        soup = BeautifulSoup(newpage)
        print ".",
        name = soup.findAll("h1")[1].string
        email = soup.findAll("span", attrs={"class": "email"})[0].string
        csv.write(name + "," +email + "\n")

csv.close()
print "\nCSV je napravljen"