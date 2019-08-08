# web-scraping-with-python

This script is developped with Python version 3.
It aims to connect to https://www.imdb.com/ and get some relevant informations about movies that were released in 2017 for example,
with the help of module requests of Python which downloads the html page of the site and try to scrap data using the library BeautfulSoup existing in package bs4.

I start scraping the first page, after that i'll iterate through the different pages of movies.

At the end, i'll use the library panda for data visualization.

Python: Version 3

Modules:
- requests with the function get to download the html page given in url
- BeautifulSoup library existing in ps4 package to analyse and extract html elements
- pandas using dataframe to visualize the data scraped in the previous step.

You can save the script on a file locally and then run it using terminal Python3 filename.py.
You can use also an IDE like visual studio code to run it.
