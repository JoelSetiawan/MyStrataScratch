import datetime as dt
from pathlib import Path

import pandas as pd

from IPython.display import display

"""
Find the country that has the most companies listed on Forbes

Forbes
Easy
General 

PracticeID 9795

Find the country that has the most companies listed on Forbes.

Output the country along with the number of companies.
DataFrame: forbes_global_2010_2014
Expected Output Type: pandas.DataFrame
forbes_global_2010_2014
company:object
sector:object
industry:object
continent:object
country:object
marketvalue:float64
sales:float64
profits:float64
assets:float64
rank:int64
forbeswebpage:object

Recommended Easy General Practice Questions

    ID 10148
    Find the top 5 cities with the most 5 star businesses

    ID 10354
    Most Profitable Companies
    ID 10026
    Find all wineries which produce wines by possessing aromas of plum, cherry, rose, or hazelnut
    Recommended Forbes Questions

    ID 10354
    Most Profitable Companies

    ID 9797
    Find industries with the highest number of companies
    ID 9663
    Find the most profitable company in the financial sector of the entire world along with its continent

"""

def make_dataframe():
    # r means raw string
    # pathlib is a tool for better working with file paths.
    path_1 = Path(r'csv/forbes_companies_2010_2014.csv')
    path_2 = Path.cwd()
    return pd.read_csv(filepath_or_buffer=path_2.joinpath(path_1), delimiter="\t")


def find_country_with_most_companies_listed_on_forbes(data: pd.DataFrame):

    country_with_most_companies_listed_on_forbes = data.groupby('country').size().sort_values(ascending=False)

    # Verify that it is a Series.
    print(type(country_with_most_companies_listed_on_forbes))
    
    # Let's us display the series values.
    display(country_with_most_companies_listed_on_forbes)

    # Let's us display the series index list.
    display(country_with_most_companies_listed_on_forbes.index.tolist())
    
    # What I learned:
    # The index is stores the country name that we groupedby.

    # This resulting code only prints out the values in the series
    # for country_company_freq in country_with_most_companies_listed_on_forbes:
    #     print(type(country_company_freq))
    #     print(country_company_freq) 

    return country_with_most_companies_listed_on_forbes.index[0]

def find_company_with_most_blank_listed_on_forbes(data: pd.DataFrame, feature_label: str):

    assert(feature_label in data.columns)    
    company_with_most_blank = data.sort_values(by=[feature_label], ascending=False)
    display(company_with_most_blank)
    # display((company_with_most_blank.index.tolist()[0], company_with_most_blank))
    
    
    
if __name__ == "__main__":
    forbes_global_2010_2014 = make_dataframe()
    display(forbes_global_2010_2014)
    find_country_with_most_companies_listed_on_forbes(forbes_global_2010_2014)
    # I can make a generic method to find the country with the most of any one feature:

    # Let's say that I want to figure out which companies have the highest profits listed out of the 100 companies that are in our dataset.
    find_company_with_most_blank_listed_on_forbes(forbes_global_2010_2014, "profits")

    

