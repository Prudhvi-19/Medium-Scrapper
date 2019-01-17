#import all required libraries for scraping WEB
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from Store_DB import *

"""Scrape Takes Url and send attributes scraped to store_db"""
def scrape(url):
    
    #Requesting Web Page and Parsing it using Beautiful Soup
    req  = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    bsobj = BeautifulSoup(html.read(),'lxml')
    
    #Getting Title from Beautiful Soup Object
    title = bsobj.find_all("h1",{"class":"elevate-h1 u-marginBottom12 u-md-marginBottom8"})
    title = title[0].get_text()
    
    #Getting Sub Title from Beautiful Soup Object
    subtitle = bsobj.find_all("p",{"class":"elevate-summary u-md-marginBottom24"})
    subtitle = subtitle[0].get_text()
   
    #Getting Content from bsobj
    content = bsobj.find_all("div",{"class":"postArticle-content js-postField js-notesSource js-trackedPost"})
    content = content[0].get_text()
    
    #Getting image links from bsobj and storing them in a string form
    images = []
    for img in bsobj.findAll('img'):
        images.append(img.get('src'))
    s = ""
    for i in images:
        s = s + " "+ i


    #Getting Claps from bsobj
    claps = bsobj.find_all("span",{"class":"u-relative u-background js-actionMultirecommendCount u-marginLeft16"})
    claps = claps[0].get_text()
    

    #Getting author from bsobj
    author = bsobj.find_all("h3",{"class":"ui-h2 u-paddingTop4 u-marginBottom4"})
    author = author[0].get_text()
    

    #Getting author_bio from bsobj
    author_bio = bsobj.find_all("p",{"class":"ui-summary u-marginBottom16"})
    author_bio = author_bio[0].get_text()


    #Getting post_date from bsobj
    post_date = bsobj.find_all("time",{"class":"u-inlineBlock u-lineHeightBase"})
    post_date = post_date[0].get_text()
    

    #Getting read_time from bsobj
    read_time = bsobj.find("span",{"class":"readingTime"})['title']
    
    #Passing Values to store_db function to store in Data Base
    store_db(title,subtitle,content,s,claps,author,author_bio,post_date,read_time)