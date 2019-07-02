'''
Created on Jan 9, 2019

@author: ksundaram
'''
import karthik_kafe_properties as p
from requests import HTTPError
import json
import requests
import datetime
import time 
import os


from intuitlib.client import AuthClient
from intuitlib.migration import migrate
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
import os 
import http 

prop_file_name='c:/craftdemo/karthik_kafe/src/karthik_kafe_properties.py'
new_prop_file_name='c:/craftdemo/karthik_kafe/src/karthik_kafe_properties1.py'
bkp_file='c:/craftdemo/karthik_kafe/src/karthik_kafe_properties.bak'
def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds

start_dt_time=datetime.datetime.strptime(p.last_refresh_date_time,'%Y-%m-%d %H:%M:%S.%f')
current_dt_time=datetime.datetime.now()
elapsed_dt_time=current_dt_time - start_dt_time
hr, min, sec = convert_timedelta(elapsed_dt_time)
print ("hr=",hr)
print ('min=',min)
print('access_token=',p.access_token)
print('refresh_token=',p.refresh_token)
print(' ')
print(' ***************')
print(' ')

# Get a new token for every one hour
# 
if hr > 0 :
    print('entered into hr > 0')
    auth_client = AuthClient(
    p.client_id,
    p.client_secret,
    p.redirect_uri,
    p.environment,
    refresh_token=p.refresh_token,
    access_token=p.access_token
    )
    scopes = [
        Scopes.ACCOUNTING,
    ]
    
#    try:
#        auth_client.refresh()
#    except AuthClientError as e:
#        print(e.status_code)
#        print(e.intuit_tid)
    
    url = auth_client.get_authorization_url(scopes)
    r_token=auth_client.refresh(refresh_token=p.refresh_token)
    access_token=auth_client.access_token    
    auth_header = 'Bearer {0}'.format(access_token)


    fp1=open(new_prop_file_name,'w')
    fp=open(prop_file_name,'r')
    for elem in fp:
#        print('elem=',elem)
        variable=elem.split('=')
        if variable[0] == 'access_token':
            print(variable[0]+'='+ access_token)
            fp1.write(variable[0]+'="'+ access_token +'"\n')
        elif variable[0] == 'refresh_token':
            fp1.write(variable[0]+'="'+ auth_client.refresh_token+'"' + "\n")
        elif variable[0] == "last_refresh_date_time":
            fp1.write(variable[0]+'="'+str(current_dt_time)+'"' + "\n")
        else:
            fp1.write(elem)
    fp.close()
    fp1.close()
    
    if os.path.isfile(bkp_file):
        os.remove(bkp_file)
    os.rename(prop_file_name,bkp_file)
    os.rename(new_prop_file_name,prop_file_name)
else:
    print('hr < 0')
    auth_header = 'Bearer {0}'.format(p.access_token)
        
            

print('auth_header=',auth_header)







