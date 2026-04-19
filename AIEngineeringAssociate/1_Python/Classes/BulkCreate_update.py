# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:09:29 2024

@author: Professor
"""

parents_data =[{'id':'1', 'name':'name1', 'children':[{'id':'a','desrip':'first'},{'id':'b','desrip':'second'}]},
          {'id':'2', 'name':'name2', 'children':[{'id':'a','desrip':'first'}]}]

parent_ids=[parent['id'] for parent in parents_data]



existing_ids = {parent.id for parent in parents_data}

print(existing_ids)