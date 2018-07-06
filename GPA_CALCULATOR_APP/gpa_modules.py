# -*- coding: utf-8 -*-
# Created by: PyQt5
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!
def user_input(subjectNumber1,subjectNumber2,subjectNumber3,subjectNumber4,subjectNumber5,subjectNumber6,subjectNumber7,subjectNumber8,subjectCredit9,subjectCredit10,subjectCredit11,subjectCredit12, subjectCredit13, subjectCredit14, subjectCredit15, subjectCredit16,subject_num_array,num_credit_hour_array):
    subject_num_array.append(subjectNumber1)
    subject_num_array.append(subjectNumber2)
    subject_num_array.append(subjectNumber3)
    subject_num_array.append(subjectNumber4)
    subject_num_array.append(subjectNumber5)
    subject_num_array.append(subjectNumber6)
    subject_num_array.append(subjectNumber7)
    subject_num_array.append(subjectNumber8)
    num_credit_hour_array.append(subjectCredit9)
    num_credit_hour_array.append(subjectCredit10)
    num_credit_hour_array.append(subjectCredit11)
    num_credit_hour_array.append(subjectCredit12)
    num_credit_hour_array.append(subjectCredit13)
    num_credit_hour_array.append(subjectCredit14)
    num_credit_hour_array.append(subjectCredit15)
    num_credit_hour_array.append(subjectCredit16)
    return  subject_num_array,num_credit_hour_array

def assign_gpa_points(subject_num_array,subject_gpa_array):
    for index,subjects in enumerate(subject_num_array):
        #print(type(subject_num_array[index]))
        if subject_num_array[index]>=89.5:
            subject_gpa_array.append(4)
        elif subject_num_array[index] >= 84.5:
            subject_gpa_array.append(3.7)
        elif subject_num_array[index] >= 79.5:
            subject_gpa_array.append(3.3)
        elif subject_num_array[index] >= 74.5:
            subject_gpa_array.append(3)
        elif subject_num_array[index] >= 69.5:
            subject_gpa_array.append(2.7)
        elif subject_num_array[index] >= 64.5:
            subject_gpa_array.append(2.3)
        elif subject_num_array[index] >= 59.5:
            subject_gpa_array.append(2.0)
        elif subject_num_array[index] >= 54.5:
            subject_gpa_array.append(1.7)
        elif subject_num_array[index] >=49.5:
            subject_gpa_array.append(1.3)
        else:
            subject_gpa_array.append(0)
    print(subject_gpa_array)

    return subject_gpa_array,
def gpa_calculation(subject_gpa_array,num_credit_hour_array):
    gpa_array=[]
    print('num of  credit hr',num_credit_hour_array)
    #for index in range(len(subject_gpa_array)):
        #gpa_array.append(subject_gpa_array[index]*num_credit_hour_array[index])
    #gpa_array=[12,2,4,5,10,10,10,4]
    gpa_array=[a * b for a, b in zip(subject_gpa_array, num_credit_hour_array)]
    total_gpa=sum(gpa_array)
    #print('total GPA:',total_gpa)
    total_credit_hr=sum(num_credit_hour_array)
    GPA=total_gpa/total_credit_hr
    print('GPA:',GPA)
    return  GPA
