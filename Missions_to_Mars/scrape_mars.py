# scrape_mars.py
# Import Modules
import pandas as pd
import requests
from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    # Scraping Nasa Mars News
    executable_path={'executable_path':'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_url = 'https://mars.nasa.gov/news/'

    browser.visit(news_url)
    text_news = browser.html
    soup_news = BeautifulSoup(text_news, 'html.parser')

    posts_news = soup_news.find_all(class_='slide')

    titles = posts_news[0].find_all(class_='content_title')
    descriptions = posts_news[0].find_all(class_='article_teaser_body')
    first_title = titles[0].text
    first_description = descriptions[0].text
    browser.quit()

    # Scraping image
    executable_path={'executable_path':'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(image_url)
    text_images = browser.html
    soup_images = BeautifulSoup(text_images, 'html.parser')

    posts_images = soup_images.find_all(class_='thumb')
    first_image = 'https://www.jpl.nasa.gov' + posts_images[0]['src']
    browser.quit()

    # Scrape Mars Weather text and image
    executable_path={'executable_path':'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    weather_url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(weather_url)
    text_weather = browser.html
    soup_weather = BeautifulSoup(text_weather, 'html.parser')

    posts_weather = soup_weather.find_all(class_='TweetTextSize')
    first_weather = posts_weather[0].text
    posts_weather_img = soup_weather.find_all(class_='AdaptiveMedia-photoContainer')
    first_weather_img = posts_weather_img[0].find_all('img')
    first_weather_img_url = first_weather_img[0]['src']
    first_weather_img_url
    browser.quit()

    # Scrape Mars Facts
    facts_url = 'https://space-facts.com/mars/'
    facts_df = pd.read_html(facts_url)

    mars_facts_df = facts_df[0]
    mars_comparison_df = facts_df[1]

    #mars_facts_df.to_html('mars_facts.html')
    #mars_comparison_df.to_html('mars_comparison.html')
    
    

    # Hemisphere Data
    hemi_data = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
]

    scrape_dict = {
        'Featured_Title': first_title,
        'Featured_Description': first_description,
        'Featured_Image': first_image,
        'Current_Weather': first_weather,
        'Current_Weather_pic': first_weather_img_url,
        'Mars_Facts': mars_facts_df.to_string(),
        'Mars_Comparison': mars_comparison_df.to_html(),
        'Hemispheres': hemi_data,
    }

    return scrape_dict

