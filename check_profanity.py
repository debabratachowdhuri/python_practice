import urllib


def read_file():
    quotes = open("movie_quotes.txt")
    contents = quotes.read()
    print (contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print (output)
    connection.close()
read_file()