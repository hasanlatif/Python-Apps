# -*- coding: utf-8 -*-
# Created by: PyQt5
#Author :Hasan Latif
#Email :hasanlatif.pk@gmail.com
# WARNING! All changes made in this file will be lost!
from gpa_modules import user_input
from gpa_modules import assign_gpa_points
from gpa_modules import gpa_calculation


subject_num_array = []
subject_gpa_array = []
num_credit_hour_array = []

if __name__ == '__main__':
    user_input(subject_num_array,num_credit_hour_array)
    assign_gpa_points(subject_num_array, subject_gpa_array)
    gpa_calculation(subject_gpa_array, num_credit_hour_array)