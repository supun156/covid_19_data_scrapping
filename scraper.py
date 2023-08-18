# Importing necessary libraries for the script
import numpy as np  # Library for numerical operations
import pandas as pd  # Library for data manipulation and analysis
import requests  # Library for making HTTP requests
import bs4  # Beautiful Soup library for parsing HTML and XML documents
import lxml.etree as xml  # Library for working with XML data
import re  # Library for regular expressions
import json  # Library for working with JSON data
import datetime  # Library for working with date and time

def generate_data_set(chart_data_text):
    """
    Generates a data set from the chart data text.

    Args:
        chart_data_text (str): The text containing chart data.

    Returns:
        list: A list of dictionaries, each containing date and count data.
    """
    category_regex = r"(?:categories: \[)(.*?)(?:])"
    category_matches = re.findall(category_regex, str(chart_data_text))
    categories = category_matches[0].replace('"', '').split(',')

    data_regex = r"(?:data: \[)(.*?)(?:])"
    data_matches = re.findall(data_regex, str(chart_data_text))
    data_values = data_matches[0].split(',')

    main_data_list = []
    for i, val in enumerate(categories):
        date_time_str = val + ' 2020'
        date_time_obj = datetime.datetime.strptime(date_time_str, '%b %d %Y')
        data_entry = {}
        date = date_time_obj.date()
        data_entry["date"] = str(date)
        count = data_values[i]
        if data_values[i] == "null":
            count = 0
        data_entry["count"] = count
        main_data_list.append(data_entry)
    return main_data_list

def extract_chart_data(chart_name, web_page):
    """
    Extracts chart data from a web page.

    Args:
        chart_name (str): The name of the chart.
        web_page (BeautifulSoup object): The parsed web page.

    Returns:
        list: A list of dictionaries representing the chart data.
    """
    chart_script = web_page.find('script', type="text/javascript", string=re.compile(chart_name))
    chart_data = []
    if chart_script:
        chart_data = generate_data_set(chart_script)
    return chart_data

def read_url(url):
    """
    Reads a URL and extracts COVID-19 data.

    Args:
        url (str): The URL to read.

    Returns:
        dict: A dictionary containing COVID-19 data.
    """
    URL = url
    requests.get(URL)
    web_page = bs4.BeautifulSoup(requests.get(URL, {}).text, "lxml")
    country_data = {}
    country_data['cases_daily'] = extract_chart_data('graph-cases-daily', web_page)
    country_data['deaths_daily'] = extract_chart_data('graph-deaths-daily', web_page)
    return country_data

def get_all_countries_data():
    """
    Retrieves COVID-19 data for all countries.

    Returns:
        dict: A dictionary containing COVID-19 data for all countries.
    """
    world_data = {}
    WORLDOMETERS_URL = "https://www.worldometers.info/coronavirus/"
    requests.get(WORLDOMETERS_URL)
    web_page = bs4.BeautifulSoup(requests.get(WORLDOMETERS_URL, {}).text, "lxml")
    country_table_scripts = web_page.find_all('table', id="main_table_countries_today")
    url_regex = re.compile('(?<=href=").*?(?=")')
    country_urls = url_regex.findall(str(country_table_scripts))

    for i, country_url in enumerate(country_urls):
        if 'world-population' in str(country_url):
            pass
        else:
            country_key = country_url.replace("country/", "").replace("/", "")
            world_data[country_key] = read_url('https://www.worldometers.info/coronavirus/' + country_url)
    
    return world_data

with open('covid19.json', 'w') as outfile:
    json.dump(get_all_countries_data(), outfile)
