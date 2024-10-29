#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:29:59 2024

@author: maria hochtaubel
"""

import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd


class PerfumeScraper:
    
    def __init__(self, url):
        self.url = url
        self.scraper = cloudscraper.create_scraper()
        self.headers = {}
        self.soup = None
        self.offers = []
        
    def fetch_content(self):
        """Fetch the HTML content from the provided URL"""
        response = self.scraper.get(self.url, headers = self.headers)
        self.soup = BeautifulSoup(response.content, 'html.parser')
        
    def parse_offers(self):
        """Parse the offers data from the HTML content"""
        if self.soup:
            self.offers = self.soup.find_all('div', attrs={'class':'row'})
        else:
            raise ValueError(" ----- Content not fetched. Run fetch_content() first -----")
    
    def extract_offer_data(self):
        """Extract relevant data for each offer and store it in a DataFrame"""
        
        df = pd.DataFrame(columns= ['name', 'price', 'offer_url'])
        num_offers = len(self.offers) - 3
        
        for i in range(1,num_offers+1):
            offer = self.offers[i].find_all('div')
            product = offer[5].get_text()
            # some of the offers has duplicated product name, the line below will fix it
            product = product[product.find(offer[5].get_text().split()[0], product.find(offer[5].get_text().split()[0])+1) if product.find(offer[5].get_text().split()[0], product.find(offer[5].get_text().split()[0])+1) != -1 else 0 :]
            price = offer[6].get_text().strip().split('\n')[0]
            offer_url = offer[6].select_one("[data-url]")['data-url']
            new_row = {'name': product, 'price': price, 'offer_url': offer_url}
            df = df.append(new_row, ignore_index= True)
        df.sort_values(by=['price'], ascending= True, inplace=True)
        return df
    
    def run(self):
        """Run the entire scraping process and return a DataFrame with the offers data"""
        
        self.fetch_content()
        self.parse_offers()
        return self.extract_offer_data()