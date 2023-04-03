import pyshorteners

#long URL goes here
link_input  = input('What link would you like to shorten?\n')
link = link_input

#initialize the Shortener
shortener = pyshorteners.Shortener()

#short the url with tinyurl
url = shortener.tinyurl.short(link)

#print shortened url
print(url)

