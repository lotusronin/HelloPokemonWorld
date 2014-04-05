import sys
import subprocess
from bs4 import BeautifulSoup
from gi.repository import Gtk

dls = []

def gethtml(c, s, f):
	for num in range(0, c):
		subprocess.call(["wget", "-q", "-O", f, s])

		soup = BeautifulSoup(open(f))
		dls.append(soup.html.head.title)
		return soup


f = open("zeckendorf.txt", 'r')

line = f.readline().split()
f.close()

morse = ""
total = 0

for x in line:
	total += int(x)
	for digit in str(x):
		f = open(digit+".txt", "r")
		morse += f.readline()
	f.close()

count0 = morse.count("0")
count1 = morse.count("1")

#print(count0, count1)

fname = "site.html"
fname2 = "pokemon.html"
site = "http://en.wikipedia.org/wiki/Special:Random"
pokesite = "http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
pokebase = "http://bulbapedia.bulbagarden.net"

alphas = ["Hel", "lo", " W", "or", "ld"]
counter = 0
#print("Parsing")
ans = ""
while(counter < len(alphas)):
	soup = gethtml(count1, site, fname)
	paragraph = soup.body.find_all('p')

	
	temp = counter
	
	for i in paragraph:
		parsestr = str(i)
		if(alphas[counter] in parsestr):
			idx = parsestr.find(alphas[counter], 0, len(parsestr))
			ans += parsestr[idx:idx+len(alphas[counter])]
			counter += 1

		if(counter >= len(alphas)):
			break

soup = gethtml(1, pokesite, fname2)

if(total > 718):
	total -= 718
if(total > 99):
	totalstr = "#" + str(total)
elif(total > 9):
	totalstr = "#0"+str(total)
else:
	totalstr = "#00"+str(total)


rows = soup.find_all("tr")

pokemon = ""

for row in rows:
	r = str(row.find_all("td"))
	if(totalstr in r):
		href = row.find_all("td")[3].find('a').get('href')
		pokemon = pokebase+href
		break


soup = gethtml(1, pokemon, fname2)
titletag = str(soup.html.head.title)

idxend = titletag.find(" (Pok")
idxbegin = titletag.find(">")
pokename = titletag[idxbegin+1:idxend]

td = str(soup.find(title=pokename).find("img"))
idxbegin = td.find("src=", 0, len(td))
idxend = td.find("srcset=", 0, len(td))
imageurl = td[idxbegin+5:idxend-2]

subprocess.call(["wget", "-q", "-O", pokename+".png", "-A.png", imageurl])
#print(ans)
#print(total)
#print(pokemon)
print(dls)

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)


label = Gtk.Label()
label.set_text(pokename +" says: " + ans + "!")
img = Gtk.Image.new_from_file(pokename+".png")
vbox = Gtk.VBox()

win.add(vbox)

vbox.add(img)
vbox.add(label)
win.show_all()
Gtk.main()