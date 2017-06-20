from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = "https://scrapebook22.appspot.com"
response = urlopen(url).read()

response = BeautifulSoup(response)

print response.html.head.title.string

csv = open("korisnici.csv", "w")

for item in response.findAll("a"): #s time dobijemo listu stringova s a tagovima (linkovima)
    if item.string == "See full profile":
        #s linka dohvatiti
        newpage = urlopen(url + item["href"]).read()
        #pretvoriti u soap objekt
        soup = BeautifulSoup(newpage)
        print".", #ovo smo stavili da vidimo da program radi, ocitava podatke
        #print ime korisnika onda stavimo print, ako ga spremimo maknemo print

        name = soup.findAll("h1") [1].string #stavili smo 1 jer postoje dva h1 taga, a nama treba drugi


        #ispisati title tag
        #print soup.html.head.title
        #ispisati span tagove
        #print soup.findAll("span", attrs={"class": "email"})
        #da bi dobili van samo spanove moramo sljedece

        email = soup.findAll("span", attrs={"class": "email"}) [0].string #0 iz razloga jer trazimo samo jedan element, email i korisnik ima samo 1 email, a 0 predstavlja prvi element
        csv.write(name + "," +email + "\n") #\n je oznaka za novi red
csv.close()
print "\nCSV je napravljen"



