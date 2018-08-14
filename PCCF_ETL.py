# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:28:16 2018

@author: riosa

Commands import PCCF Data Text File and isolate key variables while transforming the data into dictionary or dataframe outputs
"""
import os
import random
import pandas as pd

#Set file working directory

os.getcwd()

os.chdir("H:\\My Documents\Other")

directory = os.getcwd()

#Data Extraction - Import data from file into list format

in_txt = open("pccf.txt", "r")

file_str = in_txt.read()

file_str = file_str.rstrip('\n')

file_list = file_str.split('\n')


#Dictionary

PCCF_Dict = {}

PCCF_columns = ["Pos_Code", "FSA", "PR", "CD_UID", "CSD_UID", "CSD_Name", "CSD_Type", "CCS_Code", "SAC", "SAC_Type"]

PCCF_Column_Code = []

for i in range(10):
    PCCF_Column_Code.append((i, PCCF_columns[i]))

"""
for i in range(len(file_list)-1):
    row_key = str(i) + "-" + file_list[i][0:9]
    PCCF_Dict[row_key] = {}
    PCCF_Dict[row_key]['Pos_Code'] = file_list[i][0:6]
    PCCF_Dict[row_key]['FSA'] = file_list[i][6:9]
    PCCF_Dict[row_key]['PR'] = file_list[i][9:11]
    PCCF_Dict[row_key]['CD_UID'] = file_list[i][11:15]
    PCCF_Dict[row_key]['CSD_UID'] = file_list[i][15:22]
    PCCF_Dict[row_key]['CSD_Name'] = file_list[i][22:92].strip(" ")
    PCCF_Dict[row_key]['CSD_Type'] = file_list[i][92:95].strip(" ")
    PCCF_Dict[row_key]['CCS_Code'] = file_list[i][95:98]
    PCCF_Dict[row_key]['SAC'] = file_list[i][98:101]
    PCCF_Dict[row_key]['SAC_Type'] = file_list[i][101]
    
"""

#Populate Data Dictionary for DataFrame

for i in range(len(file_list)-1):
    row_key = str(i) + "-" + file_list[i][0:9]
    PCCF_Dict[row_key] = []
    PCCF_Dict[row_key].append(file_list[i][0:6])
    PCCF_Dict[row_key].append(file_list[i][6:9])
    PCCF_Dict[row_key].append(file_list[i][9:11])
    PCCF_Dict[row_key].append(file_list[i][11:15])
    PCCF_Dict[row_key].append(file_list[i][15:22])
    PCCF_Dict[row_key].append(file_list[i][22:92].strip(" "))
    PCCF_Dict[row_key].append(file_list[i][92:95].strip(" "))
    PCCF_Dict[row_key].append(file_list[i][95:98])
    PCCF_Dict[row_key].append(file_list[i][98:101])
    PCCF_Dict[row_key].append(file_list[i][101])
    
#Create random sample of dictionary entries for expedient review

sample_Set = random.sample(PCCF_Dict.items(), 15)

#Create DataFrame and label its columns accordingly

PCCF_df = pd.DataFrame.from_dict(PCCF_Dict, orient='index')

PCCF_df.columns = PCCF_columns

#Data Cleaning - Changes PR codes to PR Abbreviations

PCCF_df['PR'] = PCCF_df['PR'].str.replace('10', 'NL')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('11', 'PE')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('12', 'NS')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('13', 'NB')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('24', 'QC')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('35', 'ON')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('46', 'MB')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('47', 'SK')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('48', 'AB')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('59', 'BC')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('60', 'YT')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('61', 'NT')
PCCF_df['PR'] = PCCF_df['PR'].str.replace('62', 'NU')

#Data Visualization - Plot number of entries per province
"""
PR_count = PCCF_df["PR"].value_counts()
plt.figure("PR Entries")
sns.barplot(PR_count.index, PR_count.values, alpha = 0.8)
plt.title("# Records per Province")
plt.xlabel("Provinces", fontsize = 12)
plt.ylabel("Total Records", fontsize = 12)
plt.show()


OR 

g = sns.factorplot("PR", data=PCCF_df, aspect=4.0, kind='count')
"""

#Data Visualization- Compare number of SAC_Types per Province between ON and QC
"""
ON_count = PCCF_df["SAC_Type"][PCCF_df["PR"] == "ON"].value_counts()
QC_count = PCCF_df["SAC_Type"][PCCF_df["PR"] == "QC"].value_counts()
plt.figure("ON vs. QC - # of Records per Sac Type")
sns.barplot(ON_count.index, ON_count.values, alpha = 0.8); plt.xlabel('SAC Types', fontsize=12)
sns.barplot(QC_count.index, QC_count.values, alpha = 0.6); plt.xlabel('SAC Types', fontsize=12)
plt.title("# Records per SAC Type")
plt.xlabel("SAC Types", fontsize = 12)
plt.ylabel("Total Records", fontsize = 12)
plt.show()

OR

ONandQC_df = PCCF_df[(PCCF_df['PR']=='ON') | (PCCF_df['PR']=='QC')]
"""

#Data Visualization - Compare number of SAC_Types per Province between ON and QC without Type 1
"""
ONandQC_df = PCCF_df[((PCCF_df['PR']=='ON') | (PCCF_df['PR']=='QC')) & (PCCF_df['SAC_Type'] != '1')]
"""

#Export Dataframe to Province-Specific CSV File

def PR_Csv_Export(Province_Code):
    
    PR_df = PCCF_df[PCCF_df["PR"]== Province_Code.upper()]
    
    file_path = directory + "\Sample_Python_Files\\" + Province_Code.upper()
    
    file_name = Province_Code + "_PCCF.csv"
     
    if not os.path.exists(file_path):
       
        os.makedirs(file_path)
        
    os.chdir(file_path)
        
    PR_df.to_csv(file_name, sep='\t')
        
    return os.chdir(directory)









