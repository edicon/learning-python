'''
Test Module for Copilot
'''
import os
# import beautifulsoup
from bs4 import BeautifulSoup
import requests
import json
#import plotting library form matplotlib
import matplotlib.pyplot as plt

def get_list_of_title() :
    '''Ask the user for a list of books, one per line.'''
    '''global titles; titles = []'''
    titles = []
    while True :
        '''Ctrl-D, Ctrl-C, Enter for exit'''
        new_title = input("Title: ")
        if new_title:
            titles.append(new_title)
        else:
            break
    return titles

# Get the GoodReads API key from the environment
key = os.environ.get("GOODREADS_API_KEY")

def scrape_goodreads(titles) :
    '''Get the average rating of each from GoodReads, and return a list of floats.'''
    ratings = []
    for title in titles :
        url = "https://www.goodreads.com/book/title.xml?key={}&title={}".format(key, title)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        rating = soup.find("average_rating").text
        rating.append(float(rating))
    return ratings

def show(title, ratings) :
    '''Show the titles and ratings in a bar charts.'''
    # Make a bar chart
    plt.bar(range(len(ratings)), ratings)
    # Add labels to the ticks of the bar charts
    plt.xticks(range(len(ratings)), title)
    # Show the plot
    plt.show()

titles = get_list_of_title()
ratings = scrape_goodreads(titles)
show(titles, ratings)

def tab_indent() :
    """Tab Indent"""
    indents = []
    return indents
