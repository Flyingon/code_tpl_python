from urllib.parse import urlparse, urlencode
#
# o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
#
# print(o)

o2 = urlencode({'token': "**"})

print(o2)