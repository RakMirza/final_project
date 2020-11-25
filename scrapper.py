import requests,json,sys,os


import requests
import json

def scrape():
    data = []
    r = requests.get("https://data.cdc.gov/resource/hk9y-quqm.json?&state=US&$limit=240&$offset=0")
    facts = r.json()
    for rows in facts:      
        State =rows['state'] 
        Age_group = rows['age_group']
        Condition_group = rows['condition']
        Number_covid19_deaths = rows['number_covid19_deaths'] 
        data.append((State,Age_group,Condition_group, Number_covid19_deaths))
    return data

if __name__ == "__main__":
    f  = scrape()
    print(f)
    
