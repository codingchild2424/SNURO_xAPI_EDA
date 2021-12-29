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

    def personal_watching_time(self, actor):
        
        #actor의 df을 불러옴
        df_actor = self.df_data[self.actor == actor]

        sorted_df_actor = df_actor.sort_values(by = 'timestamp')

        sorted_df_actor.replace({
            '시청기록': 1,
            '시청중': 2,
            '실행': 3,
            '중지': 4,
            '퀴즈/메시지 등장': 5,
            '퀴즈/메시지 응답': 6,
            '강의 평가 등장': 7,
            '강의 평가 제출': 8,
            '재생바 클릭': 9
        }, inplace= True)

        verb_list = sorted_df_actor['verb']

        return verb_list

    #코드가 지저분한데, 나중에 정리할 필요가 있음
    def analyze_watching_time(self):
        #'시청기록', '시청중', '실행', '중지', '퀴즈/메시지 등장', '퀴즈/메시지 응답', '강의 평가 등장', '강의 평가 제출'
        verb_list1 = []
        verb_list2 = []
        verb_list3 = []
        verb_list4 = []
        verb_list5 = []
        verb_list6 = []
        verb_list7 = []
        verb_list8 = []
        #학생별로 verb의 수를 정리
        #학생을 한명 불러오고 그 학생의 verb의 수를 리스트에 기록
        for student in self.unique_actor:

            verb1_count = 0
            verb2_count = 0
            verb3_count = 0
            verb4_count = 0
            verb5_count = 0
            verb6_count = 0
            verb7_count = 0
            verb8_count = 0

            for verb in self.df_data[self.actor == student]['verb']:
                #'시청기록', '시청중', '실행', '중지', '퀴즈/메시지 등장', '퀴즈/메시지 응답', '강의 평가 등장', '강의 평가 제출'
                if verb == "시청기록":
                    verb1_count += 1
                elif verb == "시청중":
                    verb2_count += 1
                elif verb == "실행":
                    verb3_count += 1
                elif verb == "중지":
                    verb4_count += 1
                elif verb == "퀴즈/메시지 등장":
                    verb5_count += 1
                elif verb == "퀴즈/메시지 응답":
                    verb6_count += 1
                elif verb == "강의 평가 등장":
                    verb7_count += 1
                elif verb == "강의 평가 제출":
                    verb8_count += 1

            verb_list1.append(verb1_count)
            verb_list2.append(verb2_count)
            verb_list3.append(verb3_count)
            verb_list4.append(verb4_count)
            verb_list5.append(verb5_count)
            verb_list6.append(verb6_count)
            verb_list7.append(verb7_count)
            verb_list8.append(verb8_count)

        data1 = np.array(verb_list1)
        data2 = np.array(verb_list2)
        data3 = np.array(verb_list3)
        data4 = np.array(verb_list4)
        data5 = np.array(verb_list5)
        data6 = np.array(verb_list6)
        data7 = np.array(verb_list7)
        data8 = np.array(verb_list8)

        data_list = [data1, data2, data3, data4, data5, data6, data7, data8]

        unique_actor = self.unique_actor

        return unique_actor, data_list