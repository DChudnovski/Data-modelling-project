#This is a utility for generating random student data
import csv
from random import randint,uniform,randrange,random
from datetime import datetime 
import time
import numpy as np
import pandas as pd

student_names_file = '../name_csvs/student_names.csv'
teacher_names_file ='../name_csvs/teacher_names.csv'
student_file = '../Data_CSVs/student_data.csv'
teacher_file = '../Data_CSVs/teacher_data.csv'

def get_rand_name(name_file):
    first_names = []
    last_names = []
    with open(name_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first_names.append(row['FirstName'])
            last_names.append(row['LastName'])
        file.close()
    return (first_names[randint(0,len(first_names)-1)], last_names[randint(0,len(last_names)-1)])

def get_rand_date(start, end, strformat='%Y-%m-%d'):
    start_time = time.mktime(datetime.strptime(start, strformat).timetuple())
    end_time = time.mktime(datetime.strptime(end, strformat).timetuple())

    random_time = start_time + random() * (end_time - start_time)
    return datetime.fromtimestamp(random_time).date()

def generate_student_admin_data(number_of_entries):
    i = 1
    fields = ['studentid','lastname','firstname','grade','GPA','scheduleid','honors','DOB']
    names_list = []
    while i <= number_of_entries:
        i += 1
        names_list.append(get_rand_name(student_names_file))
    with open(student_file,'w',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        file.close()
    for j, name in enumerate(names_list):
        GPA = round(np.random.normal(3.2,.6),2)
        if GPA >= 4.00:
            GPA = 4.0
        DOB = str(get_rand_date('2009-09-01', '2013-09-01'))
        if datetime.strptime(DOB, '%Y-%m-%d').timetuple()[0] <= 2010:
            grade = 8
        elif datetime.strptime(DOB, '%Y-%m-%d').timetuple()[0] > 2010 and datetime.strptime(DOB, '%Y-%m-%d').timetuple()[0] < 2012:
            grade = 7
        else: 
            grade = 6
        scheduleid = f'{format(grade,'0')}' + f'{format(j + 1,'04')}'
        student_dict = {
            'studentid': j + 1,
            'lastname': f"'{name[1]}'",
            'firstname': f"'{name[0]}'",
            'grade': grade,
            'GPA': GPA,
            'scheduleid':0,
            'honors': True if GPA > 3.4 else False,
            'DOB': f"'{DOB}'"
        }
        with open(student_file, 'a',newline='') as file:
            writer = csv.DictWriter(file,fields)
            writer.writerow(student_dict)
            file.close()

def generate_teacher_admin_data(number_of_entries):
    i = 1
    fields = ["teacherid","lastname","firstname","scheduleid","yearstaught"]
    names_list = []
    while i <= number_of_entries:
        names_list.append(get_rand_name(teacher_names_file))
        i += 1
    with open(teacher_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        file.close()
    for j, name in enumerate(names_list):
        subjects = {}
        teacher_dict = {
            "teacherid": j + 1 ,
            "lastname": f"'{name[1]}'",
            "firstname": f"'{name[0]}'",
            "scheduleid":0,
            "yearstaught": randrange(1,30)
        }
        with open (teacher_file, 'a', newline='') as file:
            writer = csv.DictWriter(file,fields)
            writer.writerow(teacher_dict)
            file.close()
def check_student_grades():
    students = pd.read_csv(student_file)
    grade_counts = {
    '6':0,
    '7':0,
    '8':0
    }
    for index, row in students.iterrows():
        grade_counts[str(row['grade'])] += 1
    return grade_counts

print(check_student_grades())

 