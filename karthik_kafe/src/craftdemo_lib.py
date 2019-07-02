'''
Created on Jan 13, 2019

@author: ksundaram
'''

import pandas as pd

def prepare_body(customer_data_file,customer_list):
#    print('entered into prepare body',customer_data_file)
    body="{ \n"
#    for cell1 in customer_data_file.index:
    output_val=''
    true_false_flag='n'
    for count in range(len(customer_list)) :
        list_len=len(customer_list[count])
        key=customer_list[count][0]
        value=customer_list[count][1]
        if list_len == 3:
            value_sub=customer_list[count][2]
        elif list_len == 4:
            value_sub=customer_list[count][2]
            marker=customer_list[count][3]
        
#        print('key=',key)
#        print('value=',value)
#            output_val=customer_data_file[key][cell1]
#        print('cell1=',cell1)
        output_val=str(customer_data_file[key])
#        print('output_val=',output_val)
        if output_val.lower() == 'yes':
            output_val='y'
        elif output_val.lower() == 'no':
            output_val='n'

#        print('list_len=',list_len)

        if list_len == 2:
            if len(output_val)  > 0  and output_val != 'nan' :
                if output_val=='y':
                    body=body + '"' + value + '" : true ,\n'
                elif output_val=='n':
                    body=body + '"' + value + '" : false ,\n'
                else:
                    body=body + '"' + value + '" : "' + output_val + '" ,\n'
        elif list_len == 3:
            if len(output_val)  > 0  and output_val != 'nan' :
                if output_val=='y':
                    body=body + '"' + value + '" : { \n "' + value_sub + '" : true \n},\n'
                elif output_val=='n':
                    body=body + '"' + value + '" : { \n "' + value_sub + '" : false \n},\n'
                else:
                    body=body + '"' + value + '" : { \n "' + value_sub + '" : "' + output_val + '" \n},\n'
        elif list_len == 4:
            if len(output_val)  > 0  and output_val != 'nan' :
                if marker == 'begin' :
                    if output_val=='y':
                        body=body + '"' + value + '" : { \n "' + value_sub + '" : true \n},\n'
                    elif output_val=='n':
                        body=body + '"' + value + '" : { \n "' + value_sub + '" : false \n},\n'
                    else:
                        body=body + '"' + value + '" : { \n "' + value_sub + '" : "' + output_val + '",\n'
                elif marker == 'end' :
                    if output_val=='y':
                        body=body + '"' + value_sub + '" : true \n},\n'
                    elif output_val=='n':
                        body=body + '"' + value_sub + '" : false \n},\n'
                    else:
                            body=body + '"' + value_sub + '" : "' + output_val + '"\n},\n'
                else:
                    if output_val=='y':
                        body=body + '"' + value_sub + ' : true,\n'
                    elif output_val=='n':
                        body=body + '"' + value_sub + ' : false,\n'
                    else:
                        body=body + '"' + value_sub + '" : "' + output_val + '",\n'
    
    body=body + ' "domain": "QBO" \n}'
#    print('body=',body) 
    return body
