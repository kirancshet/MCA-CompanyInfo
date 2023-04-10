#-------------------------------------------------------------------------------
# Name:         utils.py
# Purpose:      This Python script fetches company information/Director Information from 
#               Ministry of Corporate Affairs Website in Python
# Author:       Kiran Chandrashekhar
# Created:      09-Apr-2023
#-------------------------------------------------------------------------------



def get_header():
    headers = {}
    headers['Origin'] = r'https://www.mca.gov.in'
    headers['Referer'] =  r'https://www.mca.gov.in/mcafoportal/showdirectorMasterData.do'
    headers['Connection'] =  r'keep-alive'
    headers['Accept-Encoding'] =  r'gzip, deflate, br'
    headers['User-Agent'] =  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

    return headers
