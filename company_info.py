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
    def get_company_info(self, cin):        
        company_data = []
        
        try:  
            headers = get_header()

            param = {}
            param['companyid'] = cin

            response = requests.post(self.mca_url, headers=headers, data=param)   

            if response.status_code == 200:
                
                soup = BeautifulSoup(response.content, 'html.parser')
                tbl = soup.find("table",{"id":"resultsTab2"})

                df = pd.read_html(str(tbl))[0]

                df.columns = ['Attribute', 'Value']

                for index, row in df.iterrows():
                    temp = {}
                    temp['Attribute'] = row['Attribute']
                    temp['Value'] = row['Value']
                    company_data.append(temp)


        except Exception as e:
            print(str(e))

        return company_data


def main():    
    cin = 'U74920DL2005PTC140111'
    company_data = CompanyInfo().get_company_info(cin)
    print(company_data)
    
if __name__ == '__main__':
    main()
    print("Done")