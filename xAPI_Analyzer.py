#여기서는 xAPI를 다루는 클래스를 담을 것

import numpy as np
import pandas as pd

class Analyzer:

    def __init__(self, df_data):
        #unique한 actor의 배열
        self.df_data = df_data
        self.unique_actor = df_data['actor'].unique()
        self.unique_object = df_data['object'].unique()
        self.unique_verb = df_data['verb'].unique()
        
        self.actor = df_data['actor']

    def analyze_activities(self, average = True):
        student_total_logs = {}

        for student in self.unique_actor:
            student_total_logs[student] = len(self.df_data[self.actor == student])

        sorted_total_logs = sorted(student_total_logs.items(), key = lambda x: x[1], reverse = True)

        students = []
        total_logs = []

        for stu, log in sorted_total_logs:
            students.append(stu)
            total_logs.append(log)
        
        #평균을 더하고 싶지 않다면 average 값을 False로 주면 됨
        if average:
            students.append('average')
            #평균 더하기
            np_total_logs = np.array(total_logs)
            total_logs.append(np_total_logs.mean())

        return students, total_logs

    def analyze_watching_time(self):
        
        pass
