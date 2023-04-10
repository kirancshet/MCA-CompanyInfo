#-------------------------------------------------------------------------------
# Name:         company_info.py
# Purpose:      This Python script fetches company information/Director Information from 
#               Ministry of Corporate Affairs Website in Python
# Author:       Kiran Chandrashekhar
# Created:      09-Apr-2023
#-------------------------------------------------------------------------------

import pandas as pd
import requests
import html5lib
from bs4 import BeautifulSoup


def get_header():
    headers = {}
    headers['Origin'] = r'https://www.mca.gov.in'
    headers['Referer'] =  r'https://www.mca.gov.in/mcafoportal/showdirectorMasterData.do'
    headers['Connection'] =  r'keep-alive'
    headers['Accept-Encoding'] =  r'gzip, deflate, br'
    headers['User-Agent'] =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    return headers

#---------------------------------------------------------------
#   Fetch Company Information for the given CIN
#---------------------------------------------------------------
def fetch_company_details(cin):        
    
    mca_url     = r"https://www.mca.gov.in/mcafoportal/companyMasterDataPopup.do"
    company_data = []
  
    headers = get_header()

    param = {'companyid': cin}
    response = requests.post(mca_url, headers=headers, data=param, timeout=10)   

    soup = BeautifulSoup(response.content, 'html.parser')

    tbl = soup.find("table",{"id":"resultsTab2"})

    df = pd.read_html(str(tbl))[0]
    df.columns = ['Attribute', 'Value']

    for index, row in df.iterrows():
        temp = {}
        temp['Attribute'] = row['Attribute']
        temp['Value'] = row['Value']
        company_data.append(temp)

    return company_data

    
if __name__ == '__main__':
    cin = 'U74920DL2005PTC140111'
    company_data = fetch_company_details(cin)
    print(company_data)
    print("Done")