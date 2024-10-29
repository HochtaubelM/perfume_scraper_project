# Perfume Data Scraper

This project is a GUI-based application that scrapes perfume offer data from predefined URLs and displays it in a structured table format. Built using Python, it leverages web scraping and data handling libraries to fetch, parse, and display data, making it easy to view and analyze perfume offers.

## Features

Scrapes perfume offer data (name, price, and offer URL) from specified e-commerce URLs.
Displays the data in a sortable table within a GUI.
Built-in dropdown menu for selecting specific perfumes to scrape.
Organized error handling for a smooth user experience.

## Project Structure

- perfume_scraper.py: Contains the PerfumeScraper class, which handles the entire scraping process, including fetching, parsing, and structuring data into a pandas DataFrame.
- perfume_scraper_gui.py: Implements the GUI for the application using customtkinter, allowing users to select perfumes, trigger data scraping, and view results in a table format.

## Dependencies

- cloudscraper: For handling Cloudflare-protected requests.
- beautifulsoup4: For HTML parsing.
- pandas: For data handling and structuring.
- customtkinter: For building a custom-styled GUI.

## Install dependencies with:

pip install cloudscraper beautifulsoup4 pandas customtkinter

## Note:

The PerfumeScraper class was specifically built to fetch data from offers listed on www.perfumehub.pl. If you intend to use this scraper on a different website, modifications to the parsing logic may be required to ensure compatibility with the new site’s HTML structure.
