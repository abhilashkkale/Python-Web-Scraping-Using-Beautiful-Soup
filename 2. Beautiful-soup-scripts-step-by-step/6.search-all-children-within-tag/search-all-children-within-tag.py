'''
This is a simple python beautiful soup script to fetch all children within a tag based on attribute like class and print the fetched content.

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


# search for all children within the p tag with class name as 'story'
p = soup.find('p', class_ ='story')
all_p_children = p.findChildren()

# Print all children within the p tag with class name as 'story'
print all_p_children
