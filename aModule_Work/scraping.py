# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# scrape all function
def scrape_all():
    # Set executable path and open blank browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # run all scraping functions and store results in dict
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # stop webdriver and reutrn the data
    browser.quit()
    return data


# Create function to pull mars news
def mars_news(browser):
    
    # visit the NASA Mars news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # optional delay for loading the page (also searches for specific combination of tag and attribute)
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # set up the html parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # set up variable to look for slides
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    # return nothing if attribute error (often when webpages format changes)
    except AttributeError:
        return None, None

    return news_title, news_p


### Module 10.3.4 Scrape Mars Featured Image (JPL Space Images Featurded Image)

# function to pull featured image
def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full-image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # add try/except block for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


# create mars facts function
def mars_facts():
    try:
        # Use pandas to read the html on a fact site, then turn their fact table into a pandas df
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None
    
    # assign columns and set index of dataframe
    df.columns = ['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # convert pandas df back to html
    return df.to_html()


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

