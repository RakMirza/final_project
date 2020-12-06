from .app import db, DBTable
import json, requests

def scrape():
    r = requests.request('GET',"https://data.cdc.gov/resource/hk9y-quqm.json?&state=US&$limit=240&$offset=0")
    facts = json.loads(r.text)
    data =[]
    for row in facts:      
        state =row['state'] 
        age_group = row['age_group']
        condition_group = row['condition']
        number_covid19_deaths = row['number_covid19_deaths'] 
        data.append((state,age_group,condition_group, number_covid19_deaths))
    #result = dict(zip(range(0, len(data)), data))
    return  data
# this `main` function should run your scraping when 
# this script is ran.
def main():
        f = scrape()
        db.drop_all()
        db.create_all()
        for item in  f:            
            state = item[0]
            age_group = item[1]  
            condition_group = item[2]
            number_covid19_deaths = item[3]        
            new_row = DBTable( state=state,age_group = age_group ,condition_group=condition_group,number_covid19_death=number_covid19_deaths)
            print(new_row)
            db.session.add(new_row)
            db.session.commit()
            

if __name__ == '__main__':
    main()