# -*- coding: utf-8 -*-
"""
Andres De los Rios
6/25/2018

Automatic Folder Creation Function - Census Project

Users can create a chain of folders throughout multiple geospatial data
repositories based on CMAs, Census Aglomeration Areas, or Provinces. 
"""
#Automated Indexing Function


import os

file_path = os.getcwd()

CMA_List = ['Chicoutimi-Jonquiere', 'Edmonton', 'Guelph', 'Halifax', \
            'Hamilton', 'Kitchener', 'London', 'Montreal', 'Oshawa', \
            'Ottawa-Hull', 'Quebec', 'Regina', 'Saint John', "Saint John's", \
            'Saskatoon', 'St. Catharines-Niagara', 'Sudbury', 'Thunder Bay', \
            'Toronto', 'Vancouver', 'Victoria', 'Windsor', 'Winnipeg']

Prov_List = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland', 'Nova Scotia', 'Ontario', 'Quebec', 'Saskatchewan']

CensAgglo_List = ['Brantford', 'Kingston', 'Moncton', 'Peterborough', 'Sarnia', 'Sault Ste. Marie', 'Sherbrooke', 'Trois-Rivieres']

def Create_Folders(file_path, boundary_list):
    """
    
    """
    folder_category = input("Would you like to access 1976 or Reference Materials folders?" + '\n')
    
    
    if folder_category == '1976':
        
        for entity in boundary_list:
       
            boundary_file_path = file_path + '/' + folder_category + '/' + entity
            
            if not os.path.exists(boundary_file_path):
                
                if boundary_list == CensAgglo_List:
                    os.makedirs(boundary_file_path + '/' + 'CensusAgglomerationArea')
                
                elif boundary_list == CMA_List:
                    os.makedirs(boundary_file_path + '/' + 'CensusMetropolitanArea')
            
                os.makedirs(boundary_file_path + '/' + 'CensusTracts')
                os.makedirs(boundary_file_path + '/' + 'Unprocessed Files')
                
    elif folder_category.lower() == 'reference materials':
        
        print('\n' + "Existing Years: ")
        for i in os.listdir(file_path + '/' + folder_category):
            print('- ' + i)
        
        year = str(input('Which year would you like to access?' + '\n'))
        
        
        print('\n' + "Existing Boundaries for " + year + ":")
        for i in os.listdir(file_path + '/' + folder_category + '/' + year):
            print('- ' + i)
        
        boundary = str(input("Which boundary would you like to edit?" + '\n'))
        
        for entity in boundary_list:
            
            boundary_file_path = file_path + '/' + folder_category + '/' + year \
            + '/' + boundary + '/' + entity 
                        
            if not os.path.exists(boundary_file_path):
                os.makedirs(boundary_file_path + '/' + 'NAD1983')
                os.makedirs(boundary_file_path + '/' + 'NAD1927')
                
    elif folder_category.lower() == 'exit':
        boundary_list = []
        return boundary_list
    
    else:
        print('Invalid Folder Category - please try again or use \'Exit\' command')
        return(Create_Folders(file_path, boundary_list))

if __name__ == '__main__':
    
    boundary_input = str(input('Which census boundary would you like to work on - CMA, Provinces, or Census Agglomerations?' + '\n')).lower()
    
    if boundary_input == 'cma':
        boundary_list = CMA_List
        
    elif boundary_input == 'provinces':
        boundary_list = Prov_List
        
    elif boundary_input == 'census agglomerations':
        boundary_list = CensAgglo_List
        
    try:
        Create_Folders(file_path, boundary_list)
        
    except NameError:
        print('Invalid Census Boundary - please try again')
        
    
        
    
  

        
        