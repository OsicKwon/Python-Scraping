** Basic Pattern


```python

    import re
    import time
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://www.hud.gov/program_offices/housing/rmra/oe/rpts/hecmsfsnap/hecmsfsnap"
    
    response = requests.get(url)
    html = response.text
    
    base_url = "https://www.hud.gov"
    
    soup = BeautifulSoup(html)
    links = soup.find_all("a", string=re.compile("Excel"))

```





** title

```python
    soup.title # <title>The Dormouse's story</title>
    soup.title.name # u'title'
    soup.title.string # u'The Dormouse's story'
    soup.title.parent.name # u'head'
    
    soup.head.title
    soup.body.a.text
    soup.body.p.b
```
