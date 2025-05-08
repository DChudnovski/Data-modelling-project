import mysql.connector
import json
import pandas as pd
from pymongo import MongoClient
from dotenv import dotenv_values

ENV = dotenv_values('./.env')

MYSQLUSER = ENV['MYSQLUSER']
MYSQLPW = ENV['MYSQLPW']
MYSQLDB = ENV['MYSQLDB']
MONGOHOST = ENV['MONGOHOST']
MONGOPORT = int(ENV['MONGOPORT'])
MONGODB = ENV['MONGODB']

def get_mysql_to_pandas():
    conn = mysql.connector.connect(user=MYSQLUSER,password=MYSQLPW, database=MYSQLDB,)
    cur = conn.cursor()
    cur.execute('SELECT * FROM sections')
    column_list = cur.description
    col_names =[i[0] for i in column_list]
    df_dict = {key:[] for key in col_names}
    sections_arr = cur.fetchall()
    conn.close()
    for tuple in sections_arr:
        for i, col in enumerate(df_dict.keys()):
            df_dict[f'{col}'].append(tuple[i])
    sections_df = pd.DataFrame().from_dict(df_dict)

    return sections_df  
   

def generate_teacher_schedules(df):
    teacherids = df['teacherid'].unique()
    arr = []
    for i in teacherids:
        result = df.query(f'teacherid == {i}')
        dict = {
            'scheduleid':f"{str('T')}{int(i)}",
            'schedule' : {}
        }
        for _, row in result.iterrows():
            dict['schedule'][f'Period {row["period"]}'] = row['sectionid']
        print(dict)
        # arr.append(dict)
        # return arr
#generate_teacher_schedules(get_mysql_to_pandas())

def generate_student_schedules(df):
    key_list = df.query('period == 1 ')
    for _, row in key_list.iterrows():
        dict = {
            'scheduleid':f"S{int(row['grade'])} {row['sectionid']}",
            'schedule':{}
        }
        s = row['sectionid']
        for i in range(1,6):
            result = df.query(f'sectionid == {s}')
            dict['schedule'][f'Period {i}'] = result['sectionid'].item()
            s += 15
        print(dict)
    pass

generate_student_schedules(get_mysql_to_pandas())

def write_schedules_to_mongo():
    client = MongoClient(host=MONGOHOST, port=MONGOPORT,)
    client.SchoolSchedulesDB.Schedules.find_one()
    client.close()
    pass

#write_schedules_to_mongo()

