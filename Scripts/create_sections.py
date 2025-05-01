import csv
import pandas as pd
import math

student_csv = r'C:\Tech-Notes\Data Engineering Projects\Data Modelling Project\Data_CSVs\student_data.csv'
teacher_csv = r'C:\Tech-Notes\Data Engineering Projects\Data Modelling Project\Data_CSVs\teacher_data.csv'
section_file = r'C:\Tech-Notes\Data Engineering Projects\Data Modelling Project\Data_CSVs\section_data.csv'
students = pd.read_csv(student_csv)
teachers = pd.read_csv(teacher_csv)

subjects = ['English', 'Mathematics', 'History', 'Science', 'Lunch']
grades = ['6','7','8']

teacher_capacity = {}

grade_counts = {
    '6':0,
    '7':0,
    '8':0
}
for index, row in students.iterrows():
    grade_counts[str(row['grade'])] += 1
sections_needed ={
    '6':0,
    '7':0,
    '8':0
}
for grade_amount in grade_counts.items():
    sections_needed[grade_amount[0]] += math.ceil(grade_amount[1]/20) * 6

total_sections = sum(sections_needed.values())

sections_needed_grade_subject= {}
for subject in subjects:
    for grade in grades:
        sections_needed_grade_subject[f'{subject} {grade}'] = math.ceil(grade_counts[grade] / 20)
for index, row in teachers.iterrows():
    teacher_capacity[f'{row['teacherid']}'] = round(total_sections/teachers.max()['teacherid'])

def generate_sections(sections_needed_dict):
    i = 1
    t = 1
    fields = ['sectionid','teacherid','name','period','grade','capacity','subject']
    with open(section_file, 'w', newline='') as file:
        csv.DictWriter(file,fields).writeheader()
        file.close()
    for section_type, number in sections_needed_dict.items():
        p = 1
        while number > 0:
            if p > 6:
                p = 1
            if t > len(teacher_capacity.keys()):
                t = 1
            section_dict = {
                'sectionid':i,
                'teacherid': t,
                'name': f'{section_type} Period: {p} {i}',
                'period': p ,
                'grade':section_type.split(' ')[1],
                'capacity':20,
                'subject':section_type.split(' ')[0]
            }
            with open(section_file, 'a',newline='') as file:
                writer = csv.DictWriter(file,fields)
                writer.writerow(section_dict)
                file.close()
            number -= 1
            p += 1
            i += 1
            t += 1

generate_sections(sections_needed_grade_subject)
