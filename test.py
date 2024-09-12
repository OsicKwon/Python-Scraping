** title

soup.title # <title>The Dormouse's story</title>
soup.title.name # u'title'
soup.title.string # u'The Dormouse's story'
soup.title.parent.name # u'head'

soup.head.title
soup.body.a.text
soup.body.p.b



** soup

soup.p # <p class="title"><b>The Dormouse's story</b></p>
soup.p['class'] # u'title'
soup.a # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>



** find

>> <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
soup.find(id="link3") 
soup.find(class_="sister")  # note that 'class_' not just 'class'

    
** find_all

# http://example.com/elsi, # http://example.com/lacie
for link in soup.find_all('a'):
    print(link.get('href')) 
    
soup.find_all('a') # [<a ..>, ..]

soup.find_all("title") # tag condition
soup.find_all("p", "title") # tag and attr
# [<p class="title"><b>The Dormouse's story</b></p>]
soup.find_all("a")

# keyword arguments
soup.find_all(id="link2")
soup.find_all(href=re.compile("elsie"), id='link1')
soup.find(string=re.compile("sisters")) # text contain sisters

# css class (class is researved keyword)
soup.find_all("a", class_="sister")


soup.find_all(attrs={"class" : "name_of_class"})



** select vs find(find_all)

- result: Beautifulsoup = soup.find( ~
- result: List[str] = soup.select( ~

#  SELECT method - CSS selector
#  Note that the elements extracted by the SELECT method are in the form of list, pay attention to add inDex when getting text
soup.select('p') #  Find all P elements according to the label name, equal to Soup.Find_all ('P')
soup.select('.sister') #  Find labels for class = sister through CSS properties
soup.select('#link1') #  Find all ID = # link1 elements by id = # link1
soup.select('p #link1') #  Combine lookup ID = # link11 P elements
soup.select("head > title") #  Find child elements Title of the Head tag
soup.select('a[class="sister"]') #  Find all attributes a tag for Sister
soup.select('a[href="http://example.com/elsie"]') #Find href = xxx A tag elements
soup.select('p')[0].get_text() #  Get the text of the first P element
soup.select('a[href*=".com/el"]')[0].attrs['href'] #Get xxx.com HREF

https://www.programmerall.com/article/63351096826/



** get

# Get the "a" tag
element = soup.find('a')# Get the attribute value
data = element.get('href')


