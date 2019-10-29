from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    return webdriver.Chrome("windows/chromedriver")

def scrape_info():
    browser = init_browser()

    #Create a dictionary to store all data and import to MongoDB
    mars_data = {}

    # Visit
    url = 'https://mars.nasa.gov/news'
    browser.get(url)
    time.sleep(1)

    # Scrape page into Soup
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    # Scrape the latest news title
    news_title = soup.find_all('div', class_='content_title')[0]
    news_title = news_title.text.strip()
    
    # get the news paragraph
    news_p = soup.find_all('div', class_='article_teaser_body')[0]
    news_p = news_p.text.strip()

    #store info to dictionary:
    mars_data['latest_news'] = news_title
    mars_data['news_summary'] = news_p

    #Use Selenium to navigate the site and find the image url for the current Featured Mars Image 
    url ='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.get(url)

    html = browser.page_source
    soup = BeautifulSoup (html, 'html.parser')
    
    
    articles = soup.find_all('ul', class_='articles')
    
    for article in articles:
        link = article.find('a')
        href = link['data-fancybox-href']
        title = link ['data-title']
    
    featured_image_url = ['https://www.jpl.nasa.gov' + href]

    mars_data['featured_image_url'] = featured_image_url


    # Get the latest weather tweet
    url ="https://twitter.com/marswxreport?lang=en"
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup (html, 'html.parser')

    mars_weather = soup.find('div', class_= 'js-tweet-text-container').text.strip()

    #store info to dictionary:
    mars_data['mars_weather'] = mars_weather

    #visit the the url below to scrape facts about Mars
    url ="https://space-facts.com/mars/"
    tables = pd.read_html(url)

    # create a dataframe with the scrape and then store into html string
    mars_df = tables[1]
    mars_df.columns = ['Profile', 'Mars']

    mars_html_table = mars_df.to_html()
    mars_html_table

    #store html string to data dictionary
    mars_data[mars_html_table] = mars_html_table

    # Scrape image urls of Mars' hemispheres
    url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    url1 = "https://astrogeology.usgs.gov"
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup (html, 'html.parser')


    images = soup.find_all('div', class_ ='item')
    hemisphere_image_urls = []
    for image in images:
        url = image.find('a', class_='itemLink product-item')
        href = url['href']
        title = image.find('h3').text.strip()
        
        dict_mars_hemisphere = {"title": title, "img_url": url1 + href}
        hemisphere_image_urls.append(dict_mars_hemisphere)
    
    #store list into data dictionary

    mars_data["hemisphere_image_urls"] = hemisphere_image_urls

    browser.close
    
    #Return the dictionary
    return mars_data
 














