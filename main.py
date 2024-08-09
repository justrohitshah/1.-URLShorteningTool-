import pyshorteners

# Function to shorten a URL
def shortURL(longURL):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(longURL))

# get user input
longURL = input("Enter URL:-")

#short the url
shortURL(longURL)


