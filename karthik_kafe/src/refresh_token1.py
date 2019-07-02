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


from intuitlib.client import AuthClient
from intuitlib.migration import migrate
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
import os 
import http 

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

url = auth_client.get_authorization_url(scopes)
r_token=auth_client.refresh(refresh_token=p.refresh_token)
print ("refresh=",auth_client.refresh_token)
#auth_client.get_bearer_token(auth_code, realm_id=realm_id)
access_token=auth_client.access_token

url = '{0}/v3/company/{1}/companyinfo/{1}'.format(p.base_url, p.realm_id)
auth_header = 'Bearer {0}'.format(access_token)


