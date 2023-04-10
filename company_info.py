#-------------------------------------------------------------------------------
# Name:         company_info.py
# Purpose:      This Python script fetches company information/Director Information from 
#               Ministry of Corporate Affairs Website in Python
# Author:       Kiran Chandrashekhar
# Created:      09-Apr-2023
#-------------------------------------------------------------------------------

from utils import get_header
import pandas as pd
import requests
import html5lib

from bs4 import BeautifulSoup

#---------------------------------------------------------------
#   Fetch Company Information from MCA
#---------------------------------------------------------------

class CompanyInfo:
    def __init__(self):
        self.mca_url     = r"https://www.mca.gov.in/mcafoportal/companyMasterDataPopup.do"

    #---------------------------------------------------------------
    #   Fetch Company Information for the given CIN
    #---------------------------------------------------------------
    def fetch_company_details(self, cin):        
       
        data = {}
        try:  
            headers = get_header()

            param = {}
            param['companyid'] = cin

            response = requests.post(self.mca_url, headers=headers, data=param, timeout=10)   

            print(response)
            print(response.status_code)

            if response.status_code == 200:

                soup = BeautifulSoup(response.content, 'html.parser')
                company_info = self.parse_company_info(soup)
                director_details = self.parse_director_info(soup)


                data['company_info'] = company_info
                data['director_info'] = director_details

        except Exception as e:
            print(str(e))

        return data
    
    #---------------------------------------------------------------
    #  Parse Director Information from the parsed HTML
    #---------------------------------------------------------------
    def parse_director_info(self, soup):
        director_data = []

        tbl = soup.find("table",{"id":"resultsTab7"})

        if tbl is not None:
            df = pd.read_html(str(tbl))[0]
            director_data = df.to_dict('records')
        
        return director_data
    
    #---------------------------------------------------------------
    #  Parse Company Information from the parsed HTML
    #---------------------------------------------------------------
    def parse_company_info(self, soup):
        company_data = []

        tbl = soup.find("table",{"id":"resultsTab2"})

        df = pd.read_html(str(tbl))[0]
        df.columns = ['Attribute', 'Value']

        for index, row in df.iterrows():
            temp = {}
            temp['Attribute'] = row['Attribute']
            temp['Value'] = row['Value']
            company_data.append(temp)
        
        return company_data


def main():    
    cin = 'U74920DL2005PTC140111'
    company_data = CompanyInfo().fetch_company_details(cin)
    print(company_data)
    
if __name__ == '__main__':
    main()
    print("Done")