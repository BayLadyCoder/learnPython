import urllib.request

zip = input('Enter your zip code :')

# represent the webpage that we are going ot connect with this URL
page = urllib.request.urlopen('http://www.uszip.com/zip/' + zip)

code = page.read()
# code.close()
# print(code)
text = code.decode('utf8')

# scraping the number of population for this zipcode
where = text.find('population')

# where the number store exactly (start-end from 'where')
startpop = where + 19
end = startpop + 6

pop = code[startpop:end]
print(pop)
