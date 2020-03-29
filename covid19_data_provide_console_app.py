import requests, json, sys, pprint


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent)
      else:
         print('\t' * (indent) + str(value))
      print('\t')

def client_cli():
    choice = 1
    print("Welcome to Covid-19 Data Provider\n")
    while(choice != 0):
    
        choice = int(input(
                           "Press 0 - to exit the application\n"+
                           "Press 1 - to view total confirmed, recovered and death cases\n"+
                           "Press 2 - to view confirmed, recovered and death cases per country\n"+
                           "Press 3 - to view only confirmed cases per country\n"))
        if(choice == 1):
            total_covid_amount()
        elif(choice == 2):
            total_per_country()
        elif(choice == 3):
            country_amount()
        else:
            print("Good Bye!")
            break


def total_covid_amount():
    url = "https://covid-19-data.p.rapidapi.com/totals"
    querystring = {"format":"undefined"}
    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "****privateAPI_KEY"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_str = response.text
    resp_dictionary = json.loads(response_str)[0]
    pretty(resp_dictionary)


def total_per_country():
    country_name = input("Please, input a country name: ")
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"undefined","name": country_name}
    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "****privateAPI_KEY"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_str = response.text
    resp_dictionary = json.loads(response_str)[0]
    
    infected = resp_dictionary['confirmed']
    recovered = resp_dictionary['recovered']
    deaths = resp_dictionary['deaths']

    dict_return  = {}
    
    dict_return['confirmed'] = infected
    dict_return['recovered'] = recovered
    dict_return['deaths'] = deaths

    pretty(dict_return)
    
    

def country_amount():
    """The input Countries list """
    countries_list=[]
    length = int(input("How many countries you want to get data about?: "))
    for i in range(length):
        con_name = str(input())
        countries_list.append(con_name)

    """Output is a dict with a country name and confirmed cases"""
    dictionary_to_return = {}
    for country in countries_list:
        url = "https://covid-19-data.p.rapidapi.com/country"
        querystring = {"format":"undefined","name": country}
        headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "****privateAPI_KEY"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_str = response.text
        resp_dictionary = json.loads(response_str)[0]
        infected_amount = resp_dictionary['confirmed']
        dictionary_to_return[country] = infected_amount
    pretty(dictionary_to_return)

client_cli()
