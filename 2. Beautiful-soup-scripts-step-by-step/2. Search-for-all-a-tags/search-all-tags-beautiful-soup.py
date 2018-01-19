'''
This is a simple script which finds all 'a' tags from html with its count using beautiful soup.
'''

from bs4 import BeautifulSoup

html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
<body>
	<p class="title">
		<b>The Dormouse's story</b>
	</p>
	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
	<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# Search for all 'a' tags
a_tags = soup.find_all('a')

# Prints all 'a' tags
print a_tags

# Prints the length of all 'a' tags
print len(a_tags)
