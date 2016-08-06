![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-MIT%20License-blue.svg)
## Philippine Stock Exchange Historical Data Scraper

This contains the python code for retrieving Philippine publicly listed companies and getting their historical data.
I developed this script to see if we can use machine learning to predict stock prices.

Steps:
- Run the stockslist parser, `python stocklistparser.py`. 
   This retrieves all the available companies from the office PSE portal edge.pse.com.ph and saves them to a csv file

- Run the data miner, `python historicaldatagetter.py`
   This uses the saved stocklist, to retrieve the daily historical data containing opening and closing stock prices for each company, as well as the high and low prices. This will output the data to csv files in the historical data folder with the corresponding company name for its filename.
