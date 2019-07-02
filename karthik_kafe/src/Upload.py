'''
Created on Jan 14, 2019

@author: ksundaram
'''
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

url_end_point={
    "query":p.base_url + "/v3/company/" + p.realm_id + "/query?",
    "Customer_insert":p.base_url + "'/v3/company/" + p.realm_id + "/customer",
    "Paymentmethod_insert":p.base_url + "/v3/company/" + p.realm_id + "/paymentmethod",
    "Vendor_insert":p.base_url + "/v3/company/" + p.realm_id + "/vendor",
    "Item_insert":p.base_url + "/v3/company/" + p.realm_id + "/item"
    }

def prepare_body_for_insert(upload_param,action_type):
    global url_end_point
    upload_list=[]
    body=''

    upload_data_file=pa.read_excel('C:/craftdemo/karthik_kafe/data/actual_data.xlsx', sheet_name=upload_param)
    upload_metadata=pa.read_excel('C:/craftdemo/karthik_kafe/data/Api_metadata.xlsx', sheet_name=upload_param+'_metadata')

    for cell in upload_metadata.index:
        vend_column=upload_metadata['Custom Column'][cell]
        metadata_column=upload_metadata['Custom_object_metadata'][cell]
        col_sub=upload_metadata['Custom_object_metadata_sub'][cell]
        col_marker=upload_metadata['marker'][cell]
    
        if str(col_sub) != 'nan' and str(col_marker) != 'nan' :
            upload_list.append((vend_column,metadata_column,col_sub,col_marker))
        elif str(col_sub) != 'nan' and str(col_marker) == 'nan' :
            upload_list.append((vend_column,metadata_column,col_sub))
        elif str(col_sub) == 'nan'   :
            upload_list.append((vend_column,metadata_column))
        else:
            upload_list.append((vend_column,metadata_column))
        
    for i in range(len(upload_data_file)):
        body=cl.prepare_body(upload_data_file.loc[i],upload_list)
        print('body=',body)
        url=url_end_point[upload_param +'_'+ action_type]
        create_data(body,url)


def read_data(upload_param,where_condition):
    intuit_tid='craft_demo_customer_read'
    url = url_end_point['query']
    print('url=',url)
    payload = "Select id from " + upload_param + " where " + where_condition + " STARTPOSITION 1 MAXRESULTS 5\n"
    print('payload=',payload)
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

def create_data(body,url):
    intuit_tid='craft_demo_customer_insert'
#    url = url_end_point['query']
    print('url=',url)
#    url = '{0}/v3/company/{1}/upload'.format(p.base_url, p.realm_id)
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

#prepare_body_for_insert('Customer','insert')
#prepare_body_for_insert('Vendor','insert')
prepare_body_for_insert('Item','insert')
#prepare_body_for_insert('Paymentmethod','insert')
#where_condition=" DisplayName='sethu llc'"
#read_data('Vendor',where_condition)