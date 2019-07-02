'''
Created on Jan 8, 2019

@author: ksundaram
'''

import karthik_kafe_properties as p
import os
import refresh_token as r
import requests as req
print("client_id=",p.client_id)
url = '{0}/v3/company/{1}/customer'.format(p.base_url, p.realm_id)
company=''

headers = {
'Authorization': r.auth_header,
'Accept': 'application/json',
'Content-Type': "application/json"
}

print ("header=",str(headers))
cust="""{
    "BillAddr": {
        "Line1": "50 Heritage Village",
        "City": "Sunnyvale",
        "Country": "USA",
        "CountrySubDivisionCode": "CA",
        "PostalCode": "94086"
    },
    "Notes": "Here are other details.",
    "Title": "Mr",
    "GivenName": "jones",
    "MiddleName": "B",
    "FamilyName": "smith",
    "Suffix": "Jr",
    "FullyQualifiedName": "wolfe2 groceries",
    "CompanyName": "Wolfe2 Groceries",
    "DisplayName": "Wolfe2 Groceries",
    "PrimaryPhone": {
        "FreeFormNumber": "(408) 838-4436"
    },
    "PrimaryEmailAddr": {
        "Address": "jsmith@rocketmail.com"
    }
}"""
    
body="""{
  "Title": "Mr",
  "GivenName": "Katie",
  "MiddleName": "f",
  "FamilyName": "Johnson", 
  "DisplayName": "katie4 groceries", 
  "Suffix": "sr",   
  "Notes": "katie4 whole foods", 
  "Taxable": true,
  "PreferredDeliveryMethod": "Email",
  "TaxExemptionReasonId":13,
  "PrimaryPhone": {
    "FreeFormNumber": "(408) 121-3456"
  },
  "Mobile": {
          "FreeFormNumber": "(973) 555-8849"
        },
  "Fax": {
          "FreeFormNumber": "(520) 555-7894"
        },
   "AlternatePhone": {
          "FreeFormNumber": "(828) 555-7894"
        },
  "PrimaryEmailAddr": {
          "Address": "support@katie2groceries.com"
        },
  "WebAddr": {
          "URI": "http://katie2groceries.com"
        },
  "BillAddr": {
        "Line1": "50 Heritage Village",
        "City": "Sunnyvale",
        "Country": "USA",
        "CountrySubDivisionCode": "CA",
        "PostalCode": "94086"
    },
  "ShipAddr": {
        "Line1": "73 Campbell Way",
        "City": "Sunnyvale",
        "Country": "USA",
        "CountrySubDivisionCode": "CA",
        "PostalCode": "94086"
    },
    "Balance": 2000.00,
    "CurrencyRef": {
          "value": "USD",
          "name": "United States Dollar"
      } 
  
}"""

body2="""
{
    "Taxable":True,
    "BillAddr": {
      "City": "Sunnyvale", 
      "Country": "USA", 
      "Line1": "1408 west california ave", 
      "PostalCode": "94086", 
      "CountrySubDivisionCode": "CA"
    }, 
    "ShipAddr": {
      "City": "Mountain View", 
      "Country": "USA", 
      "Line1": "840 Park drive", 
      "PostalCode": "94048", 
      "CountrySubDivisionCode": "CA"
    }, 
    "Job":True,
    "BillWithParent":false,
    "Balance": 2000.00,
    "balancewithJobs": 0,
    "CurrencyRef": {
         "Value": "USD",
         "name": "United States Dollar"
    }, 
    "PrimaryEmailAddr": {
      "Address": "johnyk@rediffmail.com"
    }, 
    "DisplayName": "Johny food mart", 
    "CurrencyRef": {
      "name": "United States Dollar", 
      "value": "USD"
    }, 
    "DefaultTaxCodeRef": {
      "value": "2"
    }, 
    "PreferredDeliveryMethod": "Print", 
    "GivenName": "katie", 
    "FullyQualifiedName": "Katie food mart", 
    "Title": "Mrs", 
    "Job": false, 
    "PrimaryPhone": {
      "FreeFormNumber": "(111) 222-3333"
    }, 
    "Taxable": true, 
    "MiddleName": "B", 
    "Notes": "Katie food mart is a small pop and mom shop", 
    "Active": true, 
    "Suffix": "Jr", 
    "CompanyName": "Katie food mart", 
    "FamilyName": "johnson", 
    "PrintOnCheckName": "Katie food mart"
}
"""
response = req.post(url, headers=headers, data=body)
print (response.status_code)
print (response.content)    
        
    
    