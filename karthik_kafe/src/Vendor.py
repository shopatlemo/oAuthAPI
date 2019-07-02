'''
Created on Jan 14, 2019

@author: ksundaram
'''
'''
Created on Jan 11, 2019

@author: ksundaram
'''

import karthik_kafe_properties as p
import refresh_token as r
import requests as req
import pandas as pa
from pandas import  ExcelWriter
from pandas import ExcelFile
import craftdemo_lib as cl



def prepare_body_for_insert():
    vendor_list=[]
    body=''

    vendor_data_file=pa.read_excel('C:/craftdemo/karthik_kafe/data/customer.xlsx', sheet_name='Vendor')
    vendor_metadata=pa.read_excel('C:/craftdemo/karthik_kafe/data/Api_metadata.xlsx', sheet_name='Vendor_metadata')

    for cell in vendor_metadata.index:
        vend_column=vendor_metadata['Custom Column'][cell]
        metadata_column=vendor_metadata['Customer_object_metadata'][cell]
        col_sub=vendor_metadata['Customer_object_metadata_sub'][cell]
        col_marker=vendor_metadata['marker'][cell]
    
        if str(col_sub) != 'nan' and str(col_marker) != 'nan' :
            vendor_list.append((vend_column,metadata_column,col_sub,col_marker))
        elif str(col_sub) != 'nan' and str(col_marker) == 'nan' :
            vendor_list.append((vend_column,metadata_column,col_sub))
        elif str(col_sub) == 'nan'   :
            vendor_list.append((vend_column,metadata_column))
        else:
            vendor_list.append((vend_column,metadata_column))
        
    for i in range(len(vendor_data_file)):
        body=cl.prepare_body(vendor_data_file.loc[i],vendor_list)
        print('body=',body)
        create_vendor(body)


def read_vendor(vendor_name):
    intuit_tid='craft_demo_customer_read'
    url = '{0}/v3/company/{1}/query?'.format(p.base_url, p.realm_id)
    payload = "Select id from vendor where CompanyName='" + vendor_name + "' STARTPOSITION 1 MAXRESULTS 5\n"
    querystring = {"query":payload,"minorversion":"4"}

    print ('url=',url)
    print('auth_header=',r.auth_header)

    headers={
        'User-Agent': "QBOV3-OAuth2-Postman-Collection",
        'Accept': "application/json",
        'Authorization': r.auth_header,
        'cache-control': "no-cache",
        'intuit_tid':'100_karthik4'
        }
    response = req.request("get", url,  headers=headers, params=querystring)
    print (response.status_code)
#    print (response.content)
    print('text=',response.text)

def create_vendor(body):
    intuit_tid='craft_demo_customer_insert'
    url = '{0}/v3/company/{1}/vendor'.format(p.base_url, p.realm_id)
    headers = {
            'Authorization': r.auth_header,
            'Accept': 'application/json',
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'intuit_tid':intuit_tid
}
    response = req.post(url, headers=headers, data=body)
    print (response.status_code)
    print (response.content) 

prepare_body_for_insert()
#read_vendor('rainbow food court')