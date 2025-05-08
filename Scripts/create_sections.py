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
    class_cap = 20
    ratio = grade_amount[1]/class_cap
    if math.remainder(grade_amount[1], class_cap) > 0 and math.remainder(grade_amount[1], class_cap) / class_cap  < 0.6:
        sections_needed[grade_amount[0]] = (math.floor(ratio), class_cap + (grade_amount[1] % class_cap))
    else:
        sections_needed[grade_amount[0]] = (math.ceil(ratio), grade_amount[1] % class_cap)

total_sections = 0
for tuple in sections_needed.values():
    total_sections += tuple[0]
    

sections_needed_grade_period= {}
for i in range(1,6):
    for grade in grades:
        sections_needed_grade_period[f'{i} {grade}'] = sections_needed[f'{grade}']
# print(sections_needed_grade_period)
# quit()

teacher_capacity = {}
for index, row in teachers.iterrows():
    teacher_capacity[f'{row["teacherid"]}'] = round(total_sections/teachers.max()['teacherid'])

def generate_sections(sections_needed_dict):
    i = 1
    t = 1
    s = 0
    s6 = 0
    s7 = 0
    s8 = 0
    fields = ['sectionid','teacherid','name','period','grade','capacity','subject']
    with open(section_file, 'w', newline='') as file:
        csv.DictWriter(file,fields).writeheader()
        file.close()
    for period_grade, tuple in sections_needed_dict.items():
        counter = tuple[0]
        while counter > 0:
            if s > 4:
                s = 0
            if t > len(teacher_capacity.keys()):
                t = 1
            grade = int(period_grade.split(" ")[1])
            if grade == 6:
                s = s6
                s6 += 1
            elif grade == 7:
                s = s7
                s7 += 1
            else:
                s = s8
                s8 += 1
            if s6 > 4:
                s6 = 0
            if s7 > 4:
                s7 = 0
            if s8 > 4:
                s8 = 0
            period = int(period_grade.split(" ")[0])
            subject = f"{subjects[s]}"
            section_dict = {
                'sectionid':i,
                'teacherid': t,
                'name':f"'{subject} {grade} Period: {period} [{i}]'",
                'period':period,
                'grade': grade,
                'capacity':20 if counter > 1 else tuple [1],
                'subject':f"'{subject}'"
            }
            with open(section_file, 'a',newline='') as file:
                writer = csv.DictWriter(file,fields)
                writer.writerow(section_dict)
                file.close()
            t += 1
            i += 1
            counter -= 1
        
        

generate_sections(sections_needed_grade_period)
