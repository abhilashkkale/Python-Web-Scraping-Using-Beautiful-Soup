'''
This is a simple python beautiful soup script to check the scope of the beautiful soup object.

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
	and they lived at the bottom of a well.
	</p>
	
	<p class="story">...</p>

</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

# Fetch contents of first p tag
first_p = soup.find('p')

# Fetch & print a tag within the above fetched p tag but returns none as there is no a tag in 1st p tag
print first_p.find('a')

# Fetch & print a tag within the above fetched p tag
print first_p.find('b')












