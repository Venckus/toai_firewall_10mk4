import os

from pprint import pprint 
import pandas as pd
import json

path='data/access.log'

#### read to json and then to pandas

# log_data=open(path,'r')
# result={}
# i=0
# for line in log_data:
#     data={}
#     columns = line.split(' ') #or w/e you're delimiter/separator is
#     request_str = columns[1].split(' ')
#     r_str = request_str[0][:-1]
#     if "\\x" in r_str: # put SSL label here
#         data['ssl'] = 1
#     else:
#         for c in request_str:
#             key = c.split(' ')[0]
#             val = c.split(' ')[1]
#             data[key] = value
#     result[i]=data
#     i+=1
# print(columns[:2])
# j=json.dumps(columns[:2])
# df=pd.read_json(j, orient='index')


#### read as csv to pandas
df = pd.read_csv(path, sep='\s+' ,header=None)
df.head()